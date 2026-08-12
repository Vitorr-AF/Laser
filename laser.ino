#include <ESP32Servo.h>

Servo servoHorizontal;
Servo servoVertical;

int anguloV = 90;
int anguloH = 90;

void mover_vertical(int modificador)
{
    anguloV = anguloV + modificador;
    
    if(anguloV > 180){
        anguloV = 180;
    }else if(anguloV < 0){
        anguloV = 0;
    }
    
    servoVertical.write(anguloV);
}


void mover_horizontal(int modificador)
{
    anguloH = anguloH + modificador;
    
    if(anguloH > 180){
        anguloH = 180;
    }else if(anguloH < 0){
        anguloH = 0;
    }

    servoVertical.write(anguloH);
}



void setup()
{
    Serial.begin(115200);
    servoHorizontal.attach(18);
    servoVertical.attach(19);

    servoVertical.write(anguloV);
    servoHorizontal.write(anguloH);
}

void loop()
{
    if (Serial.available())
    {
        String comando = Serial.readStringUntil('\n');

        if (comando.startsWith("VERTICAL:")) {
            int modificador = comando.substring(9).toInt();

            mover_vertical(modificador);
        }
        if (comando.startsWith("HORIZONTAL:")) {
            int modificador = comando.substring(11).toInt();

            mover_horizontal(modificador);
        }
    }
}