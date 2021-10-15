import math

def validar_direccion(direccion,caras,unidades_traslacion):
    if direccion == "izquierda":
        return trasladar_caras(caras, unidades_traslacion)
    if direccion=="derecha":
        return trasladar_caras(caras, unidades_traslacion)
    return caras


def Traslacion(p,t):
    xp=p[0]+t[0]
    yp=p[1]+t[1]

    return [xp,yp]

def trasladar_caras(caras,unidades_traladar):
    Nuevas_caras = [[ Traslacion(punto, unidades_traladar) for punto in cara] for cara in caras]
    return Nuevas_caras

def Rotacion_h(p,r):
    r = math.radians(r)
    xp = (p[0]*math.cos(r))-(p[1]*math.sin(r))
    yp = (p[0]*math.sin(r))+(p[1]*math.cos(r))
    return[int(xp),int(yp)]

def Cartesiano_Pantalla(p,centro):
    xp=p[0] + centro[0]
    yp= -p[1] + centro[1]
    return [xp,yp]