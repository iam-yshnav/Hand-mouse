import pyautogui
from cvzone.HandTrackingModule import HandDetector
import cv2
import math


cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)
    cv2.rectangle(img, (80, 105), (580, 375), (0, 255, 0), 3)


    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        bbox1 = hand1["bbox"]
        centerPoint1 = hand1['center']
        handType1 = hand1["type"]
        fingers1 = detector.fingersUp(hand1)

        cx1 = lmList1[8][0]   #first finger point
        cy1 = lmList1[8][1]
        cx2 = lmList1[4][0]   #thumb point
        cy2 = lmList1[4][1]
        cx = (cx1+cx2)//2
        cy = (cy1+cy2)//2
        # print(cx,cy)
        cv2.circle(img, (cx,cy),10,(255,255,0), cv2.FILLED)
        cv2.line(img,(cx1,cy1),(cx2,cy2),(0,255,0),2)
        #rectangle

        length = math.hypot(cx2 - cx1, cy2 - cy1)
        print(length)

        pyautogui.moveTo(cx * 4, cy * 4)
        if length < 50:
            pyautogui.mouseDown(cx*4,cy*4)
            # pyautogui.moveTo(cx*4,cy*4)
        if length > 50:
            pyautogui.mouseUp()
            # break

    # Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
