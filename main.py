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


def IsImageColor(enType):
    dates = {
        PixelType_Gvsp_RGB8_Packed: 'color',
        PixelType_Gvsp_BGR8_Packed: 'color',
        PixelType_Gvsp_YUV422_Packed: 'color',
        PixelType_Gvsp_YUV422_YUYV_Packed: 'color',
        PixelType_Gvsp_BayerGR8: 'color',
        PixelType_Gvsp_BayerRG8: 'color',
        PixelType_Gvsp_BayerGB8: 'color',
        PixelType_Gvsp_BayerBG8: 'color',
        PixelType_Gvsp_BayerGB10: 'color',
        PixelType_Gvsp_BayerGB10_Packed: 'color',
        PixelType_Gvsp_BayerBG10: 'color',
        PixelType_Gvsp_BayerBG10_Packed: 'color',
        PixelType_Gvsp_BayerRG10: 'color',
        PixelType_Gvsp_BayerRG10_Packed: 'color',
        PixelType_Gvsp_BayerGR10: 'color',
        PixelType_Gvsp_BayerGR10_Packed: 'color',
        PixelType_Gvsp_BayerGB12: 'color',
        PixelType_Gvsp_BayerGB12_Packed: 'color',
        PixelType_Gvsp_BayerBG12: 'color',
        PixelType_Gvsp_BayerBG12_Packed: 'color',
        PixelType_Gvsp_BayerRG12: 'color',
        PixelType_Gvsp_BayerRG12_Packed: 'color',
        PixelType_Gvsp_BayerGR12: 'color',
        PixelType_Gvsp_BayerGR12_Packed: 'color',
        PixelType_Gvsp_Mono8: 'mono',
        PixelType_Gvsp_Mono10: 'mono',
        PixelType_Gvsp_Mono10_Packed: 'mono',
        PixelType_Gvsp_Mono12: 'mono',
        PixelType_Gvsp_Mono12_Packed: 'mono'}
    return dates.get(enType, '未知')



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

    # Start grab image
    ret = cam.MV_CC_StartGrabbing()
    if ret != 0:
        print ("start grabbing fail! ret[0x%x]" % ret)
        sys.exit()

    ######################################################################################
    # get image
    stOutFrame = MV_FRAME_OUT()  #  переменная выходного фрейм  тип данных
    memset(byref(stOutFrame), 0, sizeof(stOutFrame))  # заполняем всю структуру нулями
    ret = cam.MV_CC_GetImageBuffer(stOutFrame, 1000)  # читаем из буфера камеры
    img_buff = None
    if None != stOutFrame.pBufAddr and 0 == ret:
        print("MV_CC_GetImageBuffer: Width[%d], Height[%d], nFrameNum[%d]" % (stOutFrame.stFrameInfo.nWidth,
                                                                              stOutFrame.stFrameInfo.nHeight,
                                                                              stOutFrame.stFrameInfo.nFrameNum))
        stConvertParam = MV_CC_PIXEL_CONVERT_PARAM()
        memset(byref(stConvertParam), 0, sizeof(stConvertParam))
        #check color
        if IsImageColor(stOutFrame.stFrameInfo.enPixelType) == 'mono':
            print("mono!")
            stConvertParam.enDstPixelType = PixelType_Gvsp_Mono8
            nConvertSize = stOutFrame.stFrameInfo.nWidth * stOutFrame.stFrameInfo.nHeight
        elif IsImageColor(stOutFrame.stFrameInfo.enPixelType) == 'color':
            print("color!")
            stConvertParam.enDstPixelType = PixelType_Gvsp_BGR8_Packed  # opecv要用BGR，不能使用RGB
            nConvertSize = stOutFrame.stFrameInfo.nWidth * stOutFrame.stFrameInfo.nHeight * 3  # размер цветного кадра
        else:
            print("not support!!!")

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
        else:
            print("convert ok!!")
        if IsImageColor(stOutFrame.stFrameInfo.enPixelType) == 'mono':
            img_buff = (c_ubyte * stConvertParam.nDstLen)() # создаем буфер изображения из безнаковых байтов
            cdll.msvcrt.memcpy(byref(img_buff), stConvertParam.pDstBuffer, stConvertParam.nDstLen)
            img_buff = np.frombuffer(img_buff, count=int(stConvertParam.nDstBufferSize), dtype=np.uint8)
            img_buff = img_buff.reshape((stOutFrame.stFrameInfo.nHeight, stOutFrame.stFrameInfo.nWidth))
            print("mono ok!!")
            image_show(image=img_buff)
        if IsImageColor(stOutFrame.stFrameInfo.enPixelType) == 'color':
            img_buff = (c_ubyte * stConvertParam.nDstLen)()
            cdll.msvcrt.memcpy(byref(img_buff), stConvertParam.pDstBuffer, stConvertParam.nDstLen) # копирование данных
            img_buff = np.frombuffer(img_buff, count=int(stConvertParam.nDstBufferSize), # преобразование в np массив
                                     dtype=np.uint8)  # data以流的形式读入转化成ndarray对象
            img_buff = img_buff.reshape(stOutFrame.stFrameInfo.nHeight, stOutFrame.stFrameInfo.nWidth, 3)
            print("color ok!!")

            heightImg, widthImg, channelsImg = img_buff.shape
            bytes_per_lineImg = channelsImg * widthImg

            q_image = QImage(img_buff.data, widthImg, heightImg, bytes_per_lineImg, QImage.Format_RGB888)
            q_pixmap = QPixmap.fromImage(q_image)

            label = QLabel()
            label.setPixmap(q_pixmap)
            label.show()



            # show image
            #cv2.imshow('HLA Label Inspection', img_buff)
            #cv2.waitKey()



            #label.show()
        else:
            print("no data[0x%x]" % ret)



    nRet = cam.MV_CC_FreeImageBuffer(stOutFrame)

    # Close device аывавыав
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