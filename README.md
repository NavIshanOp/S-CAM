# SECAM
Security cam bot. Starts camera when motion is detected.
## Connections

Connect PIR VCC WITH ESP32 3V3 AND GND WITH GND.
DATA PIN WITH GPIO 13 OF ESP32.

Upload Ino code to esp32.

Run python file in ur computer.
Whenever Motion is detected in pir the camera starts and records it after creating a recording folder.

## Changes To Be Made
Check your device management. Search For PORT and correct the following line 

``` serial_port = 'COM7'  # Change to your serial port (e.g., 'COM3' on Windows, '/dev/ttyUSB0' on Linux) ```
