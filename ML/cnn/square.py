import numpy as np
import cv2

lowerBound = np.array([74, 70, 99])
upperBound = np.array([95, 110, 255])

def showcam():
    try:
        print ('open cam')
        cap = cv2.VideoCapture(0)
    except:
        print ('Not working')
        return
    cap.set(3, 640)
    cap.set(4, 480)
    while True:
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        Gmask = cv2.inRange(hsv, lowerBound, upperBound)
        ret1, thr = cv2.threshold(Gmask, 127, 255, 0)
        _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 0:
            for i in range(len(contours)):
                # Get area value
                area = cv2.contourArea(contours[i])
                if area > 100:  # minimum yellow area
                    rect = cv2.minAreaRect(contours[i])
                    box = cv2.boxPoints(rect)
                    box = np.int0(box)
                    frame = cv2.drawContours(frame, [box], -1, (0, 255, 0), 3)
        if not ret:
            print('error')
            break
        cv2.imshow('bitwise', Gmask)
        cv2.imshow('cam_load', frame)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
showcam()