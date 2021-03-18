/* We use an exclamation mark (!) to signify the beginning of a new value
this is followed by the pin number and value
each value concludes with a newline

if you want to use any of the pins for anything other than input, you must remove them
from the list INPUT_PINS
*/

//#define DELAY 100
#define ANALOG_SIZE 2
#define DIGITAL_SIZE 2
#define SENSITIVITY_BUFFER 5

int ANALOG_VALUES[ANALOG_SIZE] = {0};
unsigned int DIGITAL_VALUES[DIGITAL_SIZE] = {0};

unsigned int ANALOG_INPUT_PINS[ANALOG_SIZE] = {
        A0, A1, //A2, A3, A4, A5,
};

unsigned int DIGITAL_INPUT_PINS[DIGITAL_SIZE] = {
        2, 3, //4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
};


void setup() {
      	Serial.begin(9600);
        
        // Set pins as inputs
      	for(int i=0; i<ANALOG_SIZE; i++)
      	{
      		      pinMode(ANALOG_INPUT_PINS[i], INPUT);
      
      	}

        for(int i=0; i<DIGITAL_SIZE; i++)
        {
                pinMode(DIGITAL_INPUT_PINS[i], INPUT_PULLUP); 
        }
}

void loop() {

        // Loop over each pin, read the input and output the result if it has changed
      	for(int i=0; i<ANALOG_SIZE; i++)
      	{
            		int pin = ANALOG_INPUT_PINS[i];
                int pinVal = analogRead(pin);
                int lastVal = ANALOG_VALUES[i];
                
                if(abs(lastVal - pinVal) >= SENSITIVITY_BUFFER)
                {
                        ANALOG_VALUES[i] = pinVal;
                        
                        Serial.println("!");
                        Serial.println(pin);
                        Serial.println(pinVal);
                }
      	}
      
        for(int i=0; i<DIGITAL_SIZE; i++)
        {
                unsigned int pin = DIGITAL_INPUT_PINS[i];
                unsigned int pinVal = digitalRead(pin);
                unsigned int lastVal = DIGITAL_VALUES[i];

                if(lastVal != pinVal)
                {
                        DIGITAL_VALUES[i] = pinVal;

                        Serial.println("!");
                        Serial.println(pin);
                        Serial.println(pinVal);
                }
        }     
        
//        delay(DELAY);
}
