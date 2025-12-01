# здесь нужно перенести код детекции из cnn_yolo.py и создать отдельный воркер для инференса
# как пример ниже
from PySide6.QtCore import QThread


class AcquisitionWorker(QThread):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._is_running = True

    def run(self):
        while self._is_running:
            pass

    def stop(self):
        self._is_running = False
        self.wait()
