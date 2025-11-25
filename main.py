
import cv2
import time
import logging

from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QMainWindow, QPushButton
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import QTimer
from MvCameraControl_class import *
import pymodbus
from pymodbus.client import ModbusTcpClient
import torch
from ultralytics import YOLO

from mainWindowSmir import Ui_MainWindow
from HikCam import  HikCam


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

def cam_status_block_button_ui(ui_link):
    if ui_link.cameraStatusProgressBar.value() == 0:
        ui_link.cameraStatusProgressBar.setValue(100)
    else:
        ui_link.cameraStatusProgressBar.setValue(0)

    if ui_link.pushButtonDisconectCam.isEnabled():
        ui_link.pushButtonDisconectCam.setEnabled(False)
    else:ui_link.pushButtonDisconectCam.setEnabled(True)

    if ui_link.pushButtonConnectCam.isEnabled():
        ui_link.pushButtonConnectCam.setEnabled(False)
    else:ui_link.pushButtonConnectCam.setEnabled(True)

    if ui_link.gain_doubleSpinBox.isEnabled():
        ui_link.gain_doubleSpinBox.setEnabled(False)
    else:
        ui_link.gain_doubleSpinBox.setEnabled(True)

    if ui_link.exposureTime_spinBox.isEnabled():
        ui_link.exposureTime_spinBox.setEnabled(False)
    else:
        ui_link.exposureTime_spinBox.setEnabled(True)


if __name__ == "__main__":

    #Qt создание приложение
    app = QApplication(sys.argv)
    #Экземпляр класса камеры
    hikCamera1 = HikCam()
    hikCamera1.update_cam_list()
    #Экземпляр класса нейроной сети
    cnn1 = CnnYolo()
    cnn1.check_envir()
    cnn1.create_model()
    #Экземпляр ui
    window = QMainWindow()
    ui = Ui_MainWindow()  #
    ui.setupUi(window)
    window.setWindowTitle("Hikrobot Camera Viewer")
    window.minimumSize()
    window.show()
    #экземпляр таймера для получения кадра с камеры
    timer = QTimer()
    timer.setInterval(10)
    timer.timeout.connect(lambda: update_frame(hikCamera1, cnn1, ui.label))
    #Cоеднение ui кнопок камеры
    ui.pushButtonConnectCam.clicked.connect(lambda:hikCamera1.create_cam_handle_open_setting_start_grab())
    ui.pushButtonDisconectCam.clicked.connect(lambda: hikCamera1.close_grab_destroy_handle())
    # Cоеднение ui настроек камеры
    ui.gain_doubleSpinBox.setRange(0.0,20.0)
    ui.gain_doubleSpinBox.setValue(2.0)
    ui.gain_doubleSpinBox.valueChanged.connect(hikCamera1.get_gain)
    ui.exposureTime_spinBox.setRange(0,20000)
    ui.exposureTime_spinBox.setValue(5000)
    ui.exposureTime_spinBox.valueChanged.connect(hikCamera1.get_exposure)
    ui.pushButtonDisconectCam.setEnabled(False)
    ui.cameraStatusProgressBar.setValue(0)
    # Соединение кнопок нейросети
    ui.pushButtonStartObjDetectCnn.clicked.connect(lambda:timer.start())
    ui.pushButtonStopObjDetectCnn.clicked.connect(lambda:timer.stop())
    # Соединение состояния камеры с блокировкой кнопок
    hikCamera1.cam_сon_discon_sig.connect(lambda:cam_status_block_button_ui(ui))

    sys.exit(app.exec())