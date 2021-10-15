from faceDefinicion import *
from grafics import *
import time

if __name__=='__main__':

    pantalla = initGrafics()
    caras=definicion_de_caras(centro,incrementoAngulo,escala)

    while not fin:
        backScreen(pantalla)
        
        imprimir_caras(pantalla, caras)

        #rotacion hacia la derecha
        for i in range(0,366,5):
            backScreen(pantalla)
            caras=definicion_de_caras(centro,i,escala)
            time.sleep(0.02)
            imprimir_caras(pantalla, caras)
            incrementoAngulo+=5
            print(incrementoAngulo)

        #rotacion hacia la izquierda
        for i in range(0,366,5):
            backScreen(pantalla)
            caras=definicion_de_caras(centro,incrementoAngulo,escala)
            time.sleep(0.02)
            imprimir_caras(pantalla, caras)
            pygame.display.flip()
            incrementoAngulo-=5
            print(incrementoAngulo)
        
        
        #aumentar escala
        for i in range(15):
            escala+=1
            backScreen(pantalla)
            caras=definicion_de_caras(centro,incrementoAngulo,escala)
            time.sleep(0.02)
            imprimir_caras(pantalla, caras)

        #reducir escala e invertir figura
        for i in range(115):
            escala-=1
            backScreen(pantalla)
            caras=definicion_de_caras(centro,incrementoAngulo,escala)
            time.sleep(0.02)
            imprimir_caras(pantalla, caras)
        
        #aumentar escala e invertir figura
        for i in range(100):
            escala+=1
            backScreen(pantalla)
            caras=definicion_de_caras(centro,incrementoAngulo,escala)
            time.sleep(0.02)
            imprimir_caras(pantalla, caras)
        
        #desplazamiento izuierda
        
        for i in range(0,200,5):
            backScreen(pantalla)
            unidades_traslacion[0]-=5
            caras = trasladar_caras_derecha(caras,[-5,0]) 
            direccion='izquierda'
            time.sleep(0.02)
            imprimir_caras(pantalla, caras)
        #desplazamiento derecha pasando por el centro
        for i in range(0,400,5):
            backScreen(pantalla)
            unidades_traslacion[0]+=5
            caras = trasladar_caras_derecha(caras,[5,0]) 
            direccion='derecha'
            time.sleep(0.02)
            imprimir_caras(pantalla, caras)
        
        #dezplazamiento a la izquierda para volver al centro
        for i in range(0,200,5):
            backScreen(pantalla)
            unidades_traslacion[0]-=5
            caras = trasladar_caras_derecha(caras,[-5,0]) 
            direccion='izquierda'
            time.sleep(0.02)
            imprimir_caras(pantalla, caras)

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                fin=True

    end()            
    print('fin de programa')