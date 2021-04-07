const int pot1 = A0;
const int pot2 = A1;
 
void setup()
{
   Serial.begin(9600);

}
 
 
void loop()
{
  if (Serial.available()>0){
   Serial.readString();
  
   Serial.print(analogRead(pot1));
   Serial.print("\t");
   Serial.print(analogRead(pot2));
   Serial.println();
   }
//   delay(100);    
}
