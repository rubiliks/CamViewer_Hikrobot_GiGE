import numpy as np
import cv2
import logging

from PySide6.QtCore import QObject, Signal, Slot
from sympy import false
from MvImport.MvCameraControl_class import *

logger = logging.getLogger(__name__)

class HikCam(QObject):
    cam_сon_discon_sig = Signal()
    cam_finded_camera_sig = Signal()
    cam_not_finded_sig = Signal()
    def __init__(self):
        super().__init__()
        self.cam = MvCamera()
        MvCamera.MV_CC_Initialize()
        self.nConnectionNum = 0
        self.deviceList = MV_CC_DEVICE_INFO_LIST()
        self.mem_connect = False
        self.stDeviceList = 0
        self.ExposureTime = 40
        self.Gain = 23.98
        self.BalanceRed = 1460
        self.BalanceGreen = 1024
        self.BalanceBlue = 1957
        self.cam_now_connect = False
        self.cam_find = False

    def update_cam_list(self):
        ret = self.cam.MV_CC_EnumDevices(MV_GIGE_DEVICE, self.deviceList)
        if ret != 0:
            logger.error("enum devices fail! ret[0x%x]" % ret)
            sys.exit()
        if self.deviceList.nDeviceNum == 0:
            logger.error("find no device!")
            #sys.exit()
            self.cam_find = False
            self.cam_not_finded_sig.emit()

        logger.info("Find %d devices!" % self.deviceList.nDeviceNum)
        # print info for all  gige cam
        for i in range(0, self.deviceList.nDeviceNum):
            mvcc_dev_info = cast(self.deviceList.pDeviceInfo[i], POINTER(MV_CC_DEVICE_INFO)).contents
            if mvcc_dev_info.nTLayerType == MV_GIGE_DEVICE or mvcc_dev_info.nTLayerType == MV_GENTL_GIGE_DEVICE:
                logger.info("gige device: [%d]" % i)
                strModeName = ''.join([chr(c) for c in mvcc_dev_info.SpecialInfo.stGigEInfo.chModelName if c != 0])
                logger.info("device model name: %s" % strModeName)
                nip1 = ((mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0xff000000) >> 24)
                nip2 = ((mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0x00ff0000) >> 16)
                nip3 = ((mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0x0000ff00) >> 8)
                nip4 = (mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0x000000ff)
                logger.info("current ip: %d.%d.%d.%d" % (nip1, nip2, nip3, nip4))
        if self.deviceList.nDeviceNum > 0:
            self.cam_find = True
            self.cam_finded_camera_sig.emit()


    def create_cam_handle_open_setting_start_grab(self):
        # _update_cam_list
        if int(self.nConnectionNum) >= self.deviceList.nDeviceNum:
            logger.error("intput error!")
            sys.exit()
        self.stDeviceList = cast(self.deviceList.pDeviceInfo[int(self.nConnectionNum)], POINTER(MV_CC_DEVICE_INFO)).contents

        # _сreate Handle
        ret = self.cam.MV_CC_CreateHandle(self.stDeviceList)
        if ret != 0:
            logger.error("create handle fail! ret[0x%x]" % ret)
            sys.exit()
        else:
            logger.info("created handle")

        # _open camera
        ret = self.cam.MV_CC_OpenDevice(MV_ACCESS_Exclusive, 0)
        if ret != 0:
            logger.error("open device fail! ret[0x%x]" % ret)
            sys.exit()
        else:
            logger.info("device open")

        # _set_camera_setting
        # Set trigger mode as off
        ret = self.cam.MV_CC_SetEnumValue("TriggerMode", MV_TRIGGER_MODE_OFF)
        if ret != 0:
            logger.error("set trigger mode fail! ret[0x%x]" % ret)
            sys.exit()
        else:
            logger.info("set trigger mode off")

        # Set gain mode
        #ret = self.cam.MV_CC_SetEnumValue("GainAuto", MV_GAIN_MODE_OFF)
        #if ret != 0:
        #    logger.error("set GainAuto mode fail! ret[0x%x]" % ret)
        #    sys.exit()
        #else:
        #    logger.info("set GainAuto mode off")

        # set Exposure Time Mode Standard =0
        #ret = self.cam.MV_CC_SetEnumValue("ExposureTimeMode", 0)
        #if ret != 0:
        #    logger.error("set ExposureTimeMode fail! ret[0x%x]" % ret)
        #    sys.exit()
        #else:
        #    logger.info("set ExposureTimeMode Mode Standard - 0")

        # set Preamp Gain 3200
        ret = self.cam.MV_CC_SetEnumValue("PreampGain", 2400)
        if ret != 0:
            logger.error("set PreampGain fail! ret[0x%x]" % ret)
            sys.exit()
        else:
            logger.info("set PreampGainMode 3.2")

        #set PixelFormat  BayerRG8 - 0x01080009
        ret = self.cam.MV_CC_SetEnumValue("PixelFormat",0x01080009)
        if ret != 0:
            logger.error("set PixelFormat fail! ret[0x%x]" % ret)
            sys.exit()
        else:
            logger.info("set PixelFormat BayerRG8" )

        #set balance white auto BalanceWhiteAuto - Off - 0
        ret = self.cam.MV_CC_SetEnumValue("BalanceWhiteAuto", 0)
        if ret != 0:
            logger.error("set BalanceWhiteAuto fail! ret[0x%x]" % ret)
            sys.exit()
        else:
            logger.info("set BalanceWhiteAuto Off - 0")

        #set Balance Ratio Selector  red  - 0
        ret = self.cam.MV_CC_SetEnumValue("BalanceRatioSelector", 0)
        if ret != 0:
            logger.error("set BalanceRatioSelector fail! ret[0x%x]" % ret)
            sys.exit()
        else:
            logger.info("set BalanceRatioSelector Red - 0")

        #set red BalanceRatio
        ret = self.cam.MV_CC_SetIntValueEx("BalanceRatio",1460)
        if ret != 0:
            logger.error("set BalanceRatio fail! ret[0x%x]" % ret)
            sys.exit()
        else:
            logger.info("set BalanceRatio Red")

        # set Balance Ratio Selector  green - 1
        ret = self.cam.MV_CC_SetEnumValue("BalanceRatioSelector", 1)
        if ret != 0:
            logger.error("set BalanceRatioSelector fail! ret[0x%x]" % ret)
            sys.exit()
        else:
            logger.info("set BalanceRatioSelector Green - 1")

        # set green BalanceRatio
        ret = self.cam.MV_CC_SetIntValueEx("BalanceRatio", 1024)
        if ret != 0:
            logger.error("set BalanceRatio fail! ret[0x%x]" % ret)
            sys.exit()
        else:
            logger.info("set BalanceRatio Green")

        # set Balance Ratio Selector  blue - 2
        ret = self.cam.MV_CC_SetEnumValue("BalanceRatioSelector", 2)
        if ret != 0:
            logger.error("set BalanceRatioSelector fail! ret[0x%x]" % ret)
            sys.exit()
        else:
            logger.info("set BalanceRatioSelector Blue - 2")

        # set blue BalanceRatio
        ret = self.cam.MV_CC_SetIntValueEx("BalanceRatio", 1957)
        if ret != 0:
            logger.error("set BalanceRatio fail! ret[0x%x]" % ret)
            sys.exit()
        else:
            logger.info("set BalanceRatio Blue")

        # Set BalanceWhiteAuto as off
        ret = self.cam.MV_CC_SetEnumValue("BalanceWhiteAuto", MV_BALANCEWHITE_AUTO_OFF)
        if ret != 0:
            logger.error("set BalanceWhiteAuto mode fail! ret[0x%x]" % ret)
            sys.exit()
        else:
            logger.info("set BalanceWhiteAuto mode off")

        # Set ExposureAuto  as off
        ret = self.cam.MV_CC_SetEnumValue("ExposureAuto", MV_EXPOSURE_AUTO_MODE_OFF)
        if ret != 0:
            logger.error("set ExposureAuto mode fail! ret[0x%x]" % ret)
            sys.exit()
        else:
            logger.info("set ExposureAuto mode off")

        # Set ExposureTime
        ret = self.cam.MV_CC_SetFloatValue("ExposureTime", self.ExposureTime)
        if ret != 0:
            logger.error("set ExposureTime fail! ret[0x%x]" % ret)
            sys.exit()
        else:
            logger.info(f"set ExposureTime {self.ExposureTime}")

        # Set Gain
        ret = self.cam.MV_CC_SetFloatValue("Gain", self.Gain)
        if ret != 0:
            logger.error("set Gain fail! ret[0x%x]" % ret)
            sys.exit()
        else:
            logger.info(f"set Gain {self.Gain}")
        # Start grabbing
        ret = self.cam.MV_CC_StartGrabbing()
        if ret != 0:
            logger.error("start grabbing fail! ret[0x%x]" % ret)
            sys.exit()
        else:
            logger.info("start grabbing ")
            self.cam_сon_discon_sig.emit()

    def get_one_frame(self):
        stOutFrame = MV_FRAME_OUT()  # переменная выходного фрейм  тип данных
        memset(byref(stOutFrame), 0, sizeof(stOutFrame))  # заполняем всю структуру нулями
        ret = self.cam.MV_CC_GetImageBuffer(stOutFrame, 10000)  # читаем из буфера камеры
        img_buff = None
        if None != stOutFrame.pBufAddr and 0 == ret:
            logger.info("MV_CC_GetImageBuffer: Width[%d], Height[%d], nFrameNum[%d]" % (stOutFrame.stFrameInfo.nWidth, stOutFrame.stFrameInfo.nHeight, stOutFrame.stFrameInfo.nFrameNum))
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
            ret = self.cam.MV_CC_ConvertPixelType(stConvertParam)  # конвертируем пиксели в правильном порядке
            if ret != 0:
                logger.error("convert pixel fail! ret[0x%x]" % ret)
                del stConvertParam.pSrcData
                sys.exit()
            img_buff = (c_ubyte * stConvertParam.nDstLen)()
            ctypes.memmove(ctypes.byref(img_buff), stConvertParam.pDstBuffer, stConvertParam.nDstLen) # копирование данных
            img_buff = np.frombuffer(img_buff, count=int(stConvertParam.nDstBufferSize),  # преобразование в np массив
                                     dtype=np.uint8)  # data以流的形式读入转化成ndarray对象
            img_buff = img_buff.reshape(stOutFrame.stFrameInfo.nHeight, stOutFrame.stFrameInfo.nWidth, 3)
            nRet = self.cam.MV_CC_FreeImageBuffer(stOutFrame)
            if ret != 0:
                logger.error("MV_CC_FreeImageBuffer fail! ret[0x%x]" % ret)
                del stConvertParam.pSrcData
                sys.exit()
            return img_buff
        else:
            imageError = cv2.imread('./resources/no_cam_connect.png')
            logger.error("no data[0x%x]" % ret)
            return imageError

    def close_grab_destroy_handle(self):
        ret = self.cam.MV_CC_CloseDevice()
        if ret != 0:
            logger.error("close deivce fail! ret[0x%x]" % ret)
            sys.exit()
        else:
            logger.info("deivce close")

        ret = self.cam.MV_CC_DestroyHandle()
        if ret != 0:
            logger.error("destroy handle fail! ret[0x%x]" % ret)
            sys.exit()
        else:
            logger.info("handle destroy")
            self.cam_сon_discon_sig.emit()

    def get_exposure(self,value):
        self.ExposureTime =  value

    def get_gain(self,value):
        self.Gain = value

    def get_BalanceRed(self,value):
        self.BalanceRed = value

    def get_BalanceGreen(self,value):
        self.BalanceGreen = value

    def get_BalanceBlue(self,value):
        self.BalanceBlue = value





