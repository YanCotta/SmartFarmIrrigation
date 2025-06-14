#include <Arduino.h>
#include <DHT.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include "config.h"

// Initialize objects using constants from config.h
DHT dht(DHT_PIN, DHT22);
LiquidCrystal_I2C lcd(LCD_ADDRESS, LCD_COLS, LCD_ROWS);

// Global timing variable
unsigned long previousMillis = 0;

void setup() {
  // Initialize Serial Monitor
  Serial.begin(SERIAL_BAUD_RATE);
  
  // Initialize LCD and backlight
  lcd.init();
  lcd.backlight();
  
  // Initialize DHT sensor
  dht.begin();
  
  // Configure pin modes using constants from config.h
  pinMode(PHOSPHORUS_PIN, INPUT_PULLUP);
  pinMode(POTASSIUM_PIN, INPUT_PULLUP);
  pinMode(RELAY_PIN, OUTPUT);
  
  // Ensure pump is off initially
  digitalWrite(RELAY_PIN, LOW);
  
  // Display startup message
  lcd.setCursor(0, 0);
  lcd.print("Smart Irrigation");
  lcd.setCursor(0, 1);
  lcd.print("System Starting");
  delay(2000); // Only delay allowed for startup message
  lcd.clear();
}

void loop() {
  // Non-blocking timing logic
  if (millis() - previousMillis >= SENSOR_READ_INTERVAL) {
    // Read humidity with error checking
    float humidity = dht.readHumidity();
    if (isnan(humidity)) {
      humidity = 0; // Set default value for error case
    }
    
    // Read nutrient sensors (inverted logic due to pull-up)
    int phosphorus = !digitalRead(PHOSPHORUS_PIN); // 1 if pressed
    int potassium = !digitalRead(POTASSIUM_PIN);   // 1 if pressed
    
    // Read and map pH (simulated via LDR)
    int phRaw = analogRead(LDR_PIN);
    float ph = map(phRaw, 0, 4095, 0, 1400) / 100.0; // Map 0-4095 to pH 0-14.0
    
    // Irrigation logic: irrigate if humidity < 50%, nutrients present, pH 6-7
    bool irrigate = (humidity < 50 && phosphorus && potassium && ph >= 6.0 && ph <= 7.0);
    digitalWrite(RELAY_PIN, irrigate ? HIGH : LOW); // Control pump
    
    // Format Serial output for Serial Plotter (numeric values separated by spaces)
    Serial.print(humidity);
    Serial.print(" ");
    Serial.print(ph);
    Serial.print(" ");
    Serial.print(phosphorus);
    Serial.print(" ");
    Serial.print(potassium);
    Serial.print(" ");
    Serial.println(irrigate ? 1 : 0);
    
    // Update LCD display
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("H:");
    lcd.print(humidity, 1);
    lcd.print("% pH:");
    lcd.print(ph, 1);
    
    lcd.setCursor(0, 1);
    lcd.print("Pump: ");
    lcd.print(irrigate ? "ON " : "OFF");
    lcd.print(" P:");
    lcd.print(phosphorus);
    lcd.print(" K:");
    lcd.print(potassium);
    
    // Update timing variable
    previousMillis = millis();
  }
}