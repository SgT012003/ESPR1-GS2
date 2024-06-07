# EDGE COMPUTING & COMPUTER SYSTEMS
Este código é um projeto Arduino que lê dados de múltiplos sensores e imprime os valores na console serial.

## Requisitos

- Wire.h: Esta biblioteca é usada para comunicação I2C e é frequentemente utilizada com dispositivos como sensores e displays. Foi desenvolvida pela equipe do Arduino.

- OneWire.h: Esta biblioteca é usada para comunicação de um único fio com dispositivos que suportam o protocolo OneWire. Foi desenvolvida por Paul Stoffregen.

- DallasTemperature.h: Esta biblioteca é usada para trabalhar com sensores de temperatura da família Dallas/Maxim, como o DS18B20. Foi desenvolvida pela equipe da Miles Burton.

- DHT.h: Esta biblioteca é usada para trabalhar com sensores de temperatura e umidade da família DHT, como o DHT11 e o DHT22. Foi desenvolvida por Adafruit Industries.

## Descrição

O projeto usa os seguintes sensores:

Sensor de turbidez ( SensorTurbidez )
Sensor de pH ( SensorPH )
Sensor de TDS ( TdsSensorPin )
Sensor de temperatura Dallas ( OneWire )
Sensor de temperatura e umidade DHT ( DHT )
O código lê dados de cada sensor e calcula os valores correspondentes. Os valores são então impressos na console serial em uma linha única, separados por vírgulas.

## Funções

- ArredondarPara -> uma função que arredonda um valor flutuante para um número especificado de casas decimais.
- getMedianNum -> uma função que calcula o valor mediano de um array.
- setup -> inicializa a console serial, define os modos de pino e inicia os protocolos OneWire e DHT.
- loop -> lê dados dos sensores, calcula os valores correspondentes e os imprime na console serial.

## Variáveis
> SensorTurbidez: o número de pino do sensor de turbidez.

> SensorPH: o número de pino do sensor de pH.

> TdsSensorPin: o número de pino do sensor de TDS.

> VREF: a tensão de referência para o sensor de TDS.

> SCOUNT: o número de amostras a serem coletadas para o sensor de TDS.

> DHTPIN: o número de pino do sensor DHT.

> DHTTYPE: o tipo de sensor DHT usado.

> analogBuffer e analogBufferTemp: arrays para armazenar as leituras do sensor de TDS.

> averageVoltage e tdsValue: variáveis para armazenar o valor de TDS calculado.

> temperature: o valor de temperatura inicial para compensação de TDS.

## Pinagem
|Sensor|Entrada|
|:--:|:---:|
|Sensor Turbidez |A1|
|Sensor PH |A2|
|Tds Sensor Pin |A3|
|DHTPIN |2|

## Resumo
Este projeto demonstra o uso de múltiplos sensores com uma placa Arduino. O código lê dados de cada sensor, calcula os valores correspondentes e os imprime na console serial. O projeto usa várias funções e variáveis para alcançar essa funcionalidade.

Se você tiver alguma dúvida ou precisar de esclarecimentos adicionais, basta perguntar!