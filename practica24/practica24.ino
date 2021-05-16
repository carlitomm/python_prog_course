#include <Adafruit_Sensor.h>
#include <DHT.h>

// Set DHT pin:
#define DHTPIN 2
// Set DHT type, uncomment whatever type you're using!
#define DHTTYPE DHT11   // DHT 11 
//#define DHTTYPE DHT22   // DHT 22  (AM2302)
//#define DHTTYPE DHT21   // DHT 21 (AM2301)
// Initialize DHT sensor for normal 16mhz Arduino:
DHT dht = DHT(DHTPIN, DHTTYPE);

void setup() {
  // Begin serial communication at a baud rate of 9600:
  Serial.begin(9600);
  // Setup sensor:
  dht.begin();
}
void loop() {
  // Wait a few seconds between measurements:
  delay(2000);
  float h = dht.readHumidity();

  float t = dht.readTemperature();   // Read the temperature as Celsius:
  
  float f = dht.readTemperature(true); // Read the temperature as Fahrenheit:
  
  // Check if any reads failed and exit early (to try again):
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  
  float hif = dht.computeHeatIndex(f, h); // Compute heat index in Fahrenheit (default):
  
  float hic = dht.computeHeatIndex(t, h, false); // Compute heat index in Celsius:
  Serial.print(h);
  Serial.print("\t");

  Serial.print(t);
  Serial.println();
}
