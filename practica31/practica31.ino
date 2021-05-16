#include <Stepper.h>

#define STEPS 100

Stepper stepper(STEPS, 8, 9, 10, 11);

int previous = 0;

void setup() {
  Serial.begin(9600);
  stepper.setSpeed(30);

}

void loop() {

  int val = analogRead(0);
  if (val >= 900) {
    Serial.println('o');
    stepper.step(-30);
    
  }
  if (val < 900) {
      Serial.println('c');
  }
}
