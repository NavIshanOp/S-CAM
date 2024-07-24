const int pirPin = 13;  // PIR sensor pin

void setup() {
  pinMode(pirPin, INPUT);
  Serial.begin(115200);
}

void loop() {
  int motionState = digitalRead(pirPin);
  
  if (motionState == HIGH) {
    Serial.println("Motion detected");
    delay(5000);
  } else {
    if (motionState == LOW) {
    Serial.println("No Motion Detected");
    }
  }
}