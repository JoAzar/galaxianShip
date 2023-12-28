import pygame
import sys

class Vidas():
    def __init__(self, ventana, ventanaAlto, ventanaAncho):
        self.ventana = ventana
        self.ventanaAlto = ventanaAlto
        self.ventanaAncho = ventanaAncho
        self.vida = pygame.image.load('/home/r3d/Documentos/galaxianShips/corazon.png')
        self.vida = pygame.transform.scale(self.vida, (40, 40))

        self.vidaRota = pygame.image.load('/home/r3d/Documentos/galaxianShips/corazonRoto.png')
        self.vidaRota = pygame.transform.scale(self.vidaRota, (40, 40))

        self.explosion = pygame.image.load('/home/r3d/Documentos/galaxianShips/explosion.png')
        self.explosion = pygame.transform.scale(self.explosion, (190, 190))

        self.score = 0

    def scores(self):
        fuente = pygame.font.Font(None, 25)
        posicionTexto = (510, 260)    #vida de la nave
        textoSuperficie = fuente.render("SCORE: "+ str(self.score), True, (253, 253, 253))
        self.ventana.blit(textoSuperficie, posicionTexto)
        pygame.display.update()


    def mostrarVidas(self, juego, nave):
        fuente = pygame.font.Font(None, 35)
        posicionTexto = (nave.x, nave.y+60)    #vida de la nave
        if nave.vida == 5:
            textoSuperficie = fuente.render("", True, (172, 214, 93))
            self.ventana.blit(textoSuperficie, posicionTexto)
            self.ventana.blit(self.vida, (560, 300))
            self.ventana.blit(self.vida, (560, 360))
            self.ventana.blit(self.vida, (560, 420))
            self.ventana.blit(self.vida, (560, 480))
            self.ventana.blit(self.vida, (560, 540)) 
                                                        
        if  nave.vida == 4:
            textoSuperficie = fuente.render("", True, (69, 69, 69))
            self.ventana.blit(textoSuperficie, posicionTexto)
            self.ventana.blit(self.vidaRota, (560, 300))
            self.ventana.blit(self.vida,     (560, 360))
            self.ventana.blit(self.vida,     (560, 420))
            self.ventana.blit(self.vida,     (560, 480))
            self.ventana.blit(self.vida,     (560, 540)) 

        if nave.vida == 3:
            textoSuperficie = fuente.render("", True, (231, 80, 29))
            self.ventana.blit(textoSuperficie, posicionTexto)
            self.ventana.blit(self.vidaRota, (560, 300))
            self.ventana.blit(self.vidaRota, (560, 360))
            self.ventana.blit(self.vida,     (560, 420))
            self.ventana.blit(self.vida,     (560, 480))
            self.ventana.blit(self.vida,     (560, 540))

        if nave.vida == 2:
            textoSuperficie = fuente.render("", True, (231, 80, 29))
            self.ventana.blit(textoSuperficie, posicionTexto)
            self.ventana.blit(self.vidaRota, (560, 300))
            self.ventana.blit(self.vidaRota, (560, 360))
            self.ventana.blit(self.vidaRota, (560, 420))
            self.ventana.blit(self.vida,     (560, 480))
            self.ventana.blit(self.vida,     (560, 540)) 

        if nave.vida == 1:
            textoSuperficie = fuente.render("", True, (231, 80, 29))
            self.ventana.blit(textoSuperficie, posicionTexto)
            self.ventana.blit(self.vidaRota, (560, 300))
            self.ventana.blit(self.vidaRota, (560, 360))
            self.ventana.blit(self.vidaRota, (560, 420))
            self.ventana.blit(self.vidaRota, (560, 480))
            self.ventana.blit(self.vida,     (560, 540)) 
        
        if nave.vida == 0:
            textoSuperficie = fuente.render("", True, (231, 80, 29))
            self.ventana.blit(textoSuperficie, posicionTexto)
            self.ventana.blit(self.vidaRota, (560, 300))
            self.ventana.blit(self.vidaRota, (560, 360))
            self.ventana.blit(self.vidaRota, (560, 420))
            self.ventana.blit(self.vidaRota, (560, 480))
            self.ventana.blit(self.vidaRota, (560, 540)) 
            self.gameOver()

    def mostrarExplosion(self, nave):
        fuente = pygame.font.Font(None, 35)
        posicionTexto = (nave.x, nave.y+30)    #vida de la nave
        textoSuperficie = fuente.render("", True, (231, 80, 29))
        self.ventana.blit(textoSuperficie, posicionTexto)
        self.ventana.blit(self.explosion, (350, 450))

    def gameOver(self):
        fuente2 = pygame.font.Font(None, 60)
        posicionTexto2 = (self.ventanaAlto//3, self.ventanaAncho//2-50)    #de la salida
        textoSuperficie2 = fuente2.render("GAME OVER", True, ( 255, 177, 51 ), None)
        self.ventana.blit(textoSuperficie2, posicionTexto2)
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

    def win(self):
        fuente2 = pygame.font.Font(None, 60)
        posicionTexto2 = (self.ventanaAlto//3, self.ventanaAncho//2-50)    #de la salida
        textoSuperficie2 = fuente2.render("¡GANASTE!", True, ( 255, 177, 51 ), None)
        self.ventana.blit(textoSuperficie2, posicionTexto2)
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()
