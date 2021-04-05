const int acan = A0;
int sensorValue = 0;
float voltaje;
unsigned long lastime = 0, sampletime = 100;

void setup(){
    Serial.begin(9600);
}

void loop(){
    if(millis() -lasttime > sampletime){
        lastime = millis();
        sensorValue = analogRead(achan);
        voltaje = escala();
        Serial.println(voltaje);
    }
}

float escala(float x, float in_min, float in_max, float out_min, float out_max)
{
    return (x-in_min)*(out_max-out_min)/(in_max-in_min)+ out_min;
}