import cv2
import time
import logging
import torch

from PySide6.QtGui import QPixmap, QImage
from ultralytics import YOLO
from datetime import datetime

logger = logging.getLogger(__name__)
class CnnYolo():
    def __init__(self):
        self.model = 0
        self.modelEnginePath ='./resurse/EMG_2025_24_06_v1.engine'
        self.obj_list =[]

    def create_model(self):
        self.model = YOLO(self.modelEnginePath)

    def object_detection(self,image):
        logger.error("object_detection")
        start_time = time.time()
        self.obj_list.clear()
        img_color_rbb = image
        heightImg, widthImg, channelsImg = img_color_rbb.shape
        bytes_per_lineImg = channelsImg * widthImg

        results = self.model(img_color_rbb)
        annotated_frame = results[0].plot()
        annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
        counter_obj = 0
        for result in results:
            boxes = result.boxes  # Boxes object
            # Извлечение координат, confidence scores и классов
            for box in boxes:
                obj_data = {}
                # Координаты в формате [x1, y1, x2, y2]
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                # Координаты в формате [x_center, y_center, width, height] (нормализованные)
                x_center, y_center, width, height = box.xywh[0].tolist()
                # Confidence score
                confidence = box.conf[0].item()
                # Класс объекта
                class_id = box.cls[0].item()
                class_name = self.model.names[class_id]
                # Данные объекта
                obj_data = {
                    "x_center": x_center,
                    "y_center": y_center,
                    "width": width,
                    "height": height,
                    "confidence": confidence,
                    "class_id": class_id,
                    "class_name": class_name,
                    "counter_obj":counter_obj,
                    "timestamp": datetime.now().isoformat()
                }
                self.obj_list.append(obj_data)

                x_center_circle = int(x_center)
                y_center_circle = int(y_center)
                counter_obj = counter_obj + 1

                cv2.circle(annotated_frame,(x_center_circle,y_center_circle),5,(0, 255, 0), 2)
                cv2.putText(annotated_frame, str(counter_obj), (x_center_circle, y_center_circle-15), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        end_time = time.time()
        execution_time = end_time - start_time
        fps = 1 / execution_time
        cv2.putText(annotated_frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        q_image = QImage(annotated_frame.data, widthImg, heightImg, bytes_per_lineImg, QImage.Format_RGB888)
        q_pixmap = QPixmap.fromImage(q_image)
        q_pixmap2 = q_pixmap.copy()
        return q_pixmap2, self.obj_list

    def check_envir(self):
        # Checking the environment
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print(f"Using device: {device}")
        print(f"PyTorch version: {torch.__version__}")
        print(f"CUDA available: {torch.cuda.is_available()}")
        print(f"CUDA version: {torch.version.cuda}")
        print(f"GPU device: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'None'}")

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