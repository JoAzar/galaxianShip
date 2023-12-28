import pygame

class Misil:
    def __init__(self, x, y):
            self.x = x
            self.y = y
            self.anchoMisil = 50
            self.altoMisil = 50
            self.anchoDibujado = 40
            self.altoDibujado = 50
            self.rect = pygame.Rect(self.x, self.y, self.anchoMisil, self.altoMisil)
            self.imagen = pygame.image.load('/home/r3d/Documentos/galaxianShips/misil2.png')
            self.imagen = pygame.transform.scale(self.imagen, (self.anchoDibujado, self.altoDibujado))

    def avanzar(self):
        self.y -= 3
        self.rect.y = self.y

    def colisionMisil(self, enemigo):
        hitBoxMisil = self.rect
        hitBoxEnemigo = pygame.Rect(enemigo.x, enemigo.y, enemigo.anchoEnemigo, enemigo.altoEnemigo)
        return hitBoxMisil.colliderect(hitBoxEnemigo)
    
    def fueraDePantalla(self):
        return self.rect.y < -0
