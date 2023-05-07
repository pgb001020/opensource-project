#define SENSOR 8 //핀 설정(디지털신호 받는 핀)

void setup() {
  Serial.begin(9600);//PC모니터로 센서값을 확인하기위해서 시리얼 통신을 정의해줍니다.
  pinMode(SENSOR, INPUT);

}


void loop() {
 int shock = 0; // 충격량을 측정하여 시리얼 모니터에 표시해줍니다
    shock++;
    for(int i = 0;i<100;i++){
      delay(10);
      if(digitalRead(SENSOR))  shock++;
    }
    Serial.println(101-shock);
}
