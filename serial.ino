char dataString[50] = {0};
int a = 0;

void setup() {
	Serial.begin(9600);				// Start serial connection
}

void loop() {
	a++;						// Increment "a" every loop
	sprintf(dataString, "%02X", a);			// Convert value to hex
	Serial.print(dataString);			// Send data
	delay(1000);					// Delay loop for 1 second
}
