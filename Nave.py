import pygame
from Enemigos import Enemigos
from  Misil import Misil

class Nave:
    def __init__(self, x=200, y=500, vida=5):
        self.vida = vida
        self.angulo = 0
        self.x = x
        self.y = y
        self.altoNave = 40
        self.anchoNave = 40
        self.altoDibujado = 50
        self.anchoDibujado = 50
        self.current_frame = 0
        self.animation_delay = 5 
        self.misil = Misil(self.x, self.y)
        self.rect = pygame.Rect(self.x, self.y, self.anchoNave, self.altoNave)
        self.imagen = [pygame.image.load('/home/r3d/Documentos/galaxianShips/nave4.png'), pygame.image.load('/home/r3d/Documentos/galaxianShips/nave4.png'), pygame.image.load('/home/r3d/Documentos/galaxianShips/nave4.png'), pygame.image.load('/home/r3d/Documentos/galaxianShips/nave4.png')]
        for i in range(len(self.imagen)):
            self.imagen[i] = pygame.transform.scale(self.imagen[i], (self.anchoDibujado, self.altoDibujado))
        
    def obtener_imagen_actual(self):
        return self.imagen[self.current_frame]

    def actualizar_animacion(self):
        self.current_frame = (self.current_frame + 1) % len(self.imagen)


    def moverDer(self):
        if self.x > 600:
            self.x = 0
        self.x += 1.5
        self.rect.x = self.x

    def moverIzq(self):
        if self.x < 0:
            self.x = 600
        self.x -= 1.5
        self.rect.x = self.x
    
    def colision(self, enemigo):
        hitBoxNave = self.rect
        hitBoxEnemigo = pygame.Rect(enemigo.x, enemigo.y, enemigo.anchoEnemigo, enemigo.altoEnemigo)
        return hitBoxNave.colliderect(hitBoxEnemigo)
    
        