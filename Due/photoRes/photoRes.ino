#include <SD.h>
#include "RTClib.h"
#define photoRes             0     // pin for the data logging shield

void setup() {
  Serial.begin(9600);
  pinMode(photoRes, INPUT);
}

void loop() {
  analogReadResolution(12);
  // Print data to serial monitor //
  Serial.print(analogRead(photoRes));
  Serial.println();
  
  delay(500);
}
