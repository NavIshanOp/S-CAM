# S-CAM - Security Cam Bot

SECAM is a security camera bot that starts recording when motion is detected. The setup involves an ESP32 microcontroller, a PIR sensor, and an I2C LCD for status display. When motion is detected, the camera starts and records the event, and the LCD displays the current status.

## Connections

Connect the PIR sensor to the ESP32 as follows:
- PIR VCC to ESP32 3V3
- PIR GND to ESP32 GND
- PIR DATA PIN to ESP32 GPIO 13

Connect the I2C LCD to the ESP32 as follows:
- LCD VCC to ESP32 5V (or 3V3 if your LCD supports it)
- LCD GND to ESP32 GND
- LCD SDA to ESP32 GPIO 21
- LCD SCL to ESP32 GPIO 22

## Upload Code to ESP32

1. Open the Arduino IDE.
2. Ensure you have the necessary libraries installed:
    - `LiquidCrystal_I2C`
3. Upload the provided INO code to the ESP32:

    ```cpp
    #include <Wire.h>
    #include <LiquidCrystal_I2C.h>

    // Define the I2C address for the LCD
    LiquidCrystal_I2C lcd(0x27, 16, 2);  // Change the address if needed

    const int pirPin = 13;  // PIR sensor pin

    void setup() {
      pinMode(pirPin, INPUT);
      Serial.begin(115200);

      // Initialize the LCD
      lcd.begin(16, 2); 
      lcd.init();
      lcd.backlight();
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Initializing...");
      delay(2000);  // Wait for 2 seconds to display the initializing message

      // Clear the initializing message
      lcd.clear();
    }

    void loop() {
      int motionState = digitalRead(pirPin);
      
      if (motionState == HIGH) {
        Serial.println("Motion detected");
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Motion detected");
        delay(5000);
      } else {
        Serial.println("No Motion Detected");
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("No Motion Detected");
      }

      delay(1000);  // Delay to prevent rapid toggling
    }
    ```

## Run the Python Script

1. Install the necessary Python libraries:
    ```bash
    pip install pyserial
    pip install opencv-python
    ```
2. Check your device management for the correct serial port and update the following line in `main.py`:
    ```python
    serial_port = 'COM7'  # Change to your serial port (e.g., 'COM3' on Windows, '/dev/ttyUSB0' on Linux)
    ```

3. Run the Python script:
    ```bash
    python main.py
    ```

**Whenever motion is detected by the PIR sensor, the camera starts recording and saves the video in a user-created recording folder..**
*Make sure to create a folder called as recordings in the same place where your python file is located*
