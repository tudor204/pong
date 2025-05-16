import pygame as pg

class Raqueta:
    def __init__(self,pos_x,pos_y,w=20,h=120,color=(255,255,255),vx=1,vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.w = w
        self.h = h 
        self.color = color
        self.vx = vx 
        self.vy = vy
    
    def dibujar(self,pantalla):
        pg.draw.rect(pantalla,self.color,(self.pos_x-(self.w//2),self.pos_y-(self.h//2),self.w,self.h))

    def mover(self,tecla_arriba, tecla_abajo,y_max=600,y_min=0):
        
        estado_teclado = pg.key.get_pressed()
    
        if estado_teclado[tecla_arriba] == True and self.pos_y > y_min +(self.h/2):
            self.pos_y -=3

        if estado_teclado[tecla_abajo] == True and self.pos_y < y_max -(self.h/2):
            self.pos_y +=3
    @property
    def derecha(self):
        return self.pos_x + self.w//2
    @property
    def izquierda(self):
        return self.pos_x - self.w//2
    @property
    def arriba(self):
        return self.pos_y - self.h//2
    @property
    def abajo(self):
        return self.pos_y + self.h//2


class Pelota:
    def __init__(self,pos_x,pos_y,color=(255,255,255),radio=20,vx=1,vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.radio = radio
        self.vx = vx 
        self.vy = vy
        self.contadorDerecho=0
        self.contadorIzquierdo=0
    
    def dibujar(self,pantalla):
        pg.draw.circle(pantalla,self.color,(self.pos_x,self.pos_y),self.radio)

    def mover(self,x_max=800, y_max=600,x_min=0,y_min=0):
        self.pos_x += self.vx
        self.pos_y += self.vy
        if (self.pos_y >= y_max-self.radio) or (self.pos_y < y_min+self.radio):
            self.vy *= -1
        
        if self.pos_x >= x_max+self.radio*5: #limite derecho
            self.contadorIzquierdo +=1
            self.pos_x=x_max//2
            self.pos_y=y_max//2
            self.vx *= 1
            self.vy *= -1

        if self.pos_x < x_min-self.radio*5:#limite izquierdo
            self.contadorDerecho +=1
            self.pos_x=x_max//2
            self.pos_y=y_max//2
            self.vx *= -1
            self.vy *= 1
    
    def mostrar_marcador(self,pantalla):
        fuente = pg.font.Font(None, 40)
        jug_1= fuente.render(str(self.contadorIzquierdo), 0,(255,255,255))
        jug_2= fuente.render(str(self.contadorDerecho), 0,(255,255,255))
        pantalla.blit(jug_1,(200,50))
        pantalla.blit(jug_2,(600,50))
    

    @property
    def derecha(self):
        return self.pos_x + self.radio
    @property
    def izquierda(self):
        return self.pos_x - self.radio
    @property
    def arriba(self):
        return self.pos_y - self.radio
    @property
    def abajo(self):
        return self.pos_y + self.radio

        

    def comprabar_choque(self,r1,r2):
        #logica de choque
        if self.derecha >= r2.izquierda and\
            self.izquierda <= r2.derecha and\
            self.abajo >= r2.arriba and\
            self.arriba <= r2.abajo:
            self.vx *= -1

        if self.derecha >= r1.izquierda and\
            self.izquierda <= r1.derecha and\
            self.abajo >= r1.arriba and\
            self.arriba <= r1.abajo:
            self.vx *= -1

    def comprabar_choqueV2(self,*raquetas):
        for r in raquetas:
            if self.derecha >= r.izquierda and\
                self.izquierda <= r.derecha and\
                self.abajo >= r.arriba and\
                self.arriba <= r.abajo:
                self.vx *= -1
