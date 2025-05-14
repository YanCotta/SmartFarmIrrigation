#include <Arduino.h>
#include <DHT.h>

// Define pin constants
#define DHT_PIN 23          // DHT22 sensor pin
#define PH_PIN 34           // LDR pin for simulated pH
#define PHOSPHORUS_PIN 18   // Button for phosphorus presence
#define POTASSIUM_PIN 19    // Button for potassium presence
#define RELAY_PIN 26        // Relay pin for irrigation pump
#define DHT_TYPE DHT22      // DHT sensor type

DHT dht(DHT_PIN, DHT_TYPE);

void setup() {
  Serial.begin(115200);          // Start serial communication
  dht.begin();                   // Initialize DHT sensor
  pinMode(PHOSPHORUS_PIN, INPUT_PULLUP); // Set phosphorus pin with pull-up
  pinMode(POTASSIUM_PIN, INPUT_PULLUP);  // Set potassium pin with pull-up
  pinMode(RELAY_PIN, OUTPUT);    // Set relay as output
  digitalWrite(RELAY_PIN, LOW);  // Ensure pump is off initially
}

void loop() {
  // Read humidity with error checking
  float humidity = dht.readHumidity();
  if (isnan(humidity)) {
    Serial.println("Error reading humidity from DHT22!");
    delay(2000);
    return;
  }

  // Read nutrient sensors (inverted logic due to pull-up)
  int phosphorus = !digitalRead(PHOSPHORUS_PIN); // 1 if pressed
  int potassium = !digitalRead(POTASSIUM_PIN);   // 1 if pressed

  // Read and map pH (simulated via LDR)
  int phRaw = analogRead(PH_PIN);
  float ph = map(phRaw, 0, 4095, 0, 14); // Map 0-4095 to pH 0-14

  // Irrigation logic: irrigate if humidity < 50%, nutrients present, pH 6-7
  bool irrigate = (humidity < 50 && phosphorus && potassium && ph >= 6 && ph <= 7);
  digitalWrite(RELAY_PIN, irrigate ? HIGH : LOW); // Control pump

  // Print data to serial monitor
  Serial.print("Humidity: "); Serial.print(humidity); Serial.print("% | ");
  Serial.print("Phosphorus: "); Serial.print(phosphorus); Serial.print(" | ");
  Serial.print("Potassium: "); Serial.print(potassium); Serial.print(" | ");
  Serial.print("pH: "); Serial.print(ph); Serial.print(" | ");
  Serial.print("Pump: "); Serial.println(irrigate ? "1" : "0");

  delay(2000); // Wait 2 seconds
}