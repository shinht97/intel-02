import torch
import cv2

print("model load")
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt', verbose=False)
# model = torch.hub.load('/home/ubuntu/python_test/yolo/yolov5', 'yolov5s', verbose=False)

print("image load")
im2 = cv2.imread("1_dog.jpg")
results = model(im2)
results.save()
pred = results.pandas().xyxy[0]
predNP = pred.to_numpy()
nj, ni = predNP.shape