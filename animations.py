from faceDefinicion import *
from grafics import *
import time

def animacion_rotacion(direccion,caras,incrementoAngulo,escala,pantalla,centro):
    for i in range(0,366,5):
        pantalla.fill(NEGRO)
        caras=definicion_de_caras(centro,incrementoAngulo,escala)
        time.sleep(0.02)
        imprimir_caras(pantalla,caras)
        pygame.display.flip()
        if direccion=='izquierda':
            incrementoAngulo+=5
        else:
            incrementoAngulo-=5
    return caras,incrementoAngulo


def animacion_escala(opcion,caras,incrementoAngulo,escala,pantalla,centro,unidades):
        print(centro)
        for i in range(unidades):
            if opcion=="aumentar":
                escala+=1
            else:
                escala-=1

            pantalla.fill(NEGRO)
            caras=definicion_de_caras(centro,incrementoAngulo,escala)
            time.sleep(0.02)
            imprimir_caras(pantalla,caras)
            pygame.display.flip()
        return caras,escala
    
def animacion_desplazamiento(direccion,unidades_traslacion,pantalla,caras,unidades):
        for i in range(0,unidades,5):
            pantalla.fill(NEGRO)
            unidades_traslacion[0]-=5
            if direccion=="derecha":
                caras = trasladar_caras(caras,[5,0]) 
            else:
                caras = trasladar_caras(caras,[-5,0]) 

            time.sleep(0.02)
            imprimir_caras(pantalla,caras)
            pygame.display.flip()
        return caras,unidades_traslacion

def animacion_rotacion_con_aumento(direccion,caras,escala,pantalla,incrementoAngulo,centro):
        for i in range(0,366,5):
            escala = escala +1 if i<183 else escala - 1
            pantalla.fill(NEGRO)
            caras=definicion_de_caras(centro,incrementoAngulo,escala)
            time.sleep(0.02)
            imprimir_caras(pantalla,caras)
            pygame.display.flip()
            if direccion=='izquierda':
                incrementoAngulo+=5
            else:
                incrementoAngulo-=5
            print(incrementoAngulo)
        
        return caras, incrementoAngulo, escala




if __name__=='__main__':

    pantalla = iniciar_graficos()
    centro = [400,400]
    incrementoAngulo=0
    unidades_traslacion=[0,0]
    escala=50
    caras = definicion_de_caras(centro, incrementoAngulo, escala)
    direccion = 'none'

    fin=False
    while not fin:
        pantalla.fill(NEGRO)
        
        imprimir_caras(pantalla, caras)
        #rotacion hacia la derecha
        caras,incrementoAngulo= animacion_rotacion('derecha',caras,incrementoAngulo,escala,pantalla,centro)
        #rotacion hacia la izquierda
        caras,incrementoAngulo= animacion_rotacion('izquierda', caras, incrementoAngulo, escala, pantalla,centro)
        #aumentar escala
        caras,escala= animacion_escala("aumentar", caras, incrementoAngulo, escala, pantalla,centro,15)
        #reducir escala e invertir figura
        caras,escala= animacion_escala('reducir', caras, incrementoAngulo, escala, pantalla, centro, 115)
        #aumentar escala e invertir figura
        caras,escala= animacion_escala('aumentar', caras, incrementoAngulo, escala, pantalla, centro, 100)
        #desplazamiento izuierda
        caras,unidades_traslacion= animacion_desplazamiento('izquierda', unidades_traslacion,pantalla, caras, 200)
        #desplazamiento derecha pasando por el centro
        caras,unidades_traslacion= animacion_desplazamiento('derecha', unidades_traslacion, pantalla, caras, 400)
        #dezplazamiento a la izquierda para volver al centro
        caras,unidades_traslacion= animacion_desplazamiento('izquierda', unidades_traslacion, pantalla, caras, 200)

        #rotacion con aumento de tamanio y disminucion hacia la izquierda
        caras,incrementoAngulo,escala= animacion_rotacion_con_aumento('izquierda', caras, escala, pantalla, incrementoAngulo, centro)
        #rotacion con aumento de tamanio y disminucion hacia la izquierda

        caras,incrementoAngulo,escala= animacion_rotacion_con_aumento('derecha', caras, escala, pantalla, incrementoAngulo, centro)

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                fin=True

    pygame.quit()          
    print('fin de programa')