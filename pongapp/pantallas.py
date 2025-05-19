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
        self.raqueta1 = Raqueta(10,ALTO//2)
        self.raqueta2 = Raqueta(ANCHO-10,ALTO//2)
        
        self.fuente = pg.font.Font(None,40)
        self.contadorDerecho=0
        self.contadorIzquierdo=0
        self.quienMarco= ""
    
        

    def bucle_fotograma(self):
        game_over = False
        while not game_over:
            self.tasa_refresco.tick(300)

            for eventos in pg.event.get():
                if eventos.type == pg.QUIT:
                    game_over = True

            self.raqueta1.mover(pg.K_w,pg.K_s)
            self.raqueta2.mover(pg.K_UP,pg.K_DOWN)
            self.quienMarco = self.pelota.mover()

            

            self.pantalla_principal.fill( (0,128,94 ) )
                                  
            self.mostra_linea_central()
           
            pg.draw.line(self.pantalla_principal,(255,255,255),(0,0),(0,600),10)
            pg.draw.line(self.pantalla_principal,(255,255,255),(800,0),(800,600),10)
            pg.draw.circle (self.pantalla_principal,(255,255,255), (400,300),60, width=0)
                        

            self.pelota.dibujar(self.pantalla_principal)
            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)
            

            self.pelota.comprobar_choque(self.raqueta1,self.raqueta2)
            #self.pelota.mostrar_marcador(self.pantalla_principal)

            self.mostrar_jugador()
            pg.display.flip()
        
        pg.quit()

    def mostrar_jugador(self):
        jugador1 = self.fuente.render("Jugador 1",0,ROJO)
        jugador2 = self.fuente.render("Jugador 2",0,ROJO)
        self.pantalla_principal.blit(jugador1,(150,20))
        self.pantalla_principal.blit(jugador2,(550,20))


    def mostra_linea_central(self):
        con_linea=0
        while con_linea <= 660:
            pg.draw.line(self.pantalla_principal,BLANCO,(ANCHO//2,con_linea),(ANCHO//2,con_linea+50),10)
            con_linea +=70

    def mostrar_marcador(self):
        jug_1= self.fuente.render(str(self.contadorIzquierdo), 0,(255,255,255))
        jug_2= self.fuente.render(str(self.contadorDerecho), 0,(255,255,255))
        self.pantalla_principal.blit(jug_1,(200,100))
        self.pantalla_principal.blit(jug_2,(600,100))


