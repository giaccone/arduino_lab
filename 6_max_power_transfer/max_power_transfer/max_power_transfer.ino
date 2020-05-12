#include <math.h>

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
  float power = (ua - ub) * current;

  if (isinf(resistance)){
    Serial.println("0 ; 0 ; 0");
  } else{
    Serial.print(current*1e3, 3);
    Serial.print(" ; ");
    Serial.print(resistance*1e-3, 3);
    Serial.print(" ; ");
    Serial.println(power*1e3, 3);
  }
  delay(500);
}
