import serial
import time
import pygame

# Colocar porta do ESP
esp = serial.Serial("COM3", 115200)

time.sleep(2)

velocidade = 20

# Código pra mandar comandos pro ESP (modificador é em graus)
def mover_vertical(modificador):
    esp.write(f"VERTICAL:{modificador}\n".encode())

def mover_horizontal(modificador):
    esp.write(f"HORIZONTAL:{modificador}\n".encode())



pygame.init()
pygame.joystick.init()



while True:
    pygame.event.pump()
    if pygame.joystick.get_count() > 0:

        if controle is None:
            controle = pygame.joystick.Joystick(0)
            controle.init()
        eixo_x = controle.get_axis(0)
        eixo_y = controle.get_axis(1)

        if eixo_x > 0.5 or eixo_x < -0.5:
            mover_horizontal(int(velocidade * eixo_x))
        if eixo_y > 0.5 or eixo_y < -0.5:
            mover_vertical(int(velocidade * eixo_y))
    else:
        controle = None
    time.sleep(0.05)