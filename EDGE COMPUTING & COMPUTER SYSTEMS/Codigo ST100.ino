#include <Wire.h>

int SensorTurbidez = A1;

int i;
float voltagem;
float NTU;

void setup() {
  Serial.begin(9600);
}

void loop() {
  voltagem = 0;

  for (i = 0; i < 800; i++) {
    voltagem += ((float)analogRead(SensorTurbidez) / 1023) * 5;
  }

  voltagem = voltagem / 800;
  voltagem = ArredondarPara(voltagem, 1);

  if (voltagem < 2.5) {
    NTU = 3000;
  }
  else if (voltagem > 4.2) {
    NTU = 0;
    voltagem = 4.2;
  }
  else {
    NTU = -1120.4 * sq(voltagem) + 5742.3 * voltagem - 4353.8;
  }

  Serial.print(NTU);
  
  delay(10);
}

float ArredondarPara(float ValorEntrada, int CasaDecimal) {
  float multiplicador = powf(10.0f, CasaDecimal);
  ValorEntrada = roundf(ValorEntrada * multiplicador) / multiplicador;
  return ValorEntrada;
}
