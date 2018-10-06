// WARNING: THIS FILE CONTAINS NO ERROR CHECKING //

#include <SD.h>
#include "RTClib.h"
#define thermPin           0      // analog 0
#define tempPin            1      // analog 1
#define SERIESRESISTOR     10000  // 10K resistor in series with thermister
#define THERMISTORNOMINAL  10000  // resistance at 25 degrees C  
#define TEMPERATURENOMINAL 25     // temp. for nominal resistance (almost always 25 C)
#define BCOEFFICIENT       3950   // The beta coefficient of the thermistor (usually 3000-4000)
#define logPin             10     // pin for the data logging shield
#define voltLvl            3.3    // board voltage
#define ADCres             1024.0 // ADC resolution


RTC_PCF8523 RTC;
DateTime curTime;
File logFile;

void setup() {
  
  analogReference(EXTERNAL);
  RTC.begin();
  SD.begin(logPin);
  Serial.begin(9600);
  pinMode(logPin, OUTPUT);
  String fileName;
  for(int i=0; i<99999; i++){
    fileName = "uno_file";
    fileName += i;
    fileName += ".csv";
    if ( SD.exists(fileName) == false ){ // if file does not exist
      logFile = SD.open(fileName, FILE_WRITE);
      break;
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
  Serial.print(", ");
  Serial.print("Themister (Degrees C)");
  Serial.print(", ");
  Serial.print("Temperature Probe (Degrees C)");
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
  logFile.print(", ");
  logFile.print("Themister (Deg C)");
  logFile.print(", ");
  logFile.print("Temp Probe (Deg C)");
  logFile.println();
}


void loop() {
  curTime = RTC.now();
  
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
  Serial.print(", ");
  Serial.print(getThermisterReading());
  Serial.print(", ");
  Serial.print(getTempProbeReading());
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
  logFile.print(", ");
  logFile.print(getThermisterReading());
  logFile.print(", ");
  logFile.print(getTempProbeReading());
  logFile.println();
  
  logFile.flush();
  delay(1000);
}

// This functions reads and calculates the termistor temp. It is called from the loop()
float getThermisterReading(){  
  int rawReading = analogRead(thermPin);                 // read value from pin
  float voltage = ((ADCres-1)/ rawReading) - 1;             // 
  float resistance = SERIESRESISTOR / voltage;           // convert to Resistance
  float steinhart = resistance / THERMISTORNOMINAL;      // (R/Ro)
  steinhart = log(steinhart);                            // ln(R/Ro)
  steinhart /= BCOEFFICIENT;                             // 1/B * ln(R/Ro)
  steinhart += 1.0 / (TEMPERATURENOMINAL + 273.15);      // + (1/To)
  steinhart = 1.0 / steinhart;                           // Invert
  float temperature = resistance = steinhart - 273.15;   // convert to C
  //temperature = temperature * 9 / 5 + 32;                // convert to F

  return temperature;
}

// This functions reads and calculates the probe temp. It is called from the loop()
float getTempProbeReading(){  
  int   rawReading   = analogRead(tempPin);          // read value from pin
  float voltage      = rawReading * voltLvl / (ADCres-1);      // convert to voltage
  float temperature  = (voltage - 0.5) * 100 ;       // 
  //temperature  = (temperature * 9 / 5) + 32;  

  return temperature;
}
