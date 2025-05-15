import pygame as pg

class raqueta:
    def __init__(self,pos_x,pos_y,w=20,h=50,color=(255,255,255),vx=1,vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.w = w
        self.h = h 
        self.color = color
        self.vx = vx 
        self.vy = vy
    
    def dibujar(self,pantalla):
        pg.draw.rect(pantalla,self.color,(self.pos_x,self.pos_y,self.w,self.h))


class pelota:
    def __init__(self,pos_x,pos_y,color=(255,255,255),radio=20,vx=1,vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.radio = radio
        self.vx = vx 
        self.vy = vy
    
    def dibujar(self,pantalla):
        pg.draw.circle(pantalla,self.color,(self.pos_x,self.pos_y),self.radio)


    
