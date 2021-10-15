import pygame
from random import choice

VERDE = [0,255,0]
ROJO = [255,0,0]
AZUL = [0,0,255]
BLANCO = [255,255,255]
NEGRO = [0,0,0]
GRIS_CLARO =[212, 212, 212]
AMARILLO =[235, 255, 57]
PURPURA =[209, 57, 255]
ROSA = [255, 105, 210]
AZUL_CIELO = [105, 255, 235]
NARANJA = [250, 126, 68]
FUSIA = [255, 0, 128]
VERDE_FLUORESENTE =[208, 255, 0]
AZUL_OSCURO=[32, 95, 104]
ROSA_SUAVE=[236, 163, 163]
GRANATE= [155, 46, 13]
VERDE_BICHE=[32, 246, 3]
AMARILLO_OSCURO=[246, 222, 3]
ANCHO_VENTANA=800
ALTO_VENTANA=800

def backScreen(pantalla):
    pantalla.fill(NEGRO)

def imprimir_caras(pantalla, lista_de_caras):
    colores=[VERDE,ROJO,AZUL,BLANCO,GRIS_CLARO,AMARILLO,PURPURA,ROSA,AZUL_CIELO,NARANJA,FUSIA,VERDE_FLUORESENTE,AZUL_OSCURO,ROSA_SUAVE,GRANATE,VERDE_BICHE,AMARILLO_OSCURO]
    for cara in lista_de_caras:
        color=choice(colores)
        pygame.draw.polygon(pantalla, color, cara)
        del colores[colores.index(color)]
    pygame.display.flip()

def initGrafics():
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO_VENTANA,ALTO_VENTANA])
    pygame.display.flip()
    return pantalla

def end():
    pygame.quit()