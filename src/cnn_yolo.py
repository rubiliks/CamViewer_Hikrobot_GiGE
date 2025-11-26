import time

import cv2
import torch
from PySide6.QtGui import QImage, QPixmap
from ultralytics import YOLO


class CnnYolo:
    def __init__(self):
        self.model = 0
        self.modelEnginePath = "./resources/EMG_2025_24_06_v1.engine"

    def create_model(self):
        self.model = YOLO(self.modelEnginePath)

    def object_detection(self, image):
        start_time = time.time()
        img_color_rbb = image
        heightImg, widthImg, channelsImg = img_color_rbb.shape
        bytes_per_lineImg = channelsImg * widthImg

        results = self.model(img_color_rbb)
        annotated_frame = results[0].plot()
        annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

        for result in results:
            boxes = result.boxes  # Boxes object

            # Извлечение координат, confidence scores и классов
            for box in boxes:
                # Координаты в формате [x1, y1, x2, y2]
                x1, y1, x2, y2 = box.xyxy[0].tolist()

                # Координаты в формате [x_center, y_center, width, height] (нормализованные)
                x_center, y_center, width, height = box.xywh[0].tolist()

                # Confidence score
                confidence = box.conf[0].item()

                # Класс объекта
                class_id = box.cls[0].item()
                class_name = self.model.names[class_id]

                print(f"Объект: {class_name}")
                print(f"Координаты: [{x1:.2f}, {y1:.2f}, {x2:.2f}, {y2:.2f}]")
                print(f"Confidence: {confidence:.2f}")

        end_time = time.time()
        execution_time = end_time - start_time
        fps = 1 / execution_time
        cv2.putText(
            annotated_frame,
            f"FPS: {fps:.2f}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )

        q_image = QImage(
            annotated_frame.data,
            widthImg,
            heightImg,
            bytes_per_lineImg,
            QImage.Format_RGB888,
        )
        q_pixmap = QPixmap.fromImage(q_image)
        q_pixmap2 = q_pixmap.copy()
        return q_pixmap2

    def check_envir(self):
        # Checking the environment
        device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using device: {device}")
        print(f"PyTorch version: {torch.__version__}")
        print(f"CUDA available: {torch.cuda.is_available()}")
        print(f"CUDA version: {torch.version.cuda}")
        print(
            f"GPU device: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'None'}"
        )
