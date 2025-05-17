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
    
   

    pantalla_principal.fill( (12, 145, 215 ) )
    pg.draw.line(pantalla_principal,(255,255,255),(400,0),(400,600),10)
    pg.draw.line(pantalla_principal,(255,255,255),(0,0),(0,600),10)
    pg.draw.line(pantalla_principal,(255,255,255),(800,0),(800,600),10)

    pantalla_principal.blit(pg.font.SysFont("Arial", 36).render("Player 1", True, (255, 255, 255)), (50, 50))
    pantalla_principal.blit(pg.font.SysFont("Arial", 36).render("Player 2", True, (255, 255, 255)), (450, 50)) 
    pg.draw.circle (pantalla_principal,(255,255,255), (400,300),60, width=0)

    

    pelota.dibujar(pantalla_principal)
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)

    pelota.comprabar_choque(raqueta1,raqueta2)

    pelota.mostrar_marcador(pantalla_principal)

   
    pg.display.flip()

pg.quit()
