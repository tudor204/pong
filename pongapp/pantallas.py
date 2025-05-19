import pygame as pg
from pongapp.figura_class import Pelota,Raqueta
from .utils import *


class Partida:
    pg.init()
    def __init__(self):
        self.pantalla_principal=pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("Pong")
        self.tasa_refresco = pg.time.Clock()

        self.pelota = Pelota(ANCHO//2,ALTO//2)
        self.raqueta1 = Raqueta(ANCHO//2,ALTO//2)
        self.raqueta2 = Raqueta(ANCHO//2,ALTO//2)

    def bucle_fotograma(self):
        game_over = False
        while not game_over:
            self.tasa_refresco = pg.time.Clock()
        for eventos in pg.event.get():
            if eventos.type == pg.QUIT:
                 game_over = True

        self.raqueta1.mover(pg.K_w,pg.K_s)
        self.raqueta2.mover(pg.K_UP,pg.K_DOWN)
        self.pelota.mover()

        self.pantalla_principal.fill( (0,128,94 ) )
        pg.draw.line(self.pantalla_principal,(255,255,255),(400,0),(400,600),10)
        pg.draw.line(self.pantalla_principal,(255,255,255),(0,0),(0,600),10)
        pg.draw.line(self.pantalla_principal,(255,255,255),(800,0),(800,600),10)
        self.pantalla_principal.blit(pg.font.SysFont("Arial", 36).render("Player 1", True, (255, 255, 255)), (50, 50))
        self.pantalla_principal.blit(pg.font.SysFont("Arial", 36).render("Player 2", True, (255, 255, 255)), (450, 50)) 
        pg.draw.circle (self.pantalla_principal,(255,255,255), (400,300),60, width=0)

        

        self.pelota.dibujar(self.pantalla_principal)
        self.raqueta1.dibujar(self.pantalla_principal)
        self.raqueta2.dibujar(self.pantalla_principal)

        self.pelota.comprabar_choque(self.raqueta1,self.raqueta2)

        self.pelota.mostrar_marcador(self.pantalla_principal)

    
        pg.display.flip()
        
    pg.quit()

