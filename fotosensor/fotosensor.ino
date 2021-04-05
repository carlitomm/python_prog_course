const sv = 2;
const rled = 4;
const int gled = 5;
int val

void setup(){
    pinMode(sv, INPUT);
    pinMode(rled, INPUT);
    pinMode(gled, INPUT);
}

void loop(){

    val = digitalRead(sv)

    if(val = HIGH)
    {
        digitalWrite(gled, HIGH);
        digitalWrite(rled, LOW);
    }
    else{
         {
        digitalWrite(gled, LOW);
        digitalWrite(rled, HIGH);
    }
    }
}
