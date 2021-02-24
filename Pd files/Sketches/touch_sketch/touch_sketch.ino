#define touchPin 3
#define ledPin 13

void setup() {
  pinMode(touchPin, INPUT);
  pinMode(ledPin, OUTPUT);

  Serial.begin(9600);
}

void loop() {
//  digitalWrite(ledPin, digitalRead(touchPin));

  Serial.println(analogRead(A0));
  delay(100);
}
