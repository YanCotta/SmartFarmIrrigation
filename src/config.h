#ifndef CONFIG_H
#define CONFIG_H

// --- Pinout Configuration ---
#define DHT_PIN 23
#define LDR_PIN 34
#define PHOSPHORUS_PIN 18
#define POTASSIUM_PIN 19
#define RELAY_PIN 26

// --- I2C Configuration ---
#define LCD_ADDRESS 0x27
#define LCD_COLS 16
#define LCD_ROWS 2

// --- System Timing ---
#define SERIAL_BAUD_RATE 115200
#define SENSOR_READ_INTERVAL 2000 // Sensor read interval in milliseconds

#endif // CONFIG_H
