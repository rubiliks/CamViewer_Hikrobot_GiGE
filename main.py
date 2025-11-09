import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QMainWindow, QPushButton
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import QTimer

from MvCameraControl_class import *

import numpy as np
import cv2
import time

import torch
from ultralytics import YOLO


x_global = False
mem_connect = False

def _update_cam_list(cam_link,cam_list_link):
    ret = cam_link.MV_CC_EnumDevices(MV_GIGE_DEVICE, cam_list_link)
    if ret != 0:
        print("enum devices fail! ret[0x%x]" % ret)
        sys.exit()
    if cam_list_link.nDeviceNum == 0:
        print("find no device!")
        sys.exit()
    print("Find %d devices!" % cam_list_link.nDeviceNum)
    # print info for all  gige cam
    for i in range(0, cam_list_link.nDeviceNum):
        mvcc_dev_info = cast(cam_list_link.pDeviceInfo[i], POINTER(MV_CC_DEVICE_INFO)).contents
        if mvcc_dev_info.nTLayerType == MV_GIGE_DEVICE or mvcc_dev_info.nTLayerType == MV_GENTL_GIGE_DEVICE:
            print("\ngige device: [%d]" % i)
            strModeName = ''.join([chr(c) for c in mvcc_dev_info.SpecialInfo.stGigEInfo.chModelName if c != 0])
            print("device model name: %s" % strModeName)
            nip1 = ((mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0xff000000) >> 24)
            nip2 = ((mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0x00ff0000) >> 16)
            nip3 = ((mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0x0000ff00) >> 8)
            nip4 = (mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0x000000ff)
            print("current ip: %d.%d.%d.%d\n" % (nip1, nip2, nip3, nip4))

def _create_cam_handle(st_device_list):
    ret = cam.MV_CC_CreateHandle(st_device_list)
    if ret != 0:
        print ("create handle fail! ret[0x%x]" % ret)
        sys.exit()

def _open_cam(cam_link,st_device_list):
    ret = cam_link.MV_CC_OpenDevice(MV_ACCESS_Exclusive, 0)
    if ret != 0:
        print("open device fail! ret[0x%x]" % ret)
        sys.exit()

    # Detection network optimal package size(It only works for the GigE camera)
    if st_device_list.nTLayerType == MV_GIGE_DEVICE or st_device_list.nTLayerType == MV_GENTL_GIGE_DEVICE:
        nPacketSize = cam_link.MV_CC_GetOptimalPacketSize()
        if int(nPacketSize) > 0:
            ret = cam_link.MV_CC_SetIntValue("GevSCPSPacketSize",nPacketSize)
            if ret != 0:
                print ("Warning: Set Packet Size fail! ret[0x%x]" % ret)
        else:
            print ("Warning: Get Packet Size fail! ret[0x%x]" % nPacketSize)

def _set_camera_setting(cam_link):
    print("Set camera setting")
    #Set trigger mode as off
    ret = cam_link.MV_CC_SetEnumValue("TriggerMode", MV_TRIGGER_MODE_OFF)
    if ret != 0:
        print ("set trigger mode fail! ret[0x%x]" % ret)
        sys.exit()
    ret = cam_link.MV_CC_SetEnumValue("GainAuto", MV_GAIN_MODE_OFF)
    if ret != 0:
        print("set GainAuto mode fail! ret[0x%x]" % ret)
        sys.exit()
    # Set BalanceWhiteAuto as off
    ret = cam_link.MV_CC_SetEnumValue("BalanceWhiteAuto", MV_BALANCEWHITE_AUTO_OFF)
    if ret != 0:
        print("set GainAuto mode fail! ret[0x%x]" % ret)
        sys.exit()
    # Set ExposureAuto  as off
    ret = cam_link.MV_CC_SetEnumValue("ExposureAuto", MV_EXPOSURE_AUTO_MODE_OFF)
    if ret != 0:
        print("set ExposureAuto mode fail! ret[0x%x]" % ret)
        sys.exit()
    # Set ExposureTime
    ret = cam_link.MV_CC_SetFloatValue("ExposureTime", 10000)
    if ret != 0:
        print("set ExposureTime fail! ret[0x%x]" % ret)
        sys.exit()
    # Set Gain
    ret = cam_link.MV_CC_SetFloatValue("Gain", 5.0)
    if ret != 0:
        print("set Gain fail! ret[0x%x]" % ret)
        sys.exit()

def _start_grab(cam_link):
    ret = cam_link.MV_CC_StartGrabbing()
    if ret != 0:
        print ("start grabbing fail! ret[0x%x]" % ret)
        sys.exit()

def _close_cam(cam_link):
    ret = cam_link.MV_CC_CloseDevice()
    if ret != 0:
        print ("close deivce fail! ret[0x%x]" % ret)
        sys.exit()

def _destroy_handle(cam_link):
    ret = cam_link.MV_CC_DestroyHandle()
    if ret != 0:
        print ("destroy handle fail! ret[0x%x]" % ret)
        sys.exit()

def _get_one_frame(cam_link,lable_link,model):
    global x_global
    if x_global == True:
        start_time = time.time()
        stOutFrame = MV_FRAME_OUT()  # переменная выходного фрейм  тип данных
        memset(byref(stOutFrame), 0, sizeof(stOutFrame))  # заполняем всю структуру нулями
        ret = cam_link.MV_CC_GetImageBuffer(stOutFrame, 10000)  # читаем из буфера камеры
        img_buff = None
        if None != stOutFrame.pBufAddr and 0 == ret:
            print("MV_CC_GetImageBuffer: Width[%d], Height[%d], nFrameNum[%d]" % (stOutFrame.stFrameInfo.nWidth,
                                                                                  stOutFrame.stFrameInfo.nHeight,
                                                                                  stOutFrame.stFrameInfo.nFrameNum))
            stConvertParam = MV_CC_PIXEL_CONVERT_PARAM()
            memset(byref(stConvertParam), 0, sizeof(stConvertParam))
            stConvertParam.enDstPixelType = PixelType_Gvsp_BGR8_Packed  # opecv要用BGR，不能使用RGB
            nConvertSize = stOutFrame.stFrameInfo.nWidth * stOutFrame.stFrameInfo.nHeight * 3  # размер цветного кадра
            # convert pixel
            if img_buff is None:
                img_buff = (c_ubyte * stOutFrame.stFrameInfo.nFrameLen)()
            stConvertParam.nWidth = stOutFrame.stFrameInfo.nWidth
            stConvertParam.nHeight = stOutFrame.stFrameInfo.nHeight
            stConvertParam.pSrcData = cast(stOutFrame.pBufAddr, POINTER(c_ubyte))
            stConvertParam.nSrcDataLen = stOutFrame.stFrameInfo.nFrameLen
            stConvertParam.enSrcPixelType = stOutFrame.stFrameInfo.enPixelType
            stConvertParam.pDstBuffer = (c_ubyte * nConvertSize)()
            stConvertParam.nDstBufferSize = nConvertSize
            ret = cam_link.MV_CC_ConvertPixelType(stConvertParam)  # конвертируем пиксели в правильном порядке
            if ret != 0:
                print("convert pixel fail! ret[0x%x]" % ret)
                del stConvertParam.pSrcData
                sys.exit()
            img_buff = (c_ubyte * stConvertParam.nDstLen)()
            cdll.msvcrt.memcpy(byref(img_buff), stConvertParam.pDstBuffer, stConvertParam.nDstLen)  # копирование данных
            img_buff = np.frombuffer(img_buff, count=int(stConvertParam.nDstBufferSize),  # преобразование в np массив
                                     dtype=np.uint8)  # data以流的形式读入转化成ndarray对象
            img_buff = img_buff.reshape(stOutFrame.stFrameInfo.nHeight, stOutFrame.stFrameInfo.nWidth, 3)

            img_color_rbb = cv2.cvtColor(img_buff, cv2.COLOR_BGR2RGB)
            heightImg, widthImg, channelsImg = img_color_rbb.shape
            bytes_per_lineImg = channelsImg * widthImg

            results = model(img_color_rbb)
            annotated_frame = results[0].plot()

            q_image = QImage(annotated_frame.data, widthImg, heightImg, bytes_per_lineImg, QImage.Format_RGB888)
            q_pixmap = QPixmap.fromImage(q_image)
            q_pixmap2 = q_pixmap.copy()

            nRet = cam_link.MV_CC_FreeImageBuffer(stOutFrame)

            end_time = time.time()
            execution_time = end_time - start_time
            fps = 1 / execution_time
            print(f"Время выполнения: {execution_time:.6f} секунд, FPS: {fps:.6f}")
            lable_link.setPixmap(q_pixmap2)
        else:
            lable_link.clear()
            lable_link =  QLabel("Hikrobot camera")
            print("no data[0x%x]" % ret)

def _funck():
    global x_global
    x_global = not x_global
    if x_global == True:
        print("Start grab image")
    else:
        print("Stop Grab")

def _serch_connect_grab(cam,deviceList,button_star_grab):
    global mem_connect
    if mem_connect == False:
        _update_cam_list(cam,deviceList)
        if int(nConnectionNum) >= deviceList.nDeviceNum:
            print("intput error!")
            sys.exit()
        stDeviceList = cast(deviceList.pDeviceInfo[int(nConnectionNum)], POINTER(MV_CC_DEVICE_INFO)).contents
        _create_cam_handle(stDeviceList)
        _open_cam(cam,stDeviceList)
        _set_camera_setting(cam)
        _start_grab(cam)
        mem_connect = True
        button_star_grab.setEnabled(True)
    else:
        _close_cam(cam)
        _destroy_handle(cam)
        mem_connect = False
        button_star_grab.setEnabled(False)


if __name__ == "__main__":
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"Using device: {device}")
    print(f"PyTorch version: {torch.__version__}")
    print(f"CUDA available: {torch.cuda.is_available()}")
    print(f"CUDA version: {torch.version.cuda}")
    print(f"GPU device: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'None'}")

    app = QApplication(sys.argv)
    #model = YOLO('yolov8n.pt')
    model = YOLO('EMG_2025_24_06_v1.onnx')

    window = QMainWindow()
    window.setWindowTitle("Hikrobot")
    window.setGeometry(100, 100, 800, 600)

    central_widget = QWidget()
    window.setCentralWidget(central_widget)

    layout = QVBoxLayout(central_widget)
    label = QLabel("Hikrobot camera", window)
    label.setWindowTitle("Камера")
    label.resize(720, 540)
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    button_star_grab = QPushButton("Start/stop grabing")
    button_connect_disconect = QPushButton("Connect/disconect camera")
    button_star_grab.setEnabled(False)

    layout.addWidget(label)
    layout.addWidget(button_connect_disconect)
    layout.addWidget(button_star_grab)

    window.show()

    cam = MvCamera()

    MvCamera.MV_CC_Initialize()
    nConnectionNum = 0
    deviceList = MV_CC_DEVICE_INFO_LIST()

    button_star_grab.clicked.connect(_funck)
    button_connect_disconect.clicked.connect(lambda:_serch_connect_grab(cam, deviceList,button_star_grab))

    timer = QTimer()
    timer.setInterval(10)
    timer.timeout.connect(lambda:_get_one_frame(cam,label,model))
    timer.start()

    sys.exit(app.exec())