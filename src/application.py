import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from src.ui.mainWindowSmir_ui import Ui_MainWindow


class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)

        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.setWindowTitle("Hikrobot Camera Viewer")
        self.window.minimumSize()
        self.window.show()

        self.ui.gain_doubleSpinBox.setRange(0.0, 20.0)
        self.ui.gain_doubleSpinBox.setValue(2.0)

        self.ui.exposureTime_spinBox.setRange(0, 20000)
        self.ui.exposureTime_spinBox.setValue(5000)

        self.ui.pushButtonDisconectCam.setEnabled(False)
        self.ui.cameraStatusProgressBar.setValue(0)

    def _update_frame(self, hikcam_link, cnnyolo_link, lable_link):
        lable_frame = hikcam_link.get_one_frame()
        lable_detection = cnnyolo_link.object_detection(
            lable_frame
        )  # сделать в отдельном воркере
        lable_link.setPixmap(lable_detection)

    def _cam_status_block_button_ui(self, ui_link):
        if ui_link.cameraStatusProgressBar.value() == 0:
            ui_link.cameraStatusProgressBar.setValue(100)
        else:
            ui_link.cameraStatusProgressBar.setValue(0)

        if ui_link.pushButtonDisconectCam.isEnabled():
            ui_link.pushButtonDisconectCam.setEnabled(False)
        else:
            ui_link.pushButtonDisconectCam.setEnabled(True)

        if ui_link.pushButtonConnectCam.isEnabled():
            ui_link.pushButtonConnectCam.setEnabled(False)
        else:
            ui_link.pushButtonConnectCam.setEnabled(True)

        if ui_link.gain_doubleSpinBox.isEnabled():
            ui_link.gain_doubleSpinBox.setEnabled(False)
        else:
            ui_link.gain_doubleSpinBox.setEnabled(True)

        if ui_link.exposureTime_spinBox.isEnabled():
            ui_link.exposureTime_spinBox.setEnabled(False)
        else:
            ui_link.exposureTime_spinBox.setEnabled(True)

    def exec(self):
        return (
            self.app.exec()
        )  # похоже на костыль но что то в голову не пришло как по другому )
