#define SOUND_SENSOR_PIN 2

void setup() {
    pinMode(SOUND_SENSOR_PIN, INPUT);
    Serial.begin(9600);
}

void loop() {
    if (digitalRead(SOUND_SENSOR_PIN) == HIGH) {
        Serial.println("DETECTED");
        delay(30000);
    }
}
