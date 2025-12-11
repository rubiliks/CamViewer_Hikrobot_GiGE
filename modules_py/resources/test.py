
import sys
import time
from PySide6.QtCore import QThread
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer, QThread
import time

def cyclt_frame():
    print("!!!!!!!!!!!!Cyclt Frame!!!!!!!!!!!!",time.time())

# В PySide6 обязательно нужно наследоваться от QThread для переопределения run()
class WorkerThread(QThread):
    def run(self):
        while True:
            print("!!!!!!!!!!!!Cyclt Valve!!!!!!!!!!!!")
            time.sleep(0.02)  # 20 мс

if __name__ == "__main__":
    app = QApplication(sys.argv)

    timerFrame = QTimer()
    timerFrame.setInterval(100)
    timerFrame.timeout.connect(cyclt_frame)
    timerFrame.start()

    # Создаем и запускаем наш поток
    thread = WorkerThread()
    thread.start()

    sys.exit(app.exec())