#include <IRremote.h> 

IRsend irsend;

unsigned int lights_on[68] = {8900,4500,550,600,550,600,550,600,550,550,550,600,550,600,550,600,550,600,550,1650,550,1700,550,1650,550,1650,550,1650,550,1650,550,1700,550,1650,550,1650,550,600,550,1650,550,600,550,600,550,600,550,1650,550,600,550,600,550,1650,550,600,550,1650,550,1650,550,1700,550,550,550,1700,550,};
unsigned int lights_off[68] = {8950,4450,550,600,550,600,550,600,550,600,550,600,550,600,550,600,550,600,550,1650,550,1650,550,1650,550,1700,550,1650,550,1650,550,1650,550,1700,550,1650,550,1650,550,1650,550,600,550,600,550,600,550,1650,550,600,550,600,550,600,550,600,550,1650,550,1650,550,1700,550,550,600,1650,550,};
unsigned int dim_more[68] = {9000,4500,550,550,600,550,600,550,550,600,550,600,550,600,550,600,550,600,600,1650,550,1650,550,1650,550,1700,550,1650,550,1650,550,1700,500,1700,550,600,550,1650,550,600,550,1700,550,1650,550,600,550,1650,550,600,550,1650,550,600,550,1700,550,600,550,600,500,1700,550,600,500,1700,550,};
unsigned int dim_less[68] = {9000,4450,550,600,550,600,550,600,550,600,550,600,550,600,550,600,550,600,550,1650,550,1700,550,1650,550,1650,550,1700,550,1650,550,1650,550,1650,600,600,550,550,600,600,550,1650,550,600,550,600,550,600,550,600,550,1650,550,1700,550,1650,550,600,550,1650,550,1650,600,1650,550,1650,550,};

int IRPin = 3;
int lampPin = 4;

void setup(){
  pinMode(lampPin, 4);
  
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    switch (Serial.read()) {

      case '0':
        irsend.sendRaw(lights_on, 68, 38);
        break;

      case '1':
        irsend.sendRaw(lights_off, 68, 38);
        break;

      case '2':
        irsend.sendRaw(dim_more, 68, 38);
        break;

      case '3':
        irsend.sendRaw(dim_less, 68, 38);
        break;

      case '4':
        digitalWrite(lampPin, HIGH);
        break;

      case '5':
        digitalWrite(lampPin, LOW);
        break;

      default:
        break;
    }
  }
  delay(50);
}