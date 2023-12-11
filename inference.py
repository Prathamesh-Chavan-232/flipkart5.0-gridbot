from ultralytics import YOLO
# from ultralytics.utils.plotting import Annotator
import cv2 as cv 

model = YOLO('./runs/detect/train10/weights/best.pt')

img = cv.imread('./cardboard.jpg')

results=model(img)

for r in results:
    for box in r.boxes:
        # print(int(box.xyxy[0][0].item()))
        xy1=(int(box.xyxy[0][0].item()),int(box.xyxy[0][1].item()))
        xy2=(int(box.xyxy[0][2].item()),int(box.xyxy[0][3].item())) 
        
        cv.rectangle( img, xy1 , xy2 , (255,0,0), 2)
        
cv.imshow('result',img)
cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(0)
cv.destroyAllWindows()