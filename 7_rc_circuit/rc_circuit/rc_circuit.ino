// initialization
float initial_condition;
unsigned long t0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  initial_condition = analogRead(A0)*5/1024.;
}

void loop() {
  // put your main code here, to run repeatedly:
  float tolerance = 0.1;
  float npt = 80;
  
  // stop here until variation is < tolerance
  while (fabs(analogRead(A0)*5/1024. - initial_condition) < tolerance) {
    t0 = micros();
    }

  // begin acquisition
  for (int i = 0; i < npt; i++) {
    unsigned long now = micros();
    Serial.print(now - t0);
    Serial.print(" ; ");
    float voltage = analogRead(A0)*5/1024.;
    Serial.println(voltage);
    }
  
  // stop execution here 
  while (1) {
    // do nothing
    }
  }
