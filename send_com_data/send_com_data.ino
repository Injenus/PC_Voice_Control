#define voice_pin 2
#define radio_pin 3
#define led_pin 13

#define interval_voice_check 1
#define period_led 80

unsigned long timer_voice_check = 0;
unsigned long timer_led = 0;
unsigned long timer_virtual_press = 0;
byte led_state = 0;
byte val, val2;
int voice_value;
bool isVirtualPress = false;
bool isWarning = false;
void setup() {
  Serial.begin(115200);
  pinMode(radio_pin, INPUT_PULLUP);
  pinMode(voice_pin, INPUT);
  pinMode(led_pin, OUTPUT);
}

//void loop() {
//  if (millis() - timer_voice_check >= interval_voice_check) {
//    timer_voice_check = millis();
//    voice_value=digitalRead(voice_pin);
//  }
//
//  if (millis() - timer_virtual_press<=100 && isVirtualPress){
//    Serial.println('1');
//  }
//  else {
//    Serial.println('0');
//    isVirtualPress=false;
//  }
//
//  if (voice_value>0 && !isVirtualPress){
//    timer_virtual_press=millis();
//    isVirtualPress=true;
//  }
//}

void loop() {
  if (Serial.available() > 0) {
    byte incomingByte = Serial.read();  // Чтение принятого байта
    if (incomingByte == '1') {  // Если принято число 1
      isWarning = !isWarning;
    }
  }

  if (millis() - timer_led >= period_led) {
    timer_led = millis();
    if (isWarning) {
      digitalWrite(led_pin, led_state);
      if (led_state == 0) {
        led_state = 1;
      }
      else {
        led_state = 0;
      }
    }
  }

  if (millis() - timer_voice_check >= interval_voice_check) {
    timer_voice_check = millis();
    val = digitalRead(voice_pin);
    val2 = !digitalRead(radio_pin);
    //    Serial.print(millis());
    //    Serial.print(',');
    Serial.println(val + val2);
    if (!isWarning){
      digitalWrite(led_pin, val + val2);
    }
  }
}
