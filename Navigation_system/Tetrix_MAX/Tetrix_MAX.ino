/*
  |X|X|X|X|
  |X|X|X|X|
  |X|X|X|X|
  |X|X|X|X|

  1 = move Forward
  2 = move Left
  3 = move Right
  4 = move Backward

*/

#include <PRIZM.h>
#include <SoftwareSerial.h>
#define rxPin 9
#define txPin 2
int motorPower = 50;
String inputString = "";

PRIZM prizm;
SoftwareSerial Btmodule (rxPin, txPin);
void setup() {
  pinMode(rxPin, INPUT);
  pinMode(txPin, OUTPUT);
  Serial.begin(9600);
  Btmodule.begin(9600);
  prizm.PrizmBegin();
  prizm.setMotorInvert(1, 1);
}


void moveFront() {
  Serial.println("moveFront");
  Btmodule.write("moveFront");
  prizm.resetEncoders();
  prizm.setMotorTargets(360, 1440, 360, 1440);
}

void moveBack() {
  Serial.println("moveBack");
  Btmodule.write("moveBack");
  prizm.resetEncoders();
  prizm.setMotorTargets(-360, -1440, -360, -1440);
}

void rotateLeft() {
  Serial.println("rotateLeft");
  Btmodule.write("rotateLeft");
  prizm.resetEncoders();
  prizm.setMotorTargets(360, -1380, 360, 1380);
  //prizm.setMotorDegrees(180, 360, 180, -360);
  //  prizm.setMotorTargets(360, -1300, 360, -1300);

}

void rotateRight() {
  Serial.println("rotateRight");
  Btmodule.write("rotateRight");
  prizm.resetEncoders();
  prizm.setMotorTargets(360, 1300, 360, -1300);
  //prizm.setMotorDegrees(-180, 360, -180, -360);
}


void loop() {
  while (Btmodule.available() > 0) {
    char c = Btmodule.read();
    if (isdigit(c)) {
      Serial.print("inside is digit : ");
      Serial.println(c);
      inputString += c;
    }
  }
  if (inputString.length() > 0) {
    Serial.print("I received: ");
    Serial.print(inputString);
    Serial.println();
    for (int i = 0; i < inputString.length(); i++) {
      char c = inputString.charAt(i);
      if (c == '1') {
        moveFront();
      }
      else if (c == '2') {
        rotateLeft();
      }
      else if (c == '3') {
        rotateRight();
      }
      else if (c == '4') {
        moveBack();
      }
      else if (c == '9') {
        Serial.println("exit");
        }
    }
    inputString = "";
  }
}
