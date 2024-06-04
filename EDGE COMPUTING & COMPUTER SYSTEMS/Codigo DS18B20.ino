#include <OneWire.h>  
#include <DallasTemperature.h>

#define dados 2

OneWire oneWire(dados);
DallasTemperature sensors(&oneWire);

void setup(void) { 
 Serial.begin(9600);
 sensors.begin();
} 

void loop(void) { 
 sensors.requestTemperatures();
 Serial.print(sensors.getTempCByIndex(0));
}