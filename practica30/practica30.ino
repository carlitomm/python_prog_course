#include <Servo.h>

int resistor = A0;
Servo door;

void setup() {
  door.attach(9);
  Serial.begin(9600);

}

void loop() {
  if(analogRead(resistor)>=900){
    Serial.println('o');
    door.write(180);
    delay(3000);
    door.write(0);
    Serial.println('c');
  }

}
