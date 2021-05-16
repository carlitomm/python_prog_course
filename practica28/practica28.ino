

int ledPin = 13;
boolean ledState = LOW;

String value;
void setup() {
  pinMode(8, INPUT);
  pinMode(13, OUTPUT);

  Serial.begin(9600);
  Serial.setTimeout(50);
  ledState = !ledState;
  digitalWrite(ledPin, LOW);

}


void loop() {
  if (Serial.available() > 0) {
    value = Serial.readString();

    ledState = !ledState;
    Serial.println(ledState);
    digitalWrite(ledPin, ledState);
  }
}
