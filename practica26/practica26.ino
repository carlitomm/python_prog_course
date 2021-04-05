
float x = 0;
float value;
void setup() {
  Serial.begin(9600);
  
}

void loop() {
  
  for (x=-3.14;x<3.14;x+=0.1){
    value = sin(x);
    Serial.println(value);
  }
  delay(100);
  
}
