#include <Arduino.h>
#include <DHT.h>

#define DHT_PIN 23
#define PH_PIN 34
#define PHOSPHORUS_PIN 18
#define POTASSIUM_PIN 19
#define RELAY_PIN 26
#define DHT_TYPE DHT22

DHT dht(DHT_PIN, DHT_TYPE);

void setup() {  
  Serial.begin(115200);
  dht.begin();
  pinMode(PHOSPHORUS_PIN, INPUT_PULLUP);
  pinMode(POTASSIUM_PIN, INPUT_PULLUP);
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, LOW);
}

void loop() {
  float humidity = dht.readHumidity();
  int phosphorus = !digitalRead(PHOSPHORUS_PIN); // 1 se pressionado
  int potassium = !digitalRead(POTASSIUM_PIN);  // 1 se pressionado
  int phRaw = analogRead(PH_PIN);
  float ph = map(phRaw, 0, 4095, 0, 14); // Mapeia LDR para pH 0-14

  bool irrigate = (humidity < 50 && phosphorus && potassium && ph >= 6 && ph <= 7);
  digitalWrite(RELAY_PIN, irrigate ? HIGH : LOW);

  Serial.print("Umidade: "); Serial.print(humidity); Serial.print("% | ");
  Serial.print("Fósforo: "); Serial.print(phosphorus); Serial.print(" | ");
  Serial.print("Potássio: "); Serial.print(potassium); Serial.print(" | ");
  Serial.print("pH: "); Serial.print(ph); Serial.print(" | ");
  Serial.print("Bomba: "); Serial.println(irrigate ? "1" : "0");

  delay(2000);
}