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
        self.modelEnginePath =''
        self.obj_list =[]

    def create_model(self,modelPath):
        if (len(modelPath) != 0 ):
            try:
                self.modelEnginePath = modelPath
                self.model = YOLO(self.modelEnginePath)
                logger.info("CNN created")
            except ValueError:
                logger.error(f"CNN create error {ValueError}")
        else:
            logger.error("CNN modelPath empty path")

    def object_detection(self,image):
        if(image.size>0 and (image  is not  None)):
            logger.info("objec_detection image ok")
            start_time = time.time()
            self.obj_list.clear()
            img_color_rbb = image
            heightImg, widthImg, channelsImg = img_color_rbb.shape
            bytes_per_lineImg = channelsImg * widthImg
            results = self.model(img_color_rbb, verbose = False)
            annotated_frame = results[0].plot()
            annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
            counter_obj = 0
            for result in results:
                boxes = result.boxes
                # Извлечение координат, confidence scores и классов
                for box in boxes:
                    obj_data = {}
                    obj_data.clear()
                    x1, y1, x2, y2 = box.xyxy[0].tolist()
                    x_center, y_center, width, height = box.xywh[0].tolist()
                    confidence = box.conf[0].item()
                    class_id = box.cls[0].item()
                    class_name = self.model.names[class_id]
                    # Данные объекта
                    obj_data = {
                        "frame_width": widthImg,
                        "frame_height": heightImg,
                        "x_center": x_center,
                        "y_center": y_center,
                        "width": width,
                        "height": height,
                        "confidence": confidence,
                        "class_id": class_id,
                        "class_name": class_name,
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
            resized = cv2.resize(annotated_frame, (1545, 386))
            #q_image = QImage(annotated_frame.data, widthImg, heightImg, bytes_per_lineImg, QImage.Format_RGB888)
            heightImgDispla, widthImgDispla, channelsImgDispla = resized.shape
            bytes_per_lineImgDispla = channelsImgDispla * widthImgDispla

            q_image = QImage(resized.data, widthImgDispla, heightImgDispla, bytes_per_lineImgDispla, QImage.Format_RGB888)
            q_pixmap = QPixmap.fromImage(q_image)
            q_pixmap2 = q_pixmap.copy()
            return q_pixmap2, self.obj_list
        else:
            logger.error("no image")
            return None,None

    def check_envir(self):
        # Checking the environment
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        logger.info(f"Using device: {device}")
        logger.info(f"PyTorch version: {torch.__version__}")
        logger.info(f"CUDA available: {torch.cuda.is_available()}")
        logger.info(f"CUDA version: {torch.version.cuda}")
        logger.info(f"GPU device: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'None'}")


