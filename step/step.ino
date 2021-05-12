//control de motor a pasos 
//via serial con python

//Establecer pines de motor a pasos
int pinesmotor[] = {8,9,10,11};

void setup()
{
    Serial.begin(9600);
    pinMode(8,OUTPUT);
    pinMode(9,OUTPUT);
    pinMode(10,OUTPUT);
    pinMode(11,OUTPUT);
}

void loop()
{
    if (Serial.available()>0)
    {
        int dato = Serial.read();

        if (dato == '1')
        { 
            //vuelta a derecha
            //Giro Adelante
            giroizquirda();
            delay(20);
        }

        if (dato == '2')
        {
            //vuelta izquierda
            //Giro Atras
            giroderecha();
            delay(20);
        }

    }
}
//giro derecha
//Gito Atras
void giroderecha()
{
    digitalWrite(pinesmotor[0],LOW);
    digitalWrite(pinesmotor[1],LOW);
    digitalWrite(pinesmotor[2],LOW);
    digitalWrite(pinesmotor[3],HIGH);
    delay(5);
    digitalWrite(pinesmotor[0],LOW);
    digitalWrite(pinesmotor[1],LOW);
    digitalWrite(pinesmotor[2],HIGH);
    digitalWrite(pinesmotor[3],HIGH);
    delay(5);
    digitalWrite(pinesmotor[0],LOW);
    digitalWrite(pinesmotor[1],LOW);
    digitalWrite(pinesmotor[2],HIGH);
    digitalWrite(pinesmotor[3],LOW);
    delay(5);
    digitalWrite(pinesmotor[0],LOW);
    digitalWrite(pinesmotor[1],HIGH);
    digitalWrite(pinesmotor[2],HIGH);
    digitalWrite(pinesmotor[3],LOW);
    delay(5);
    digitalWrite(pinesmotor[0],LOW);
    digitalWrite(pinesmotor[1],HIGH);
    digitalWrite(pinesmotor[2],LOW);
    digitalWrite(pinesmotor[3],LOW);
    delay(5);
    digitalWrite(pinesmotor[0],HIGH);
    digitalWrite(pinesmotor[1],HIGH);
    digitalWrite(pinesmotor[2],LOW);
    digitalWrite(pinesmotor[3],LOW);
    delay(5);
    digitalWrite(pinesmotor[0],HIGH);
    digitalWrite(pinesmotor[1],LOW);
    digitalWrite(pinesmotor[2],LOW);
    digitalWrite(pinesmotor[3],LOW);
    delay(5);
    digitalWrite(pinesmotor[0],HIGH);
    digitalWrite(pinesmotor[1],LOW);
    digitalWrite(pinesmotor[2],LOW);
    digitalWrite(pinesmotor[3],HIGH);
    delay(5);
}

//giro Adelante
void giroizquirda()
{
    digitalWrite(pinesmotor[0],HIGH);
    digitalWrite(pinesmotor[1],LOW);
    digitalWrite(pinesmotor[2],LOW);
    digitalWrite(pinesmotor[3],HIGH);
    delay(5);
    digitalWrite(pinesmotor[0],HIGH);
    digitalWrite(pinesmotor[1],LOW);
    digitalWrite(pinesmotor[2],LOW);
    digitalWrite(pinesmotor[3],LOW);
    delay(5);
    digitalWrite(pinesmotor[0],HIGH);
    digitalWrite(pinesmotor[1],HIGH);
    digitalWrite(pinesmotor[2],LOW);
    digitalWrite(pinesmotor[3],LOW);
    delay(5);
    digitalWrite(pinesmotor[0],LOW);
    digitalWrite(pinesmotor[1],HIGH);
    digitalWrite(pinesmotor[2],LOW);
    digitalWrite(pinesmotor[3],LOW);
    delay(5);
    digitalWrite(pinesmotor[0],LOW);
    digitalWrite(pinesmotor[1],HIGH);
    digitalWrite(pinesmotor[2],HIGH);
    digitalWrite(pinesmotor[3],LOW);
    delay(5);
    digitalWrite(pinesmotor[0],LOW);
    digitalWrite(pinesmotor[1],LOW);
    digitalWrite(pinesmotor[2],HIGH);
    digitalWrite(pinesmotor[3],LOW);
    delay(5);
    digitalWrite(pinesmotor[0],LOW);
    digitalWrite(pinesmotor[1],LOW);
    digitalWrite(pinesmotor[2],HIGH);
    digitalWrite(pinesmotor[3],HIGH);
    delay(5);
    digitalWrite(pinesmotor[0],LOW);
    digitalWrite(pinesmotor[1],LOW);
    digitalWrite(pinesmotor[2],LOW);
    digitalWrite(pinesmotor[3],HIGH);
    delay(5);
}
