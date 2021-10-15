from faceDefinicion import *
from grafics import *


if __name__=='__main__':
    
    pantalla = initGrafics()
    caras=definicion_de_caras(centro,incrementoAngulo,escala)


    direccion='none'
    while not fin:
        backScreen(pantalla)
        
        imprimir_caras(pantalla, caras)
        

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                fin=True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    unidades_traslacion[0]-=5
                    caras = trasladar_caras_derecha(caras,[-5,0]) 
                    direccion='izquierda'
                    
                elif event.key == pygame.K_RIGHT:
                    unidades_traslacion[0]+=5
                    caras  = trasladar_caras_izquierda(caras,[5,0])
                    direccion='derecha'

                elif event.key == pygame.K_DOWN:
                    escala-=10
                    caras  = definicion_de_caras(centro, incrementoAngulo, escala)
                    caras=validar_direccion(direccion,caras, unidades_traslacion)


                elif event.key == pygame.K_UP:
                    escala+=10
                    caras = definicion_de_caras(centro, incrementoAngulo, escala)
                    caras=validar_direccion(direccion, caras, unidades_traslacion)
                    

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    incrementoAngulo+=5
                    caras=definicion_de_caras(centro,incrementoAngulo,escala)
                    caras=validar_direccion(direccion,caras, unidades_traslacion)
                    

                if event.button == 5:
                    incrementoAngulo-=5
                    caras=definicion_de_caras(centro,incrementoAngulo,escala)
                    caras=validar_direccion(direccion, caras, unidades_traslacion)

    end() 
    print('fin de programa')
    