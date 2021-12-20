// turn led on when even number input and off when odd input detected

int x;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(115200);
  Serial.setTimeout(1);
  // Serial.println("AOA");
}
void loop() {
  while (!Serial.available())
    ;
  x = Serial.readString().toInt();
  if (x % 2 == 0) {
    digitalWrite(LED_BUILTIN, HIGH);
  }    // turn the LED on (HIGH is the voltage level)
       //   delay(1000);
  else // wait for a second
  {
    digitalWrite(LED_BUILTIN, LOW);
  } // turn the LED off by making the voltage LOW
    //   delay(1000);

  Serial.print(x + 1);
}