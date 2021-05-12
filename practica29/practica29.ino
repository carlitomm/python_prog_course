#include "MeccaBrain.h"

MeccaBrain mb(2);

int incoming;
byte red;
byte green;
byte blue;


void setup() {
   Serial.begin(9600);
}

void loop() {
  mb.communicate();
  if(Serial.available()>0){
    incoming = Serial.read();
    if (incoming == 'r'){
      red = byte(Serial.parseInt());
    }
    if (incoming == 'g'){
      green = byte(Serial.parseInt());
    }
    if (incoming == 'b'){
      blue = byte(Serial.parseInt());
    }
    mb.setLEDColor(red, green, blue, 8);
  }
  
}
