# SECAM - Security Cam Bot

SECAM is a security camera bot that starts recording when motion is detected. The setup involves an ESP32 microcontroller and a PIR sensor. When motion is detected, the camera starts and records the event.

## Connections

Connect the PIR sensor to the ESP32 as follows:
- PIR VCC to ESP32 3V3
- PIR GND to ESP32 GND
- PIR DATA PIN to ESP32 GPIO 13

## Upload Code to ESP32

1. Open the Arduino IDE.
2. Upload the provided INO code to the ESP32.

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

Whenever motion is detected by the PIR sensor, the camera starts recording and saves the video in a newly created recording folder.
