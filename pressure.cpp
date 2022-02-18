#include <Arduino.h>

int FSRsensor = A0;                           
int value = 0;                                       
void setup() 
{
    pinMode(Led, OUTPUT);                 
    Serial.begin(9600);                           

}
void loop() 
{
    value = analogRead(FSRsensor);    
    Serial.println(value);                           

    delay(1000);                                   
}