const int potInt = A2;
const int buttonInt = 2;
boolean automatic = true;
float x = 1.57;

boolean going_up = false;

float value;
void setup() {
  Serial.begin(9600);
}

float scale(float meassure) {

  meassure = (meassure * 0.0048 * 16) + 40;
  return meassure;
}

void loop() {

  if (automatic == true) {
    if (x > 1.57) {
      going_up = false;
    } else if (x < -1.57) {
      going_up = true;
    }
    if (going_up) {
      x += 0.1;
    }
    else {
      x -= 0.1;
    }
    //Serial.print(x);
    value = sin(x);
    value = value + 1;
    value = (value * 40) + 40;
   Serial.println(value);

  } else {
    value = analogRead(potInt);
    value = scale(value);
    Serial.println(value);
  }
  if (digitalRead(buttonInt) == HIGH) {
    while (digitalRead(buttonInt) == HIGH);
    automatic = !automatic;
    Serial.print(automatic);
  }
  delay(100);
}
