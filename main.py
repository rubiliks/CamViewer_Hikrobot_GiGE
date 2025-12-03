from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
from MvImport.MvCameraControl_class import *
from modules_py.mainWindowSmir_ui import Ui_MainWindow
from modules_py.hik_cam import  HikCam
from modules_py.cnn_yolo import  CnnYolo
from modules_py.settings import Setting
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

def cnn_status_button_ui(ui_link):
    if ui_link.pushButtonStopObjDetectCnn.isEnabled():
        ui_link.pushButtonStartObjDetectCnn.setEnabled(True)
        ui_link.pushButtonStopObjDetectCnn.setEnabled(False)
        ui_link.label.clear()
        ui_link.cnnStatusProgressBar.setValue(0)
        ui_link.Cnn_path_qlineEdit.setEnabled(True)
    else:
        ui_link.pushButtonStartObjDetectCnn.setEnabled(False)
        ui_link.pushButtonStopObjDetectCnn.setEnabled(True)
        ui_link.cnnStatusProgressBar.setValue(100)
        ui_link.Cnn_path_qlineEdit.setEnabled(False)

def cnn_apply_cnn_path (cnn_link,cnn_path):
    cnn_link.create_model(cnn_path)


def cam_status_block_serch_came(ui_link):
    if not ui_link.pushButtonConnectCam.isEnabled():
        ui_link.pushButtonConnectCam.setEnabled(True)
        ui_link.Cam_find_label.setText("Cam finded!")

def cam_status_not_find_came(ui_link):
    ui_link.pushButtonConnectCam.setEnabled(False)
    ui_link.Cam_find_label.setText("Cam not find")

def change_gain_setting(ui_link,setting_link):
    setting_link.write_setting_gain(ui_link.gain_doubleSpinBox.value())

def change_exposure_setting(ui_link,setting_link):
    setting_link.write_setting_exposure(ui_link.exposureTime_spinBox.value())


if __name__ == "__main__":
    logger.info("Start app")
    #Qt создание приложение
    app = QApplication(sys.argv)
    # Экземпляр сеттинга
    setting1 = Setting()
    setting1.set_setting_path('resources/settings.json')
    setting1.read_settings()
    #Экземпляр класса камеры
    hikCamera1 = HikCam()
    #Экземпляр класса нейроной сети
    cnn1 = CnnYolo()
    cnn1.check_envir()
    cnn1.create_model(setting1.cnnPath)

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
    ui.gain_doubleSpinBox.setValue(setting1.cameraSettingGain)
    ui.gain_doubleSpinBox.valueChanged.connect(hikCamera1.get_gain)
    ui.exposureTime_spinBox.setRange(0,20000)
    ui.exposureTime_spinBox.setValue(setting1.cameraSettingExposureTime)
    ui.exposureTime_spinBox.valueChanged.connect(hikCamera1.get_exposure)
    ui.gain_doubleSpinBox.valueChanged.connect(lambda:change_gain_setting(ui,setting1))
    ui.exposureTime_spinBox.valueChanged.connect(lambda: change_exposure_setting(ui, setting1))
    ui.pushButtonDisconectCam.setEnabled(False)
    ui.cameraStatusProgressBar.setValue(0)
    ui.cnnStatusProgressBar.setValue(0)
    ui.pushButtonStopObjDetectCnn.setEnabled(False)
    ui.lineEdit.setEnabled(False)

    # Соединение кнопок нейросети
    ui.pushButtonStartObjDetectCnn.clicked.connect(lambda:timer.start())
    ui.pushButtonStopObjDetectCnn.clicked.connect(lambda:timer.stop())
    ui.pushButtonStartObjDetectCnn.clicked.connect(lambda:cnn_status_button_ui(ui))
    ui.pushButtonStopObjDetectCnn.clicked.connect(lambda: cnn_status_button_ui(ui))
    ui.ApplyCNNpushButton.clicked.connect(lambda:cnn_apply_cnn_path(cnn1,setting1.cnnPath))

    # Соединение состояния камеры с блокировкой кнопок
    ui.pushButtonConnectCam.setEnabled(False)
    hikCamera1.cam_сon_discon_sig.connect(lambda:cam_status_block_button_ui(ui))
    hikCamera1.cam_finded_camera_sig.connect(lambda:cam_status_block_serch_came(ui))
    hikCamera1.cam_not_finded_sig.connect(lambda:cam_status_not_find_came(ui))
    ui.Cam_find_label.setText('No Camera Find')
    logger.info("App started")

    sys.exit(app.exec())
