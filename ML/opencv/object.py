# import necessary packages
import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2
from sympy import false

# open webcam (웹캠 열기)
webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Could not open webcam")
    exit()
    

# loop through frames
while webcam.isOpened():

    # read frame from webcam 
    status, frame = webcam.read()

    if not status:
        break

    # apply object detection
    bbox, label, conf = cv.detect_common_objects(frame)

    print(bbox, label, conf)

    # draw bounding box over detected objects 
    #out = draw_bbox(frame, bbox, label, conf, write_conf=True)
    out = draw_bbox(frame, bbox, label, conf, write_conf=false)

    # display output
    cv2.imshow("Real-time object detection", out)

    # press "Q" to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# release resources
webcam.release()
cv2.destroyAllWindows() 