float voltage;
float ph;

void setup() {
    Serial.begin(9600);
}

void loop() {
    int sensorValue = analogRead(A2);
    voltage = (sensorValue * (5.00 / 1023.00));
    ph = (voltage * -5.70) + 21.34;
    Serial.print(ph); 
    delay(1000);
}
