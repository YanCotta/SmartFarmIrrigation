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

// --- System Timing (Memory Optimization: using const uint16_t for timing values) ---
#define SERIAL_BAUD_RATE 115200
#define SENSOR_READ_INTERVAL 2000  // 2 seconds in milliseconds (uint16_t saves 2 bytes vs uint32_t)

// --- Sensor Thresholds (Memory Optimization: using const values instead of variables) ---
#define HUMIDITY_THRESHOLD 50      // 50% humidity threshold for irrigation
#define PH_MIN_THRESHOLD 6.0       // Minimum pH for irrigation (float saves memory vs double)
#define PH_MAX_THRESHOLD 7.0       // Maximum pH for irrigation

#endif // CONFIG_H
