#include "HCSR04.h"

float dist = 100;
boolean alarma = false;
int intButton = A0;
int outBuzzer = 2;
int led = 13;


UltraSonicDistanceSensor distanceSensor(20, 21);


// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  pinMode(led, OUTPUT);
  pinMode(outBuzzer, OUTPUT);
  pinMode(intButton, INPUT);
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  if (alarma == false){
  double distance = distanceSensor.measureDistanceCm();
  Serial.println(distance);
  if (distance < 10 && distance != -1){
    alarma = true;
  }
  delay(50);
  }else{
    digitalWrite(outBuzzer, HIGH);
    delay(250);
    digitalWrite(outBuzzer, LOW);
    delay(250);
    if(digitalRead(intButton) == HIGH){
      alarma = false;
    }
  }
}
