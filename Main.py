import pygame
import sys
from Nave import Nave
from Misil import Misil
from Enemigos import Enemigos
from Vidas import Vidas
import random

pygame.init()

clock = pygame.time.Clock()
FPS = 130

ventanaAncho = 600
ventanaAlto = 600
ventana = pygame.display.set_mode((ventanaAlto, ventanaAncho))
pygame.display.set_caption("Space War")
fondo = pygame.image.load('/home/r3d/Documentos/galaxianShips/fondo.png')
fondo = pygame.transform.scale(fondo, (ventanaAlto, ventanaAncho))

blanco = (255,255,255)
negro = (0,0,0)
rosado_claro = (255, 182, 193)
verde_claro = (144, 238, 144)
amarillo_claro = (255, 255, 102)
rojo_claro = (255, 102, 102)

#SONIDOS
sonidoMisil = pygame.mixer.Sound("/home/r3d/Documentos/galaxianShips/sonidos/lazer2.wav")   #SONIDOS MISIL
musicaJuego = pygame.mixer.Sound("/home/r3d/Documentos/galaxianShips/sonidos/musicaJuego.wav")



class Juego:
    def __init__(self):
        self.nave = Nave()
        self.misil = None
        self.enemigos = []
        self.naveChoco = False
        self.misilChoco = False
        self.cartel = False
        self.vidas = Vidas(ventana, ventanaAlto, ventanaAncho)
        self.enemigoEliminado = []
        pygame.mixer.Sound.play(musicaJuego) #musica del juego
        for i in range(7):
            enemigo = Enemigos(random.randint(40, 560), -10)
            self.enemigos.append(enemigo)

    def avanzarEnemigo(self):
        if self.enemigos is not None:
            for enemigo in self.enemigos:
                enemigo.avanzar()
                if enemigo.fueraDePantalla() and enemigo is not None:
                    enemigo.reiniciarPos()

    def naveChocoEnemigo(self):
        for enemigo in self.enemigos:
            if self.nave.colision(enemigo) and not self.naveChoco:
                self.enemigoEliminado.append(enemigo)
                self.naveChoco = True
                self.nave.vida -= 1
                juego.mostrarVidaNave()       
        for enemigo in self.enemigoEliminado:
            if enemigo in self.enemigos:
                self.enemigos.remove(enemigo)
        self.naveChoco = False

    def ponerExplosion(self):
        for enemigo in self.enemigos:
            if self.nave.colision(enemigo):
                self.vidas.mostrarExplosion(self.nave)  

    def misilChocoEnemigo(self):
        if self.misil is not None and not self.misilChoco:
            for enemigo in self.enemigos:
                if self.misil is not None and self.misil.colisionMisil(enemigo):
                    self.misilChoco = True
                    self.misil = None
                    self.vidas.score += 1
                    self.enemigoEliminado.append(enemigo)
        for enemigo in self.enemigoEliminado:
            if enemigo in self.enemigos:
                self.enemigos.remove(enemigo)
        self.misilChoco = False

    def actualizar(self):
        self.avanzarEnemigo()
        self.naveChocoEnemigo()
        self.ponerExplosion()
        self.misilChocoEnemigo()

    def dispararMisil(self, teclas):
        if teclas[pygame.K_SPACE] and self.misil is None:   #MISIL
            self.misil = Misil(self.nave.x, self.nave.y)
            pygame.mixer.Sound.play(sonidoMisil)
        if self.misil is not None:
            self.misil.avanzar()
            if self.misil.fueraDePantalla():
                    self.misil = None

    def moverNave(self, teclas):
        if teclas[pygame.K_RIGHT]:
            self.nave.moverDer()
        if teclas[pygame.K_LEFT]:
            self.nave.moverIzq()

    def salirDelJuego(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.vidas.gameOver()
                pygame.quit()
                sys.exit()

    def noHayEnemigos(self):
        return len(self.enemigos) == 0
    
    def ganarJuego(self):
        if self.noHayEnemigos():
            self.vidas.win()

    def manejarEventos(self):
        teclas = pygame.key.get_pressed()
        self.vidas.scores()
        juego.ganarJuego()
        juego.salirDelJuego()
        juego.dispararMisil(teclas)
        juego.moverNave(teclas)
        
    def dibujar(self):
        ventana.blit(fondo, (0,0))
        if self.nave is not None:
            imagen_actual = self.nave.obtener_imagen_actual()
            ventana.blit(imagen_actual, (self.nave.x, self.nave.y))
            self.nave.actualizar_animacion()
        if self.misil is not None:
            ventana.blit(self.misil.imagen, (self.misil.x, self.misil.y))
        for enemigo in self.enemigos:
            ventana.blit(enemigo.imagen, (enemigo.x, enemigo.y))

    def mostrarVidaNave(self):
        self.vidas.mostrarVidas(juego, self.nave)
                

juego = Juego()

while True:
    juego.actualizar()
    juego.dibujar()
    juego.mostrarVidaNave()
    juego.manejarEventos()
    clock.tick(FPS)
    pygame.display.update()