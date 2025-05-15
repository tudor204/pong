import pygame as pg 
from figura_class import pelota,raqueta

pg.init()

pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption("Pong")

pelota = pelota(400,300)
raqueta1 = raqueta(0+20,300-(50/2))
raqueta2 = raqueta(800-30,300-(50/2))


game_over = False

while not game_over:
    
    for eventos in pg.event.get():
        if eventos.type == pg.QUIT:
            game_over = True

    pantalla_principal.fill( (0,128,94 ) )
    pg.draw.line(pantalla_principal,(255,255,255),(400,0),(400,600),10)
    
    pelota.dibujar(pantalla_principal)
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)

    pg.display.flip()

pg.quit()
