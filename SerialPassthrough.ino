/*
  Serial sketch

*/

void setup() {
  Serial.begin(19200);
}

void loop() {
    Serial.write("x = 1\n");   // read it and send it out Serial1 (pins 0 & 1);
    delay(1000);
  }
