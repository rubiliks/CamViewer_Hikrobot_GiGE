from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer

from MvImport.MvCameraControl_class import *
from modules_py.mainWindowSmir import Ui_MainWindow
from modules_py.HikCam import  HikCam
from modules_py.CnnYolo import  CnnYolo

import logging

logging.basicConfig(filename='CamViewer_Hikrobot_GiGE.log', level=logging.DEBUG,format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def update_frame(hikcam_link,cnnyolo_link,lable_link):
    lable_frame = hikcam_link.get_one_frame()
    lable_detection,objs_cnn_data = cnnyolo_link.object_detection(lable_frame)
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

    if ui_link.searchCam.isEnabled():
        ui_link.searchCam.setEnabled(False)
    else:
        ui_link.searchCam.setEnabled(True)


def cam_status_block_serch_came(ui_link):
    if not ui_link.pushButtonConnectCam.isEnabled():
        ui_link.pushButtonConnectCam.setEnabled(True)
        ui_link.Cam_find_label.setText("Cam finded!")


if __name__ == "__main__":
    logger.info("Start app")
    #Qt создание приложение
    app = QApplication(sys.argv)
    #Экземпляр класса камеры
    hikCamera1 = HikCam()
    #hikCamera1.update_cam_list()
    #Экземпляр класса нейроной сети
    cnn1 = CnnYolo()
    cnn1.check_envir()
    cnn1.create_model('./resurse/EMG_2025_24_06_v1.engine')
    #Экземпляр ui
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.setWindowTitle("Hikrobot Camera Viewer")
    window.minimumSize()
    window.show()
    #Экземпляр таймера для получения кадра с камеры
    timer = QTimer()
    timer.setInterval(30)
    timer.timeout.connect(lambda: update_frame(hikCamera1, cnn1, ui.label))
    #Cоеднение ui кнопок камеры
    ui.searchCam.clicked.connect(lambda:hikCamera1.update_cam_list())
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
    ui.pushButtonConnectCam.setEnabled(False)
    hikCamera1.cam_сon_discon_sig.connect(lambda:cam_status_block_button_ui(ui))
    hikCamera1.cam_finded_camera_sig.connect(lambda:cam_status_block_serch_came(ui))
    ui.Cam_find_label.setText('No Camera Find')
    logger.info("App started")

    sys.exit(app.exec())
