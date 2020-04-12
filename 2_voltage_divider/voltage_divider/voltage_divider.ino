void setup() {
  // initialize serial communication 
  Serial.begin(9600);

}

void loop() {
  // read analog input A0
  float vr2 = analogRead(A0) * 5 / 1024.;
  // print reading
  Serial.print("VR2 = ");
  Serial.print(vr2, 3);
  Serial.println(" (V)");
  delay(2000);

}
