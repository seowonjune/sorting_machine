import cv2 as cv
import numpy as np
import tensorflow as tf
from keras.models import load_model

#이미지 파일 > 그레이스케일
img_color = cv.imread('D:/2020/num.jpg', cv.IMREAD_COLOR)
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)

#그레이 스케일 > 바이너리 
ret,img_binary = cv.threshold(img_gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)

cv.imshow('binary', img_binary)
cv.waitKey(0)

kernel = cv.getStructuringElement( cv.MORPH_RECT, ( 5, 5 ) )
#모폴로지 연산 빈값은 0으로 채움
img_binary = cv.morphologyEx(img_binary, cv. MORPH_CLOSE, kernel)

cv.imshow('morphlogy', img_binary)
cv.waitKey(0)

#숫자 구분 contours
contours, hierarchy = cv.findContours(img_binary, cv.RETR_EXTERNAL, 
                        cv.CHAIN_APPROX_SIMPLE)
for contour in contours:

    #숫자별로 경계박스 구하기
    x, y, w, h = cv.boundingRect(contour)

    #가로, 세로 중 긴 방향을 택 후 , 여분을 추가하여 한변의 크기를 정함
    length = max(w, h) + 60
    
    #빈 이미지를 생성
    img_digit = np.zeros((length, length, 1),np.uint8)

    #숫자가 이미지의 정중앙에 오도록 경계박스의 시작 위치를 조정
    new_x,new_y = x-(length - w)//2, y-(length - h)//2

    img_digit = img_binary[new_y:new_y+length, new_x:new_x+length]

    #kernel = np.ones((5, 5), np.uint8)
    #숫자 인식을 위해 팽창 모폴로지 연산 적용
    #img_digit = cv.morphologyEx(img_digit, cv.MORPH_DILATE, kernel)

    #cv.imshow('digit', img_digit)
    #cv.waitKey(0)

    #학습된 모델을 불러온다
    model = load_model('mnist.h5')

    #이미지 크기를 학습에서 요구되는 28*28 변환 함.
    img_digit = cv.resize(img_digit, (28, 28), interpolation=cv.INTER_AREA)

    #학습 픽셀 0~1 사이로 변환 
    img_digit = img_digit / 255.0

    img_input = img_digit.reshape(1, 28, 28, 1)
    predictions = model.predict(img_input)

    #인식된 숫자 
    number = np.argmax(predictions)
    print(number)

    cv.rectangle(img_color, (x, y), (x+w, y+h), (255, 255, 0), 2)

    location = (x + int(w *0.5), y - 10)
    font = cv.FONT_HERSHEY_COMPLEX  
    fontScale = 1.2
    cv.putText(img_color, str(number), location, font, fontScale, (0,255,0), 2)
    
    #결과
    cv.imshow('digit', img_digit)
    cv.waitKey(0)

#원본이미지 + 결과표
cv.imshow('result', img_color)
cv.waitKey(0)