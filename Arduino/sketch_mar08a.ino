int datapin = 11;
int clockpin = 12;
int latchpin = 8;
byte layer1 = B00000001;
byte layer2 = B00000010;
byte layer3 = B00000100;
byte layer4 = B00001000;
byte layer5 = B00010000;
byte layer6 = B00100000;
byte layer7 = B01000000;
byte layer8 = B10000000;
float delayms = 1000/60;
byte blank = B00000000;
byte bytes[] = {blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,blank,B11111111};
byte layers[] = {layer1,layer2,layer3,layer4,layer5,layer6,layer7,layer8};

void setup() {
  // put your setup code here, to run once:
pinMode(datapin,OUTPUT);
pinMode(latchpin,OUTPUT);
pinMode(clockpin,OUTPUT);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
    for(int j=0;j<=8;j++){  
      digitalWrite(latchpin,LOW); 
      for(int i = (j*8);i<=((j+1)*8);i++){
        shiftOut(datapin,clockpin,MSBFIRST,bytes[i]);
      }
      shiftOut(datapin,clockpin,MSBFIRST,layers[j]);
      digitalWrite(latchpin,HIGH);
      delay(delayms/8);
    }
}
