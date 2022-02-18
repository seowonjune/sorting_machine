int Laser_pin = 7; 
void setup() {
  pinMode(Laser_pin, OUTPUT);
}
void loop() {
  digitalWrite(Laser_pin,HIGH);
  delay(1000);
  digitalWrite(Laser_pin,LOW);
  delay(1000);
}