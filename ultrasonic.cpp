#include <Arduino.h>

//초음파 센서 핀 설정 (Ultrasonic sensor)
#define TRIG 9 //TRIG 핀 설정 (초음파 보내는 핀)
#define ECHO 8 //ECHO 핀 설정 (초음파 받는 핀)


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  //초음파 센서 부분
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  //초음파 센서
  long duration, distance;

  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);

  duration = pulseIn(ECHO, HIGH);  //물체에 반사되어 돌아온 초음파의 시간을 변수에 저장
  
  distance = duration * 17 / 1000;  //거리를 cm 단위로 변환

  //ultrasonic sensor로 측정한 거리같 serial 포트에 출력
  Serial.println("duration: ");
  Serial.println(duration);
  Serial.println("\ndistance: ");
  Serial.println(distance);

  delay(1000); //dealy timne 1s
}