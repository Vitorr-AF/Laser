import serial
import time

# Colocar porta do ESP
esp = serial.Serial("COM3", 115200)

time.sleep(2)


modificador = 10

# Código pra mandar comandos pro ESP
esp.write(f"VERTICAL:{modificador}\n".encode())
esp.write(f"HORIZONTAL:{modificador}\n".encode())