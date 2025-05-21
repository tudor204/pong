import pygame as pg
from .pantallas import Menu, Partida, Resultado, Records
from .utils import *

class PantallaControlador:
    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((ANCHO,ALTO))
        self.menu = Menu()
        self.partida = Partida()
        self.resultado = Resultado()
        self.records = Records()

    def star(self):
        seguir = True
        while seguir:
            opcion = self.menu.bucle_pantalla()  # ✅ Leemos la opción seleccionada

            if opcion == "partida":
                self.partida = Partida()
                self.partida.bucle_pantalla()
                resultado_final = self.partida.fin_partida()

                if resultado_final:
                    self.resultado.cargarResultado(resultado_final)
                    self.resultado.bucle_pantalla()

            elif opcion == "records":
                self.records.bucle_pantalla()

            elif opcion is None:  # Por ejemplo si cierran la ventana
                seguir = False

        pg.quit()



        