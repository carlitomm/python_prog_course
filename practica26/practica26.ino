const int potInt = A2;

float x = 0;
float value;
void setup() {
  Serial.begin(9600);
}

void loop() {
  value = analogRead(A2);
  for (x=-3.14;x<3.14;x+=0.1){
    value = sin(x);
    value = value + 1;
    value = value * 40;
    Serial.println(value);
  }
  delay(100);
}
