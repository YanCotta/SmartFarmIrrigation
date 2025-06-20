#include <Arduino.h>
#include <DHT.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include "config.h"

// Initialize objects using constants from config.h
DHT dht(DHT_PIN, DHT22);
LiquidCrystal_I2C lcd(LCD_ADDRESS, LCD_COLS, LCD_ROWS);

// Memory Optimization: Use uint32_t instead of unsigned long (same size but more explicit)
uint32_t previousMillis = 0;

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

void loop() {  // Non-blocking timing logic
  if (millis() - previousMillis >= SENSOR_READ_INTERVAL) {
    // Memory Optimization: Read humidity with error checking using float (4 bytes) instead of double (8 bytes)
    float humidity = dht.readHumidity();
    if (isnan(humidity)) {
      humidity = 0.0f; // Memory Optimization: Use float literal (f suffix) instead of double
    }
    
    // Memory Optimization: Use uint8_t for digital readings (1 byte instead of int 4 bytes)
    // Read nutrient sensors (inverted logic due to pull-up)
    uint8_t phosphorus = !digitalRead(PHOSPHORUS_PIN); // 1 if pressed, 0 if not
    uint8_t potassium = !digitalRead(POTASSIUM_PIN);   // 1 if pressed, 0 if not
    
    // Memory Optimization: Use uint16_t for ADC reading (2 bytes instead of int 4 bytes)
    // Read and map pH (simulated via LDR)
    uint16_t phRaw = analogRead(LDR_PIN);
    float ph = map(phRaw, 0, 4095, 0, 1400) / 100.0f; // Memory Optimization: float division with f suffix
    
    // Irrigation logic using optimized thresholds from config.h
    // Memory Optimization: Use bool type (1 byte) for boolean result
    bool irrigate = (humidity < HUMIDITY_THRESHOLD && phosphorus && potassium && 
                    ph >= PH_MIN_THRESHOLD && ph <= PH_MAX_THRESHOLD);
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