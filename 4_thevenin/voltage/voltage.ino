void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  float voltage = analogRead(A0) * 5 / 1024.;

  Serial.print(voltage);
  Serial.println(" (V)");
  delay(2000);
}
