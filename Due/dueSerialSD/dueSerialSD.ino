#include <SD.h>
#include "RTClib.h"
#define logPin             10     // pin for the data logging shield

RTC_PCF8523 rtc;
DateTime curTime;
File logFile;

void setup() {
  Serial.begin(9600);
  pinMode(logPin, OUTPUT);
  
  char fileName[] = "LOG000.CSV";
  for (int i = 0; i < 1000; i++) {
    fileName[3] = i/100      + '0';
    fileName[4] = (i%100)/10 + '0';
    fileName[5] = i%10       + '0';
    if (! SD.exists(fileName)) {
      // only open a new file if it doesn't exist
      logFile = SD.open(fileName, FILE_WRITE); 
      break;  // leave the loop!
    }
  }

  // Print header to serial monitor //
  Serial.print("year");
  Serial.print(", ");
  Serial.print("month");
  Serial.print(", ");
  Serial.print("day");
  Serial.print(", ");
  Serial.print("hour");
  Serial.print(", ");
  Serial.print("minute");
  Serial.print(", ");
  Serial.print("second");
  Serial.println();

  // Save header to SD file //
  logFile.print("year");
  logFile.print(", ");
  logFile.print("month");
  logFile.print(", ");
  logFile.print("day");
  logFile.print(", ");
  logFile.print("hour");
  logFile.print(", ");
  logFile.print("minute");
  logFile.print(", ");
  logFile.print("second");
  logFile.println();
}

void loop() {
  curTime = rtc.now();
  
  // Print data to serial monitor //
  Serial.print(curTime.year());
  Serial.print(", ");
  Serial.print(curTime.month());
  Serial.print(", ");
  Serial.print(curTime.day());
  Serial.print(", ");
  Serial.print(curTime.hour());
  Serial.print(", ");
  Serial.print(curTime.minute());
  Serial.print(", ");
  Serial.print(curTime.second());
  Serial.println();
  
  // Save data to SD file //
  logFile.print(curTime.year());
  logFile.print(", ");
  logFile.print(curTime.month());
  logFile.print(", ");
  logFile.print(curTime.day());
  logFile.print(", ");
  logFile.print(curTime.hour());
  logFile.print(", ");
  logFile.print(curTime.minute());
  logFile.print(", ");
  logFile.print(curTime.second());
  logFile.println();
  
  logFile.flush();
  delay(1000);
}
