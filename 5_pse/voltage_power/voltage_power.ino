void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  float voltage = analogRead(A0) * 5 / 1024.;
  float power = voltage * voltage / 5.1e3;

  Serial.print(voltage, 3);
  Serial.println(" (V)");
  Serial.print(power*1e3, 3);
  Serial.println(" (mW)");
  
  delay(2000);
}
