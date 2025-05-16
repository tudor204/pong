import pygame as pg 
from figura_class import Pelota,Raqueta

pg.init()

pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption("Pong")




#definir tasa de refresco de nuestro bucle de fotogramas, fps=fotograma por segundo
tasa_refresco = pg.time.Clock()



pelota = Pelota(400,300)
raqueta1 = Raqueta(10,300)
raqueta2 = Raqueta(790,300)


game_over = False

while not game_over:
    #obener la tasa de refresco en milisegundos
    valor_tasa = tasa_refresco.tick(300)#variables para controlar la velocidad entre fotogramas
    #print(valor_tasa)
    
    for eventos in pg.event.get():
        if eventos.type == pg.QUIT:
            game_over = True


    raqueta1.mover(pg.K_w,pg.K_s)
    raqueta2.mover(pg.K_UP,pg.K_DOWN)
    pelota.mover()
    #print("punto Derecho", pelota.contadorDerecho)
    #print("punto Izquierdo",pelota.contadorIzquierdo)
    
   

    pantalla_principal.fill( (0,128,94 ) )
    pg.draw.line(pantalla_principal,(255,255,255),(400,0),(400,600),10)
    
    pelota.dibujar(pantalla_principal)
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)

    #logica de choque
    if pelota.derecha >= raqueta2.izquierda and\
        pelota.izquierda <= raqueta2.derecha and\
        pelota.abajo >= raqueta2.arriba and\
        pelota.arriba <= raqueta2.abajo:
        pelota.vx *= -1

    if pelota.derecha >= raqueta1.izquierda and\
        pelota.izquierda <= raqueta1.derecha and\
        pelota.abajo >= raqueta1.arriba and\
        pelota.arriba <= raqueta1.abajo:
        pelota.vx *= -1

    pelota.mostrar_marcador(pantalla_principal)

   
    pg.display.flip()

pg.quit()
