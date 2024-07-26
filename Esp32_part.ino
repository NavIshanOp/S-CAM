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
