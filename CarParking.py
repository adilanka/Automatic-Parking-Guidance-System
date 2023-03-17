import cv2
import pickle

width, height = 27, 65
try:
    with open('ParkingSpotPOS','rb') as f:
        posList = pickle.load(f)
except:
    posList = []

def mouseClick(events, x, y, flags, params):
     if events == cv2.EVENT_LBUTTONDOWN:
         posList.append((x,y))
     if events == cv2.EVENT_RBUTTONDOWN:
         for i, pos in enumerate(posList):
             x1, y1 = pos
             if x1<x<x1+width and y1<y<y1+height:
                 posList.pop(i)

     with open('ParkingSpotPOS','wb') as f:
        pickle.dump(posList, f)

while True:
    img = cv2.imread('PV1_image.jpg')
    #for pos in posList:
     #   cv2.rectangle(img, pos, (pos[0]+width, pos[1]+height), (0, 255, 0), 2)
    #cv2.rectangle(img,(480,480),(545,350),(0,255,0),2)
    #cv2.rectangle(img, (108, 205), (135, 265), (0, 255, 0), 2)
    for pos in posList:
       cv2.rectangle(img, pos, (pos[0]+width, pos[1]+height),(0, 255, 0), 2)
    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)
    cv2.waitKey(10)