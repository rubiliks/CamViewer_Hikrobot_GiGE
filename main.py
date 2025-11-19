import numpy as np
import cv2
import time

import logging

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QMainWindow, QPushButton
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import QTimer

from MvCameraControl_class import *

import pymodbus
from pymodbus.client import ModbusTcpClient

import torch
from ultralytics import YOLO

from mainWindowSmir import Ui_MainWindow


class HikCam():
    def __init__(self,number):
        self.number = number
        self.cam = MvCamera()
        MvCamera.MV_CC_Initialize()
        self.nConnectionNum = 0
        self.deviceList = MV_CC_DEVICE_INFO_LIST()
        self.mem_connect = False
        self.stDeviceList = 0
        self.ExposureTime = 10000
        self.Gain = 2.0

    def update_cam_list(self):
        ret = self.cam.MV_CC_EnumDevices(MV_GIGE_DEVICE, self.deviceList)
        if ret != 0:
            print("enum devices fail! ret[0x%x]" % ret)
            sys.exit()
        if self.deviceList.nDeviceNum == 0:
            print("find no device!")
            sys.exit()
        print("Find %d devices!" % self.deviceList.nDeviceNum)
        # print info for all  gige cam
        for i in range(0, self.deviceList.nDeviceNum):
            mvcc_dev_info = cast(self.deviceList.pDeviceInfo[i], POINTER(MV_CC_DEVICE_INFO)).contents
            if mvcc_dev_info.nTLayerType == MV_GIGE_DEVICE or mvcc_dev_info.nTLayerType == MV_GENTL_GIGE_DEVICE:
                print("\ngige device: [%d]" % i)
                strModeName = ''.join([chr(c) for c in mvcc_dev_info.SpecialInfo.stGigEInfo.chModelName if c != 0])
                print("device model name: %s" % strModeName)
                nip1 = ((mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0xff000000) >> 24)
                nip2 = ((mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0x00ff0000) >> 16)
                nip3 = ((mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0x0000ff00) >> 8)
                nip4 = (mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0x000000ff)
                print("current ip: %d.%d.%d.%d\n" % (nip1, nip2, nip3, nip4))

    def create_cam_handle_open_setting_start_grab(self):

        # _update_cam_list
        if int(self.nConnectionNum) >= self.deviceList.nDeviceNum:
            print("intput error!")
            sys.exit()
        self.stDeviceList = cast(self.deviceList.pDeviceInfo[int(self.nConnectionNum)], POINTER(MV_CC_DEVICE_INFO)).contents

        # _сreate Handle
        ret = self.cam.MV_CC_CreateHandle(self.stDeviceList)
        if ret != 0:
            print("create handle fail! ret[0x%x]" % ret)
            sys.exit()
        else:
            print("created handle ")

        # _open camera
        ret = self.cam.MV_CC_OpenDevice(MV_ACCESS_Exclusive, 0)
        if ret != 0:
            print("open device fail! ret[0x%x]" % ret)
            sys.exit()
        else:
            print("device open ")

        # _set_camera_setting
        print("set camera setting")
        # Set trigger mode as off
        ret = self.cam.MV_CC_SetEnumValue("TriggerMode", MV_TRIGGER_MODE_OFF)
        if ret != 0:
            print("set trigger mode fail! ret[0x%x]" % ret)
            sys.exit()
        else:
            print("set trigger mode off")

        # Set gain mode
        ret = self.cam.MV_CC_SetEnumValue("GainAuto", MV_GAIN_MODE_OFF)
        if ret != 0:
            print("set GainAuto mode fail! ret[0x%x]" % ret)
            sys.exit()
        else:
            print("set GainAuto mode off")

        # Set BalanceWhiteAuto as off
        ret = self.cam.MV_CC_SetEnumValue("BalanceWhiteAuto", MV_BALANCEWHITE_AUTO_OFF)
        if ret != 0:
            print("set BalanceWhiteAuto mode fail! ret[0x%x]" % ret)
            sys.exit()
        else:
            print("set BalanceWhiteAuto mode off")

        # Set ExposureAuto  as off
        ret = self.cam.MV_CC_SetEnumValue("ExposureAuto", MV_EXPOSURE_AUTO_MODE_OFF)
        if ret != 0:
            print("set ExposureAuto mode fail! ret[0x%x]" % ret)
            sys.exit()
        else:
            print("set ExposureAuto mode off")

        # Set ExposureTime
        ret = self.cam.MV_CC_SetFloatValue("ExposureTime", self.ExposureTime)
        if ret != 0:
            print("set ExposureTime fail! ret[0x%x]" % ret)
            sys.exit()
        else:
            print("set ExposureTime ExposureTime",self.ExposureTime)

        # Set Gain
        ret = self.cam.MV_CC_SetFloatValue("Gain", self.Gain)
        if ret != 0:
            print("set Gain fail! ret[0x%x]" % ret)
            sys.exit()
        else:
            print("set Gain ExposureTime", self.Gain)
        # Start grabbing
        ret = self.cam.MV_CC_StartGrabbing()
        if ret != 0:
            print("start grabbing fail! ret[0x%x]" % ret)
            sys.exit()
        else:
            print("start grabbing ")

    def get_one_frame(self):
        stOutFrame = MV_FRAME_OUT()  # переменная выходного фрейм  тип данных
        memset(byref(stOutFrame), 0, sizeof(stOutFrame))  # заполняем всю структуру нулями
        ret = self.cam.MV_CC_GetImageBuffer(stOutFrame, 10000)  # читаем из буфера камеры
        img_buff = None
        if None != stOutFrame.pBufAddr and 0 == ret:
            print("MV_CC_GetImageBuffer: Width[%d], Height[%d], nFrameNum[%d]" % (stOutFrame.stFrameInfo.nWidth, stOutFrame.stFrameInfo.nHeight, stOutFrame.stFrameInfo.nFrameNum))
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
                print("convert pixel fail! ret[0x%x]" % ret)
                del stConvertParam.pSrcData
                sys.exit()
            img_buff = (c_ubyte * stConvertParam.nDstLen)()
            cdll.msvcrt.memcpy(byref(img_buff), stConvertParam.pDstBuffer, stConvertParam.nDstLen)  # копирование данных
            img_buff = np.frombuffer(img_buff, count=int(stConvertParam.nDstBufferSize),  # преобразование в np массив
                                     dtype=np.uint8)  # data以流的形式读入转化成ndarray对象
            img_buff = img_buff.reshape(stOutFrame.stFrameInfo.nHeight, stOutFrame.stFrameInfo.nWidth, 3)
            nRet = self.cam.MV_CC_FreeImageBuffer(stOutFrame)
            if ret != 0:
                print("MV_CC_FreeImageBuffer fail! ret[0x%x]" % ret)
                del stConvertParam.pSrcData
                sys.exit()
            return img_buff
        else:
            imageError = cv2.imread('no_cam_connect.jpg')
            print("no data[0x%x]" % ret)
            return imageError

    def close_grab_destroy_handle(self):
        ret = self.cam.MV_CC_CloseDevice()
        if ret != 0:
            print("close deivce fail! ret[0x%x]" % ret)
            sys.exit()
        else:
            print("deivce close")

        ret = self.cam.MV_CC_DestroyHandle()
        if ret != 0:
            print("destroy handle fail! ret[0x%x]" % ret)
            sys.exit()
        else:
            print("handle destroy")

class CnnYolo():
    def __init__(self):
        self.model = 0
        self.modelEnginePath ='EMG_2025_24_06_v1.engine'

    def create_model(self):
        self.model = YOLO(self.modelEnginePath)

    def object_detection(self,image):
        start_time = time.time()
        img_color_rbb = image
        heightImg, widthImg, channelsImg = img_color_rbb.shape
        bytes_per_lineImg = channelsImg * widthImg

        results = self.model(img_color_rbb)
        annotated_frame = results[0].plot()
        annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

        end_time = time.time()
        execution_time = end_time - start_time
        fps = 1 / execution_time
        cv2.putText(annotated_frame, f"FPS: {fps:.2f}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        q_image = QImage(annotated_frame.data, widthImg, heightImg, bytes_per_lineImg, QImage.Format_RGB888)
        q_pixmap = QPixmap.fromImage(q_image)
        q_pixmap2 = q_pixmap.copy()
        return q_pixmap2

    def check_envir(self):
        # Checking the environment
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print(f"Using device: {device}")
        print(f"PyTorch version: {torch.__version__}")
        print(f"CUDA available: {torch.cuda.is_available()}")
        print(f"CUDA version: {torch.version.cuda}")
        print(f"GPU device: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'None'}")
        print(f"Версия pymodbus: {pymodbus.__version__}")

class Logger:
    def __init__(self, name: str = __name__):
        self._setup_logging()
        self.logger = logging.getLogger(name)

    def _setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('app.log'),
                logging.StreamHandler()
            ]
        )

    def debug(self, message: str):
        self.logger.debug(message)

    def info(self, message: str):
        self.logger.info(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def error(self, message: str):
        self.logger.error(message)

    def critical(self, message: str):
        self.logger.critical(message)

def _modbus_connect():
    client_link = ModbusTcpClient(
        host='192.168.4.176',  # IP-адрес устройства
        port=502,  # Стандартный порт Modbus TCP
        timeout=3,  # Таймаут в секундах
        retries=3  # Количество попыток переподключения
    )
    return  client_link

def _modbus_read(client_link):
    if client_link.connect():
        print("Успешное подключение modbus")
    result = client_link.read_discrete_inputs(
        address=0,  # Начальный адрес
        count=8,  # Количество битов (8 bits)
        device_id=1  # ID устройства
    )

    if not result.isError():
        bits = result.bits[:8]
        print(f"Input bits: {bits}")
        print("Состояние input bits:")
        for i, bit in enumerate(bits):
            print(f"Bit {i}: {'ON' if bit else 'OFF'}")

def update_frame(hikcam_link,cnnyolo_link,lable_link):
    lable_frame = hikcam_link.get_one_frame()
    lable_detection = cnnyolo_link.object_detection(lable_frame)
    lable_link.setPixmap(lable_detection)


if __name__ == "__main__":

    #Qt app create
    app = QApplication(sys.argv)

    hikCamera1 = HikCam(10)
    hikCamera1.update_cam_list()

    cnn1 = CnnYolo()
    cnn1.check_envir()
    cnn1.create_model()

    window = QMainWindow()
    ui = Ui_MainWindow()  # Создаем экземпляр UI
    ui.setupUi(window)  # Настраиваем окно через UI

    window.setWindowTitle("Hikrobot Camera Viewer")
    window.minimumSize()
    window.show()

    timer = QTimer()
    timer.setInterval(10)

    ui.pushButtonDisconectCam.setEnabled(False)

    ui.pushButtonConnectCam.clicked.connect(lambda:hikCamera1.create_cam_handle_open_setting_start_grab())
    ui.pushButtonDisconectCam.clicked.connect(lambda: hikCamera1.close_grab_destroy_handle())

    ui.gain_doubleSpinBox.setRange(0.0,20.0)
    #ui.gain_doubleSpinBox.setValue(Gain)
    #ui.gain_doubleSpinBox.valueChanged.connect(_changeValueGain)

    ui.exposureTime_spinBox.setRange(0,20000)
    #ui.exposureTime_spinBox.setValue(ExposureTime)
    #ui.exposureTime_spinBox.valueChanged.connect(_changeValueExposureTime)

    ui.pushButtonStartObjDetectCnn.clicked.connect(lambda:timer.start())
    ui.pushButtonStopObjDetectCnn.clicked.connect(lambda:timer.stop())

    timer.timeout.connect(lambda: update_frame(hikCamera1, cnn1, ui.label))

    sys.exit(app.exec())