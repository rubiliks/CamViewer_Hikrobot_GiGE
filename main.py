import cv2
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer, Signal, Slot
from PySide6.QtCore import QThread
from polars import self_dtype

from MvImport.MvCameraControl_class import *
from modules_py.mainWindowSmir_ui import Ui_MainWindow
from modules_py.hik_cam import  HikCam
from modules_py.cnn_yolo import  CnnYolo
from modules_py.settings import Setting
import logging
import time

from pymodbus.client import ModbusTcpClient


logging.basicConfig(filename='CamViewer_Hikrobot_GiGE.log', level=logging.DEBUG,format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# В PySide6 обязательно нужно наследоваться от QThread для переопределения run()
class WorkerThread(QThread):
    receive_list_signal = Signal(list)
    def __init__(self):
        super().__init__()
        self.test = False
        self.data_list_recive = []
        self.data_list = []
        self.bool_list = [False] * 80
        self.receive_list_signal.connect(self.process_list)

    def run(self):
        self.test = True
        client = ModbusTcpClient(
            host='192.168.88.150',  # IP-адрес устройства
            port=502,  # Стандартный порт Modbus TCP
            timeout=3,  # Таймаут в секундах
            retries=3  # Количество попыток переподключения
        )
        print('client',client)

        while self.test:
            print(f'data {self.data_list}  \n')
            for objsInframe in self.data_list:
                # print(f'frame {counter} {objsInframe} \n')
                for obj in objsInframe:
                    #print(f'obj {obj} \n')
                    obj["valveTime"] = obj["valveTime"] - 0.02
                    if obj["valveTime"] < 0.0 and obj["valveTime"] > -0.3:
                        obj["valveOpen"] = True
                    if obj["valveTime"] < - 0.3:
                        obj["valveOpen"] = False

            self.bool_list = [False] * 80

            #free valve false in obj
            for objsInframe in self.data_list:
                objCounter = 0
                for obj in objsInframe:
                    if "valveOpen" in obj:
                        if obj["valveOpen"] == True:
                            self.bool_list[obj["selectValve"]] = True
                        else:
                            self.bool_list[obj["selectValve"]] = False
                            objsInframe.pop(objCounter)
                        objCounter = objCounter + 1
            #free frame
            frameCounter = 0
            for objsInframe in self.data_list:
                if objsInframe == []:
                    self.data_list.pop(frameCounter)
            frameCounter = frameCounter + 1

            resule_write_coils = client.write_coils(4096, self.bool_list)
            time.sleep(0.02)  # 20 мс

    def stop(self):
        self.test = False

    def process_list(self, data):
        self.data_list_recive = data.copy()
        datacopy = self.data_list.copy()
        datacopy.append(self.data_list_recive)
        self.data_list = datacopy.copy()

def stop_and_close_thred():
    thread.stop()
    thread.wait()
    thread.deleteLater()
    print('Closing Thread')


def time_valve(hikcam_link1,objs_cnn_data1):
    #print(hikcam_link1.ResultingFrame)
    #print(hikcam_link1.ResultingLineRate)
    secInLine = ((1 / hikcam_link1.ResultingFrame) / hikcam_link1.Height)
    #print(secInLine)
    counterInt = 0
    valvesNumber = 79
    lengthToValvesBlock = 0.8 # metric
    ConveyorSpeed = 2.0 # m/s
    #valveBlockWidth = 2.0 # m
    valvesStep =  valvesNumber/hikcam_link1.Width
    #print(valvesStep)
    timeToOpen = lengthToValvesBlock/ConveyorSpeed
    objByTike = []
    objByTike.clear()
    for obj in objs_cnn_data1:
        #print(counterInt)
        counterInt = counterInt + 1
        #print(obj['timestamp'])
        #print('y_center',obj['y_center'])
        #print('x_center',obj['x_center'])
        deltaTime = obj['y_center'] * secInLine
        #print('delta time', deltaTime)
        valveTime = timeToOpen - deltaTime
        #print('valve time',valveTime)
        selectValve = obj['x_center'] * valvesStep
        selectValveRound =  round(selectValve)
        obj_data = {
            "valveTime": valveTime,
            "selectValve":selectValveRound
        }
        objByTike.append(obj_data)

    #print(objByTike)
    #print('end')
    return objByTike

def update_frame(hikcam_link,cnnyolo_link,lable_link):
    lable_frame = hikcam_link.get_one_frame()
    lable_detection,objs_cnn_data = cnnyolo_link.object_detection(lable_frame)
    lable_link.setPixmap(lable_detection)
    objByTikeFrame = []
    objByTikeFrame.clear()
    objByTikeFrame = time_valve(hikcam_link,objs_cnn_data).copy()
    if len(objByTikeFrame) > 0:
        thread.receive_list_signal.emit(objByTikeFrame.copy())
        print('objValveArray',objByTikeFrame)
        #print('sizeOfobjValveArray',len(objByTikeFrame_link))
    #print('frame',hikcam_link.ResultingFrame)


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

    if ui_link.gainDoubleSpinBox.isEnabled():
        ui_link.gainDoubleSpinBox.setEnabled(False)
    else:
        ui_link.gainDoubleSpinBox.setEnabled(True)

    if ui_link.exposureTime_spinBox.isEnabled():
        ui_link.exposureTime_spinBox.setEnabled(False)
    else:
        ui_link.exposureTime_spinBox.setEnabled(True)

    if ui_link.pushButtonsearchCam.isEnabled():
        ui_link.pushButtonsearchCam.setEnabled(False)
    else:
        ui_link.pushButtonsearchCam.setEnabled(True)

    if ui_link.BalanceBuespinBox.isEnabled():
        ui_link.BalanceBuespinBox.setEnabled(False)
    else:
        ui_link.BalanceBuespinBox.setEnabled(True)

    if ui_link.BalanceRedSpinBox.isEnabled():
        ui_link.BalanceRedSpinBox.setEnabled(False)
    else:
        ui_link.BalanceRedSpinBox.setEnabled(True)

    if ui_link.BalanceGreenspinBox.isEnabled():
        ui_link.BalanceGreenspinBox.setEnabled(False)
    else:
        ui_link.BalanceGreenspinBox.setEnabled(True)

    if ui_link.OffsetXspinBox.isEnabled():
        ui_link.OffsetXspinBox.setEnabled(False)
    else:
        ui_link.OffsetXspinBox.setEnabled(True)

    if ui_link.HeightspinBox.isEnabled():
        ui_link.HeightspinBox.setEnabled(False)
    else:
        ui_link.HeightspinBox.setEnabled(True)

    if ui_link.WidthspinBox.isEnabled():
        ui_link.WidthspinBox.setEnabled(False)
    else:
        ui_link.WidthspinBox.setEnabled(True)

def cnn_status_button_ui(ui_link):
    if ui_link.pushButtonStopObjDetectCnn.isEnabled():
        ui_link.pushButtonStartObjDetectCnn.setEnabled(True)
        ui_link.pushButtonStopObjDetectCnn.setEnabled(False)
        ui_link.CameraLabel.clear()
        ui_link.cnnStatusProgressBar.setValue(0)
        ui_link.cnnPathQlineEdit.setEnabled(True)
        #ui_link.ApplyCNNpushButton.setEnabled(True)
    else:
        ui_link.pushButtonStartObjDetectCnn.setEnabled(False)
        ui_link.pushButtonStopObjDetectCnn.setEnabled(True)
        ui_link.cnnStatusProgressBar.setValue(100)
        ui_link.cnnPathQlineEdit.setEnabled(False)
        #ui_link.ApplyCNNpushButton.setEnabled(False)

def cnn_apply_cnn_path (cnn_link,cnn_path):
    cnn_link.create_model(cnn_path)

def cam_status_block_serch_came(ui_link):
    if not ui_link.pushButtonConnectCam.isEnabled():
        ui_link.pushButtonConnectCam.setEnabled(True)
        ui_link.camFindLabel.setText("Cam finded!")

def cam_status_not_find_came(ui_link):
    ui_link.pushButtonConnectCam.setEnabled(False)
    ui_link.camFindLabel.setText("Cam not find")

def change_gain_setting(ui_link,setting_link):
    setting_link.write_setting_gain(ui_link.gainDoubleSpinBox.value())

def change_exposure_setting(ui_link,setting_link):
    setting_link.write_setting_exposure(ui_link.exposureTime_spinBox.value())

def change_BalanceRed_setting(ui_link,setting_link):
    setting_link.write_setting_BalanceRed(ui_link.BalanceRedSpinBox.value())

def change_BalanceGreen_setting(ui_link,setting_link):
    setting_link.write_setting_BalanceGreen(ui_link.BalanceGreenspinBox.value())

def change_BalanceBlue_setting(ui_link,setting_link):
    setting_link.write_setting_BalanceBlue(ui_link.BalanceBuespinBox.value())

def change_Width_setting(ui_link,setting_link):
    setting_link.write_setting_Width(ui_link.WidthspinBox.value())

def change_Height_setting(ui_link,setting_link):
    setting_link.write_setting_Height(ui_link.HeightSpinBox.value())

def change_OffsetX_setting(ui_link,setting_link):
    setting_link.write_setting_OffsetX(ui_link.HeightSpinBox.value())

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
    window.resize(4000,4000)
    window.show()

    #Экземпляр таймера для получения кадра с камеры
    timer = QTimer()
    timer.setInterval(100)
    timer.timeout.connect(lambda: update_frame(hikCamera1, cnn1, ui.CameraLabel))

    #Thread valve
    thread = WorkerThread()


    #Cоеднение ui кнопок камеры
    ui.pushButtonsearchCam.clicked.connect(lambda:hikCamera1.update_cam_list())
    ui.pushButtonConnectCam.clicked.connect(lambda:hikCamera1.create_cam_handle_open_setting_start_grab())
    ui.pushButtonDisconectCam.clicked.connect(lambda: hikCamera1.close_grab_destroy_handle())

    # Cоеднение ui настроек камеры
    # Gain
    ui.gainDoubleSpinBox.setRange(0.0,23.98)
    ui.gainDoubleSpinBox.setValue(setting1.cameraSettingGain)
    hikCamera1.set_gain(setting1.cameraSettingGain)
    ui.gainDoubleSpinBox.valueChanged.connect(hikCamera1.set_gain)
    ui.gainDoubleSpinBox.valueChanged.connect(lambda: change_gain_setting(ui, setting1))
    # Expusure
    ui.exposureTime_spinBox.setRange(0,20000)
    ui.exposureTime_spinBox.setValue(setting1.cameraSettingExposureTime)
    hikCamera1.set_exposure(setting1.cameraSettingExposureTime)
    ui.exposureTime_spinBox.valueChanged.connect(hikCamera1.set_exposure)
    ui.exposureTime_spinBox.valueChanged.connect(lambda: change_exposure_setting(ui, setting1))
    # Balance Red
    ui.BalanceRedSpinBox.setRange(0,3000)
    ui.BalanceRedSpinBox.setValue(setting1.cameraSettingBalanceRed)
    hikCamera1.set_BalanceRed(setting1.cameraSettingBalanceRed)
    ui.BalanceRedSpinBox.valueChanged.connect(hikCamera1.set_BalanceRed)
    ui.BalanceRedSpinBox.valueChanged.connect(lambda:change_BalanceRed_setting(ui, setting1))
    # Balance Green
    ui.BalanceGreenspinBox.setRange(0,3000)
    ui.BalanceGreenspinBox.setValue(setting1.cameraSettingBalanceGreen)
    hikCamera1.set_BalanceGreen(setting1.cameraSettingBalanceGreen)
    ui.BalanceGreenspinBox.valueChanged.connect(hikCamera1.set_BalanceGreen)
    ui.BalanceGreenspinBox.valueChanged.connect(lambda:change_BalanceGreen_setting(ui, setting1))
    # Balance Blue
    ui.BalanceBuespinBox.setRange(0,3000)
    ui.BalanceBuespinBox.setValue(setting1.cameraSettingBalanceBlue)
    hikCamera1.set_BalanceBlue(setting1.cameraSettingBalanceBlue)
    ui.BalanceBuespinBox.valueChanged.connect(hikCamera1.set_BalanceBlue)
    ui.BalanceBuespinBox.valueChanged.connect(lambda:change_BalanceBlue_setting(ui, setting1))
    # Width
    ui.WidthspinBox.setRange(128,4096)
    ui.WidthspinBox.setValue(setting1.cameraSettingWidth)
    hikCamera1.set_Width(setting1.cameraSettingWidth)
    ui.WidthspinBox.valueChanged.connect(hikCamera1.set_Width)
    ui.WidthspinBox.valueChanged.connect(lambda:change_Width_setting(ui, setting1))
    #Height
    ui.HeightspinBox.setRange(2,2000)
    ui.HeightspinBox.setValue(setting1.cameraSettingHeight)
    hikCamera1.set_Height(setting1.cameraSettingHeight)
    ui.HeightspinBox.valueChanged.connect(hikCamera1.set_Height)
    ui.HeightspinBox.valueChanged.connect(lambda:change_Height_setting(ui, setting1))
    #OffsetX
    ui.OffsetXspinBox.setRange(0,4096)
    ui.OffsetXspinBox.setValue(setting1.cameraSettingOffsetX)
    hikCamera1.set_OffsetX(setting1.cameraSettingOffsetX)
    ui.OffsetXspinBox.valueChanged.connect(hikCamera1.set_OffsetX)
    ui.OffsetXspinBox.valueChanged.connect(lambda:change_OffsetX_setting(ui, setting1))

    ui.pushButtonDisconectCam.setEnabled(False)
    ui.cameraStatusProgressBar.setValue(0)
    ui.cnnStatusProgressBar.setValue(0)
    ui.pushButtonStopObjDetectCnn.setEnabled(False)
    ui.settingPathlineEdit.setEnabled(False)

    # Соединение кнопок нейросети
    ui.pushButtonStartObjDetectCnn.clicked.connect(lambda:timer.start())
    ui.pushButtonStopObjDetectCnn.clicked.connect(lambda:timer.stop())

    ui.pushButtonStartObjDetectCnn.clicked.connect(lambda:thread.start())
    ui.pushButtonStopObjDetectCnn.clicked.connect(lambda:thread.stop())

    ui.pushButtonStartObjDetectCnn.clicked.connect(lambda:cnn_status_button_ui(ui))
    ui.pushButtonStopObjDetectCnn.clicked.connect(lambda: cnn_status_button_ui(ui))
    #ui.ApplyCNNpushButton.clicked.connect(lambda:cnn_apply_cnn_path(cnn1,setting1.cnnPath))

    # Соединение состояния камеры с блокировкой кнопок
    ui.pushButtonConnectCam.setEnabled(False)
    hikCamera1.cam_сon_discon_sig.connect(lambda:cam_status_block_button_ui(ui))
    hikCamera1.cam_finded_camera_sig.connect(lambda:cam_status_block_serch_came(ui))
    hikCamera1.cam_not_finded_sig.connect(lambda:cam_status_not_find_came(ui))
    ui.camFindLabel.setText('No Camera Find')
    ui.tabWidget.setCurrentWidget(ui.mainTab)
    logger.info("App started")

    app.aboutToQuit.connect(stop_and_close_thred)

    sys.exit(app.exec())
