void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  float ua = analogRead(A0) * 5 / 1024.;
  float ub = analogRead(A1) * 5 / 1024.;
  float current = ub / 2e3;
  float resistance = (ua - ub) / current;

  Serial.print(resistance);
  Serial.println(" (ohm)");
  Serial.println("");
  
  delay(2000);
}
