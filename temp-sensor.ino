// Arduino Temperature Sensor Tool
const int sensorPin = A0;
const float baselineTemp = 20;     // Celcius (20C = 68F)
const int HALF_SECOND = 500;       // milliseconds

void setup() 
{
  // Open a serial port
  Serial.begin(9600);

  for (int pinNum = 2; pinNum < 5; pinNum++)
  {
    pinMode(pinNum, OUTPUT);
    digitalWrite(pinNum, LOW);
  }
}


void loop() 
{
  int sensorVal = analogRead(sensorPin);

  Serial.print("Sensor value: ");
  Serial.print(sensorVal);

  float voltage = 5.0 * (sensorVal / 1024.0);
  Serial.print(", Volts: ");
  Serial.print(voltage);

  float temp = 100 * (voltage - 0.5);
  Serial.print(", Temp: ");
  Serial.print(temp);
  Serial.print((char)176);
  Serial.println(" C");

  if (temp < baselineTemp + 2)
  {
    digitalWrite(2, LOW);
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
  }
  else if (temp >= baselineTemp + 2 && temp < baselineTemp + 4)
  {
    digitalWrite(2, HIGH);
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
  }
  else if (temp >= baselineTemp + 4 && temp < baselineTemp + 6)
  {
    digitalWrite(2, HIGH);
    digitalWrite(3, HIGH);
    digitalWrite(4, LOW);
  }
  else if (temp >= baselineTemp + 6)
  {
    digitalWrite(2, HIGH);
    digitalWrite(3, HIGH);
    digitalWrite(4, HIGH);
  }

  delay(HALF_SECOND);
  
}
