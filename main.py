import cv2
import numpy as np


widthImg=540
heightImg =640

######Capturing and showing a video#######
cap = cv2.VideoCapture(0)
cap.set(3,widthImg)
cap.set(4,heightImg)
cap.set(10,150)

def preprocessing(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,200,200)
    kernel = np.ones((5,5))
    imgDial = cv2.dilate(imgCanny,kernel,iterations=2)
    imgThres = cv2.erode(imgDial,kernel,iterations=1)
    return imgThres





while True:
    success, img = cap.read()
    img = cv2.resize(img,(widthImg,heightImg))
    imgThres = preprocessing(img)
    cv2.imshow("Video",imgThres)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
