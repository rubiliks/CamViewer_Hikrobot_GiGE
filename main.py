import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow

from src.application import Application
from src.cnn_yolo import CnnYolo
from src.hik_cam import HikCam

if __name__ == "__main__":

    app = Application()

    # Экземпляр класса камеры
    hikCamera1 = HikCam()
    hikCamera1.update_cam_list()

    # Экземпляр класса нейроной сети
    cnn1 = CnnYolo()
    cnn1.check_envir()
    cnn1.create_model()

    # экземпляр таймера для получения кадра с камеры
    timer = QTimer()
    timer.setInterval(30)
    timer.timeout.connect(lambda: app._update_frame(hikCamera1, cnn1, app.ui.label))

    # Cоеднение ui кнопок камеры
    app.ui.pushButtonConnectCam.clicked.connect(
        lambda: hikCamera1.create_cam_handle_open_setting_start_grab()
    )
    app.ui.pushButtonDisconectCam.clicked.connect(
        lambda: hikCamera1.close_grab_destroy_handle()
    )
    # Cоеднение ui настроек камеры
    app.ui.gain_doubleSpinBox.valueChanged.connect(hikCamera1.get_gain)
    app.ui.exposureTime_spinBox.valueChanged.connect(hikCamera1.get_exposure)

    # Соединение кнопок нейросети
    app.ui.pushButtonStartObjDetectCnn.clicked.connect(lambda: timer.start())
    app.ui.pushButtonStopObjDetectCnn.clicked.connect(lambda: timer.stop())

    # Соединение состояния камеры с блокировкой кнопок
    hikCamera1.cam_сon_discon_sig.connect(
        lambda: app._cam_status_block_button_ui(app.ui)
    )

    sys.exit(app.exec())
