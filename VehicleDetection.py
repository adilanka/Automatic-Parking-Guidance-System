import cv2
import pickle
import numpy as np
import cvzone

#Reading the video using OpenCV
cap = cv2.VideoCapture(r'C:\Users\Aditya Lanka\PycharmProjects\ParkingSpaceDetector\PV1.mp4')
#Loading the pickle file made in the CarParking.py
with open('ParkingSpotPOS', 'rb') as f:
    posList = pickle.load(f)

width, height = 27, 65

def checkParkingSpace(imgProcessed):
    SpaceCounter = 0
    for pos in posList:
        x, y = pos

        imgCrop = imgProcessed[y:y + height, x:x + width]
        #cv2.imshow(str(x),imgCrop)
        count = cv2.countNonZero(imgCrop)


        if count<250:
            color = (0,255,0)
            thickness = 2
            SpaceCounter+=1
        else:
            color = (0,0,255)
            thickness = 1
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
        cvzone.putTextRect(img, str(count), (x, y + height), scale=0.8, thickness=1, offset=0, colorR=color)

    cvzone.putTextRect(img, f'Free Parking Spaces: -{SpaceCounter}/{len(posList)}', (180,175), scale=1, thickness=1, offset=0, colorR=(0, 0, 0))


while True:
    if(cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT)):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)

    success, img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(3,3),1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold,5)
    kernel = np.ones((3,3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)
    checkParkingSpace(imgDilate)
    cv2.imshow("Image", img)
    cv2.imshow("ImageBlur",imgBlur)
    cv2.imshow("ImageThreshold",imgThreshold)
    cv2.waitKey(1)
