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
        
        self.fuente = pg.font.Font(FUENTE1,40)
        
        self.contadorDerecho=0
        self.contadorIzquierdo=0
        self.quienMarco = ""
        self.temporizador = TIEMPO
        self. game_over = False
        self.contadorFotograma =0 
        self.colorFondo=COLOR_CANCHA  

    def bucle_pantalla(self):
        
        #while not game_over and self.temporizador > 0 and self.contadorDerecho < 10 and self.contadorIzquierdo <10:
        while not self.game_over:
            salto_tiempo = self.tasa_refresco.tick(300)
            self.fin_partida()
            
            self.temporizador -= salto_tiempo
            
            for eventos in pg.event.get():
                if eventos.type == pg.QUIT:
                    self.game_over = True

            self.raqueta1.mover(pg.K_w,pg.K_s)
            self.raqueta2.mover(pg.K_UP,pg.K_DOWN)
            self.quienMarco = self.pelota.mover()

            color = self.fijar_fondo()
            self.pantalla_principal.fill( color=color )
                 
                             
            self.mostra_linea_central()
           
            pg.draw.line(self.pantalla_principal,(255,255,255),(0,0),(0,600),10)
            pg.draw.line(self.pantalla_principal,(255,255,255),(800,0),(800,600),10)
            pg.draw.circle (self.pantalla_principal,(255,255,255), (400,300),60, width=0)
                        

            self.pelota.dibujar(self.pantalla_principal)
            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)

            
                 
            

            self.pelota.comprobar_choque(self.raqueta1,self.raqueta2)
            self.mostrar_marcador()
            self.mostrar_temporizador()
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
        if self.quienMarco == "right":
                self.contadorDerecho += 1
        elif self.quienMarco == "left":
                self.contadorIzquierdo += 1

        jug_1= self.fuente.render(str(self.contadorIzquierdo), 0,(255,255,255))
        jug_2= self.fuente.render(str(self.contadorDerecho), 0,(255,255,255))
        self.pantalla_principal.blit(jug_1,(200,100))
        self.pantalla_principal.blit(jug_2,(600,100)) 

    def mostrar_temporizador(self):
        tiempo_juego=self.fuente.render(str(self.temporizador//1000),0,ROJO)
        rect_tiempo = tiempo_juego.get_rect(center=(400, 100))
        padding = 10  # Puedes cambiar este valor para más espacio
        rect_tiempo.inflate_ip(padding * 2, padding * 2)  # Aumenta ancho y alto
        # Dibujar el fondo con esquinas redondeadas
        pg.draw.rect(self.pantalla_principal, (0, 0, 0), rect_tiempo, border_radius=10)
        # Dibujar el borde blanco con las mismas esquinas redondeadas
        pg.draw.rect(self.pantalla_principal, (255, 255, 255), rect_tiempo, width=2, border_radius=10)
        # Dibujar el texto (usando el rect original sin padding)
        texto_rect = tiempo_juego.get_rect(center=(400, 100))
        self.pantalla_principal.blit(tiempo_juego, texto_rect)

    def fin_partida(self):
        if self.temporizador <= 0:
            self.game_over = True
            if self.contadorDerecho > self.contadorIzquierdo:
                return f"Gana el Jugador 2, resultado Jugador2:{self.contadorDerecho}, Jugador1:{self.contadorIzquierdo}"
            elif self.contadorDerecho < self.contadorIzquierdo:
                return f"Gana el Jugador 1, resultado Jugador1:{self.contadorIzquierdo}, Jugador2:{self.contadorDerecho}"
            else:
                return f"Empate entre Jugador 1 y Jugador 2, resultado Jugador1:{self.contadorIzquierdo}, Jugador2:{self.contadorDerecho}"

        if self.contadorDerecho == 3:
            self.game_over = True
            return "El ganador es el jugador 2"
        if self.contadorIzquierdo == 3:
            self.game_over = True
            return "El ganador es el jugador 1"

    def fijar_fondo(self):

        self.contadorFotograma += 1

        if self.temporizador > 10000:
             self.contadorFotograma = 0
        elif self.temporizador > 5000:
            if self.contadorFotograma == 60:
                if self.colorFondo == COLOR_CANCHA:
                     self.colorFondo = NARANJA
                else:
                    self.colorFondo = COLOR_CANCHA
                self.contadorFotograma=0
        else:
             if self.contadorFotograma == 50:
                if self.colorFondo == NARANJA:
                     self.colorFondo = ROJO_CLARO
                else:
                    self.colorFondo = NARANJA
                self.contadorFotograma=0   

        return self.colorFondo         

class Menu:
    pg.init()
    def __init__(self):
        self.pantalla_principal=pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("Menu")
        self.tasa_refresco=pg.time.Clock()
        self.imagenFondo = pg.image.load(FONDO1)
        self.fuenteMenu = pg.font.Font(FUENTEMENU,20)

    def bucle_pantalla(self):
        game_over=False
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True

            boton = pg.key.get_pressed()

            if boton[pg.K_r]== True:
                game_over = True
                return "records"
            if boton[pg.K_RETURN]== True:
                game_over = True
                return "partida"

            self.pantalla_principal.blit(self.imagenFondo,(0,0))
            jugar = self.fuenteMenu.render("Pulsa ENTER para jugar",0, ROJO)
            records = self.fuenteMenu.render("Pulsa R para ver pntuaciones",0, ROJO_CLARO)
                 
            self.pantalla_principal.blit(jugar,(200,ALTO//2))
            self.pantalla_principal.blit(records,(160,ALTO//2+40))

            pg.display.flip()
        pg.quit()


class Resultado:
    def __init__(self,resultado_final):
        pg.init()
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("Resultado")
        self.tasa_refresco = pg.time.Clock()
        self.fuenteResultado = pg.font.Font(FUENTEMENU,10)
        self.resultado_final = resultado_final

    def bucle_pantalla(self):
        game_over = False
        self.tasa_refresco.tick(380)
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True
            if evento.type == pg.KEYDOWN:
                game_over = True

            self.pantalla_principal.fill(BLANCO)
            resultado = self.fuenteResultado.render(self.resultado_final,0,ROJO)

            self.pantalla_principal.blit(resultado,(120,ALTO//2))

            pg.display.flip()

class Records:
    def __init__(self):
        pg.init()
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("Puntuación")
        self.tasa_refresco = pg.time.Clock()
        self.fuenteRecords = pg.font.Font(FUENTEMENU,10)

    def bucle_pantalla(self):
        game_over=False
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True

            self.pantalla_principal.fill(BLANCO)
            texto = self.fuenteRecords.render("Mejores puntuaciones",0, ROJO)
                 
            self.pantalla_principal.blit(texto,(230,ALTO//2))

            pg.display.flip()
        pg.quit()
        







    

    


        
