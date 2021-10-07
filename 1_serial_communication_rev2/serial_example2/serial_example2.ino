float k = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print(k);
  Serial.print(" ; ");
  Serial.println(k * k);
  k += 1;
  delay(2000);
}
