#include <Wire.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <DHT.h>

#define SensorTurbidez A1
#define SensorPH A2
#define TdsSensorPin A3
#define VREF 5.0
#define SCOUNT 30
#define DHTPIN 2
#define DHTTYPE DHT11

OneWire oneWire(2);
DallasTemperature sensors(&oneWire);
DHT dht(DHTPIN, DHTTYPE);

unsigned long previousMillis = 0;
const long interval = 3600000; // 3600 segundos = 1 hora

float ArredondarPara(float ValorEntrada, int CasaDecimal) {
    float multiplicador = powf(10.0f, CasaDecimal);
    ValorEntrada = roundf(ValorEntrada * multiplicador) / multiplicador;
    return ValorEntrada;
}

int analogBuffer[SCOUNT];
int analogBufferTemp[SCOUNT];
int analogBufferIndex = 0;
int copyIndex = 0;
float averageVoltage = 0;
float tdsValue = 0;
float temperature = 16; // Temperatura inicial de compensação para o sensor TDS

int getMedianNum(int bArray[], int iFilterLen) {
    int bTab[iFilterLen];
    for (byte i = 0; i < iFilterLen; i++)
        bTab[i] = bArray[i];
    int i, j, bTemp;
    for (j = 0; j < iFilterLen - 1; j++) {
        for (i = 0; i < iFilterLen - j - 1; i++) {
            if (bTab[i] > bTab[i + 1]) {
                bTemp = bTab[i];
                bTab[i] = bTab[i + 1];
                bTab[i + 1] = bTemp;
            }
        }
    }
    if ((iFilterLen & 1) > 0) {
        bTemp = bTab[(iFilterLen - 1) / 2];
    } else {
        bTemp = (bTab[iFilterLen / 2] + bTab[iFilterLen / 2 - 1]) / 2;
    }
    return bTemp;
}

void setup() {
    Serial.begin(115200);
    pinMode(TdsSensorPin, INPUT);
    sensors.begin();
    dht.begin();
}

void loop() {
    unsigned long currentMillis = millis();
    
    // Leitura contínua para o sensor TDS
    if (millis() - previousMillis >= 40U) {
        previousMillis = millis();
        analogBuffer[analogBufferIndex] = analogRead(TdsSensorPin);
        analogBufferIndex++;
        if (analogBufferIndex == SCOUNT) {
            analogBufferIndex = 0;
        }
    }
    
    static unsigned long lastReadTime = 0;
    if (currentMillis - lastReadTime >= interval) {
        lastReadTime = currentMillis;
        
        // Leitura do sensor de turbidez
        float voltagem = 0;
        for (int i = 0; i < 800; i++) {
            voltagem += ((float)analogRead(SensorTurbidez) / 1023) * 5;
        }
        voltagem = voltagem / 800;
        voltagem = ArredondarPara(voltagem, 1);
        float NTU;
        if (voltagem < 2.5) {
            NTU = 3000;
        } else if (voltagem > 4.2) {
            NTU = 0;
            voltagem = 4.2;
        } else {
            NTU = -1120.4 * sq(voltagem) + 5742.3 * voltagem - 4353.8;
        }

        // Leitura do sensor de pH
        int sensorValue = analogRead(SensorPH);
        float voltage = (sensorValue * (5.00 / 1023.00));
        float ph = (voltage * -5.70) + 21.34;

        // Leitura do sensor de temperatura Dallas
        sensors.requestTemperatures();
        float tempDallas = sensors.getTempCByIndex(0);

        // Leitura do sensor de temperatura e umidade DHT
        float h = dht.readHumidity();
        float t = dht.readTemperature();

        // Cálculo e impressão do valor de TDS
        for (copyIndex = 0; copyIndex < SCOUNT; copyIndex++) {
            analogBufferTemp[copyIndex] = analogBuffer[copyIndex];
        }
        averageVoltage = getMedianNum(analogBufferTemp, SCOUNT) * (float)VREF / 1024.0;
        float compensationCoefficient = 1.0 + 0.02 * (temperature - 25.0);
        float compensationVoltage = averageVoltage / compensationCoefficient;
        tdsValue = (133.42 * compensationVoltage * compensationVoltage * compensationVoltage 
                    - 255.86 * compensationVoltage * compensationVoltage 
                    + 857.39 * compensationVoltage) * 0.5;

        // Imprime todos os valores na mesma linha, separados por vírgulas
        Serial.print(NTU); Serial.print(", ");
        Serial.print(ph); Serial.print(", ");
        Serial.print(tempDallas); Serial.print(", ");
        Serial.print(h); Serial.print(", ");
        Serial.print(t); Serial.print(", ");
        Serial.print(tdsValue, 0); Serial.println();
    }
}