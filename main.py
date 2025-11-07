#https://github.com/SurawutSukkum/Python_YOLOV5_Basler_Opencv/blob/main/HIKrobotTest.py#L688

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PySide6.QtGui import QPixmap, QImage

import os
from ctypes import *
from MvCameraControl_class import *

import numpy as np
import cv2



#entry point
if __name__ == "__main__":

    app = QApplication(sys.argv)
    MvCamera.MV_CC_Initialize()
    deviceList = MV_CC_DEVICE_INFO_LIST()

    # find all cam
    ret = MvCamera.MV_CC_EnumDevices(MV_GIGE_DEVICE, deviceList)
    if ret != 0:
        print("enum devices fail! ret[0x%x]" % ret)
        sys.exit()

    if deviceList.nDeviceNum == 0:
        print("find no device!")
        sys.exit()

    print ("Find %d devices!" % deviceList.nDeviceNum)

    # print info for all  gige cam
    for i in range(0, deviceList.nDeviceNum):
        mvcc_dev_info = cast(deviceList.pDeviceInfo[i], POINTER(MV_CC_DEVICE_INFO)).contents
        if mvcc_dev_info.nTLayerType == MV_GIGE_DEVICE or mvcc_dev_info.nTLayerType == MV_GENTL_GIGE_DEVICE:
            print("\ngige device: [%d]" % i)
            strModeName = ''.join([chr(c) for c in mvcc_dev_info.SpecialInfo.stGigEInfo.chModelName if c != 0])
            print("device model name: %s" % strModeName)
            nip1 = ((mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0xff000000) >> 24)
            nip2 = ((mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0x00ff0000) >> 16)
            nip3 = ((mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0x0000ff00) >> 8)
            nip4 = (mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0x000000ff)
            print("current ip: %d.%d.%d.%d\n" % (nip1, nip2, nip3, nip4))

    # connect to 0 id cam
    nConnectionNum = 0
    if int(nConnectionNum) >= deviceList.nDeviceNum:
        print("intput error!")
        sys.exit()

    # create cam obj
    cam = MvCamera()
    stDeviceList = cast(deviceList.pDeviceInfo[int(nConnectionNum)], POINTER(MV_CC_DEVICE_INFO)).contents

    # create handle
    ret = cam.MV_CC_CreateHandle(stDeviceList)
    if ret != 0:
        print ("create handle fail! ret[0x%x]" % ret)
        sys.exit()

    # open cam
    ret = cam.MV_CC_OpenDevice(MV_ACCESS_Exclusive, 0)
    if ret != 0:
        print ("open device fail! ret[0x%x]" % ret)
        sys.exit()

    # Detection network optimal package size(It only works for the GigE camera)
    if stDeviceList.nTLayerType == MV_GIGE_DEVICE or stDeviceList.nTLayerType == MV_GENTL_GIGE_DEVICE:
        nPacketSize = cam.MV_CC_GetOptimalPacketSize()
        if int(nPacketSize) > 0:
            ret = cam.MV_CC_SetIntValue("GevSCPSPacketSize",nPacketSize)
            if ret != 0:
                print ("Warning: Set Packet Size fail! ret[0x%x]" % ret)
        else:
            print ("Warning: Get Packet Size fail! ret[0x%x]" % nPacketSize)

    #Set trigger mode as off
    ret = cam.MV_CC_SetEnumValue("TriggerMode", MV_TRIGGER_MODE_OFF)
    if ret != 0:
        print ("set trigger mode fail! ret[0x%x]" % ret)
        sys.exit()
    #Set GainAuto as off
    ret = cam.MV_CC_SetEnumValue("GainAuto", MV_GAIN_MODE_OFF)
    if ret != 0:
        print ("set GainAuto mode fail! ret[0x%x]" % ret)
        sys.exit()
    # Set BalanceWhiteAuto as off
    ret = cam.MV_CC_SetEnumValue("BalanceWhiteAuto", MV_BALANCEWHITE_AUTO_OFF)
    if ret != 0:
        print ("set GainAuto mode fail! ret[0x%x]" % ret)
        sys.exit()
    # Set ExposureAuto  as off
    ret = cam.MV_CC_SetEnumValue("ExposureAuto", MV_EXPOSURE_AUTO_MODE_OFF)
    if ret != 0:
        print ("set ExposureAuto mode fail! ret[0x%x]" % ret)
        sys.exit()
    # Set ExposureTime
    ret = cam.MV_CC_SetFloatValue("ExposureTime", 10000)
    if ret != 0:
        print ("set ExposureTime fail! ret[0x%x]" % ret)
        sys.exit()
    # Set Gain
    ret = cam.MV_CC_SetFloatValue("Gain",5.0 )
    if ret != 0:
        print ("set Gain fail! ret[0x%x]" % ret)
        sys.exit()


    # Start grab image
    ret = cam.MV_CC_StartGrabbing()
    if ret != 0:
        print ("start grabbing fail! ret[0x%x]" % ret)
        sys.exit()

    # get image

    label = QLabel()
    label.setWindowTitle("Камера")
    label.resize(720, 540)
    label.show()

    ######################################################################################
    while True:
        try:
            stOutFrame = MV_FRAME_OUT()  # переменная выходного фрейм  тип данных
            memset(byref(stOutFrame), 0, sizeof(stOutFrame))  # заполняем всю структуру нулями
            ret = cam.MV_CC_GetImageBuffer(stOutFrame, 10000)  # читаем из буфера камеры
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
                ret = cam.MV_CC_ConvertPixelType(stConvertParam) # конвертируем пиксели в правильном порядке
                if ret != 0:
                    print("convert pixel fail! ret[0x%x]" % ret)
                    del stConvertParam.pSrcData
                    sys.exit()

                img_buff = (c_ubyte * stConvertParam.nDstLen)()
                cdll.msvcrt.memcpy(byref(img_buff), stConvertParam.pDstBuffer, stConvertParam.nDstLen) # копирование данных
                img_buff = np.frombuffer(img_buff, count=int(stConvertParam.nDstBufferSize), # преобразование в np массив
                                         dtype=np.uint8)  # data以流的形式读入转化成ndarray对象
                img_buff = img_buff.reshape(stOutFrame.stFrameInfo.nHeight, stOutFrame.stFrameInfo.nWidth, 3)

                img_color_rbb = cv2.cvtColor(img_buff,cv2.COLOR_BGR2RGB)
                heightImg, widthImg, channelsImg = img_color_rbb.shape
                bytes_per_lineImg = channelsImg * widthImg

                q_image = QImage(img_color_rbb.data, widthImg, heightImg, bytes_per_lineImg, QImage.Format_RGB888)
                q_pixmap = QPixmap.fromImage(q_image)
                q_pixmap2 = q_pixmap.copy()
                label.setPixmap(q_pixmap2)

                nRet = cam.MV_CC_FreeImageBuffer(stOutFrame)
                cv2.waitKey()

            else:
                print("no data[0x%x]" % ret)

        except Exception as e:
            print("no data[0x%x]")

    # Close device
    ret = cam.MV_CC_CloseDevice()
    if ret != 0:
        print ("close deivce fail! ret[0x%x]" % ret)
        sys.exit()
    # Destroy handle
    ret = cam.MV_CC_DestroyHandle()
    if ret != 0:
        print ("destroy handle fail! ret[0x%x]" % ret)
        sys.exit()

    sys.exit(app.exec())