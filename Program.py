//Nama  : Nadya Shabirah Hardiono
//NIM   : 25/561895/SV/26673

//inisialisasi library
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>
#include <ESP32Servo.h>

int16_t gx, gy, gz;

Adafruit_MPU6050 mpu;
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;

//pin config
#define PIN_pir 13
#define PIN_servo1 19
#define PIN_servo2 18
#define PIN_servo3 5
#define PIN_servo4 17
#define PIN_servo5 12

void setup() {
  Serial.begin(115200);
  Wire.begin();
  
  //inisialisasi pin
  mpu.initialize();

  pinMode(PIN_pir, INPUT);
  servo1.attach(PIN_servo1);
  servo2.attach(PIN_servo2);
  servo3.attach(PIN_servo3);
  servo4.attach(PIN_servo4);
  servo5.attach(PIN_servo5);


  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_5_HZ);

  servo1.write(90);
  servo2.write(90);
  servo3.write(90);
  servo4.write(90);
  servo5.write(90);

}

void loop() {
  //mpu
  mpu.getGyroSensor(&gx, &gy, &gz)
  Serial.print(" X: "); Serial.print(x);
  Serial.print(" Y: "); Serial.print(y);
  Serial.print(" Z: "); Serial.println(z);


  servo1.write(gx);
  servo2.write(gx);
  servo3.write(gy);
  servo4.write(gy);
  servo5.write(gz);

  //deteksi gerakan melalui pir
  int movement = digitalRead(PIN_pir);

  if (movement == HIGH) {
    servo1.write(180);
    servo2.write(120);
    servo3.write(50);
    servo4.write(40);
    servo5.write(30);

    Serial.println("Terdeteksi gerakan");
    
  } else {
    servo1.write(90);
    servo2.write(90);
    servo3.write(90);
    servo4.write(90);
    servo5.write(90);
}
delay (100);
