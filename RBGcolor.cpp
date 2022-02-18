#include <Wire.h>
#include "Adafruit_TCS34725.h"

Adafruit_TCS34725 tcs = Adafruit_TCS34725(TCS34725_INTEGRATIONTIME_50MS, TCS34725_GAIN_4X);   // Adafruit_TCS34725라이브러리 사용을 위한 객체 생성

void setup() {
  Serial.begin(9600);

  if (tcs.begin()) {    
    Serial.println("Found sensor");
  } else {              
    Serial.println("No TCS34725 found ... check your connections");
    while (1);          
  }
}

void loop() {
  uint16_t clear, red, green, blue;

  delay(60);

  tcs.getRawData(&red, &green, &blue, &clear);    

  int r = map(red, 0, 21504, 0, 1025);
  int g = map(green, 0, 21504, 0, 1025);
  int b = map(blue, 0, 21504, 0, 1025); 

  Serial.print("\tR:\t"); Serial.print(r);
  Serial.print("\tG:\t"); Serial.print(g);
  Serial.print("\tB:\t"); Serial.println(b);
}