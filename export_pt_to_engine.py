from ultralytics import YOLO
import torch

print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"CUDA version: {torch.version.cuda}")

model= YOLO('EMG_2025_24_06_v1.pt')
model.export(format="engine",imgsz =1440,half=True)
