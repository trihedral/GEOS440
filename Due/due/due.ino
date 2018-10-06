#include <SD.h>
#include "RTClib.h"
#include <Adafruit_MAX31865.h>
#define thermPin           A0     // analog 0
#define probePin           A1     // analog 1
#define SERIESRESISTOR     10000  // 10K resistor in series with thermister
#define THERMISTORNOMINAL  10000  // resistance at 25 degrees C  
#define TEMPERATURENOMINAL 25     // temp. for nominal resistance (almost always 25 C)
#define BCOEFFICIENT       3950   // The beta coefficient of the thermistor (usually 3000-4000)
#define logPin             10     // pin for the data logging shield
#define RREF               430.0  // The value of the Rref resistor
#define RNOMINAL           100.0  // The 'nominal' 0-degrees-C resistance of the sensor


Adafruit_MAX31865 amax = Adafruit_MAX31865(2, 3, 4, 5);
RTC_PCF8523 rtc;
DateTime curTime;
File logFile;

void setup() {
  analogReadResolution(12);
  pinMode(thermPin, INPUT);
  pinMode(probePin, INPUT);
  pinMode(logPin, OUTPUT);
  Serial.begin(9600);
  SD.begin(logPin);
  rtc.begin();
  amax.begin(MAX31865_3WIRE);
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
  Serial.print("Year");
  Serial.print(", ");
  Serial.print("Month");
  Serial.print(", ");
  Serial.print("Day");
  Serial.print(", ");
  Serial.print("Hour");
  Serial.print(", ");
  Serial.print("Minute");
  Serial.print(", ");
  Serial.print("Second");
  Serial.print(", ");
  Serial.print("Themistor");
  Serial.print(", ");
  Serial.print("Temperature Probe");
  Serial.print(", ");
  Serial.print("Platinum Rtd");
  Serial.println();

  // Save header to SD file //
  logFile.print("Year");
  logFile.print(", ");
  logFile.print("Month");
  logFile.print(", ");
  logFile.print("Day");
  logFile.print(", ");
  logFile.print("Hour");
  logFile.print(", ");
  logFile.print("Minute");
  logFile.print(", ");
  logFile.print("Second");
  logFile.print(", ");
  logFile.print("Themistor");
  logFile.print(", ");
  logFile.print("Temperature Probe");
  logFile.print(", ");
  logFile.print("Platinum Rtd");
  logFile.println();
}


void loop() {
  curTime = rtc.now();
  double thermistorReading = getThermistorReading();
  double probeReading      = getProbeReading();
  double rtdReading        = amax.temperature(RNOMINAL, RREF);
  
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
  Serial.print(thermistorReading);
  Serial.print(", ");
  Serial.print(probeReading);
  Serial.print(", ");
  Serial.print(rtdReading);
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
  logFile.print(thermistorReading);
  logFile.print(", ");
  logFile.print(probeReading);
  logFile.print(", ");
  logFile.print(rtdReading);
  logFile.println();
  
  logFile.flush();  // saves the file to the SD card
  delay(1000);
}

// This functions reads and calculates the termistor temp. It is called from the loop()
double getThermistorReading(){  
  int rawReading = analogRead(thermPin);                 // read value from pin
  double voltage = (4095.0 / rawReading) - 1;               // 
  double resistance = SERIESRESISTOR / voltage;           // convert to Resistance
  double steinhart = resistance / THERMISTORNOMINAL;      // (R/Ro)
  steinhart = log(steinhart);                            // ln(R/Ro)
  steinhart /= BCOEFFICIENT;                             // 1/B * ln(R/Ro)
  steinhart += 1.0 / (TEMPERATURENOMINAL + 273.15);      // + (1/To)
  steinhart = 1.0 / steinhart;                           // Invert
  double temperature = steinhart - 273.15;                // convert to C
  //temperature = temperature * 9 / 5 + 32;              // convert to F

  return temperature;
}

// This functions reads and calculates the probe temp. It is called from the loop()
double getProbeReading(){  
  int   rawReading   = analogRead(probePin);          // read value from pin
  double voltage     = rawReading * 3.3 / 4095.0;     // convert to voltage
  double temperature  = (voltage - 0.5) * 100 ;       // 
  //temperature  = (temperature * 9 / 5) + 32;  

  return temperature;
}
