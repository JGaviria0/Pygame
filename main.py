from definicionDeCaras import *
from graficos import *


if __name__ == '__main__':

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    unidades_traslacion[0] -= 5
                    caras = trasladar_caras(caras, [-5, 0])
                    direccion = 'izquierda'

                elif event.key == pygame.K_RIGHT:
                    unidades_traslacion[0] += 5
                    caras = trasladar_caras(caras, [5, 0])
                    direccion = 'derecha'

                elif event.key == pygame.K_DOWN:
                    escala -= 10
                    caras = definicion_de_caras(
                        centro, incrementoAngulo, escala)
                    caras = validar_direccion(
                        direccion, caras, unidades_traslacion)

                elif event.key == pygame.K_UP:
                    escala += 10
                    caras = definicion_de_caras(
                        centro, incrementoAngulo, escala)
                    caras = validar_direccion(
                        direccion, caras, unidades_traslacion)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    incrementoAngulo += 5
                    caras = definicion_de_caras(
                        centro, incrementoAngulo, escala)
                    caras = validar_direccion(
                        direccion, caras, unidades_traslacion)

                if event.button == 5:
                    incrementoAngulo -= 5
                    caras = definicion_de_caras(
                        centro, incrementoAngulo, escala)
                    caras = validar_direccion(
                        direccion, caras, unidades_traslacion)

    pygame.quit()
    print('fin de programa')
