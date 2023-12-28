
import pygame
import random

class Enemigos:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.altoEnemigo = 40
        self.anchoEnemigo = 40
        self.altoDibujado = 40
        self.anchoDibujado = 40
        self.rect = pygame.Rect(self.x, self.y, self.anchoEnemigo, self.altoEnemigo)
        self.imagen = pygame.image.load('/home/r3d/Documentos/galaxianShips/ovni.png')
        self.imagen = pygame.transform.scale(self.imagen, (self.anchoDibujado, self.altoDibujado))

    def avanzar(self):
        self.y += 1.3
        self.rect.y = self.y

    def fueraDePantalla(self):
        return self.y > 600

    def reiniciarPos(self):
        self.y = 0
        self.x = random.randint(40, 560)
