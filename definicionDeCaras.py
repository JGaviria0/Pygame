from utilidades import *

def definicion_de_caras(centro,grados_extra,escala):

    angulo45=45+grados_extra
    angulo90=90+grados_extra
    angulo225=225+grados_extra
    angulo135=135+grados_extra
    angulo270=270+grados_extra
    angulo315=315+grados_extra



    # figura 1

    p1 = [escala*2, 0]
    p1_rot = Rotacion_h(p1, angulo45)
    p1_trans = Cartesiano_Pantalla(p1_rot, centro)

    p2 = [escala, 0]
    p2_rot = Rotacion_h(p2, angulo90)
    p2_trans = Cartesiano_Pantalla(p2_rot, p1_trans)

    p3 = [escala*2, 0]
    p3_rot = Rotacion_h(p3, angulo225)
    p3_trans = Cartesiano_Pantalla(p3_rot, p2_trans)

    p4 = [escala*2, 0]
    p4_rot = Rotacion_h(p4, angulo135)
    p4_trans = Cartesiano_Pantalla(p4_rot, p3_trans)

    p5 = [escala, 0]
    p5_rot = Rotacion_h(p5, angulo270)
    p5_trans = Cartesiano_Pantalla(p5_rot, p4_trans)

    p6 = [escala*2, 0]
    p6_rot = Rotacion_h(p6, angulo315)
    p6_trans = Cartesiano_Pantalla(p6_rot, p5_trans)

    # Techo figura 1

    p7 = [escala, 0]
    p7_rot = Rotacion_h(p7, angulo135)
    p7_trans = Cartesiano_Pantalla(p7_rot, p2_trans)

    p8 = [escala, 0]
    p8_rot = Rotacion_h(p8, angulo225)
    p8_trans = Cartesiano_Pantalla(p8_rot, p7_trans)

    p9 = [escala, 0]
    p9_rot = Rotacion_h(p9, angulo135)
    p9_trans = Cartesiano_Pantalla(p9_rot, p8_trans)

    # Figura 2

    p10 = [escala, 0]
    p10_rot = Rotacion_h(p9, angulo90)
    p10_trans = Cartesiano_Pantalla(p10_rot, p7_trans)

    p11 = [escala, 0]
    p11_rot = Rotacion_h(p11, angulo225)
    p11_trans = Cartesiano_Pantalla(p11_rot, p10_trans)

    p12 = [escala, 0]
    p12_rot = Rotacion_h(p12, angulo135)
    p12_trans = Cartesiano_Pantalla(p12_rot, p11_trans)


    # Techo figura 2

    p13 = [escala, 0]
    p13_rot = Rotacion_h(p13, angulo135)
    p13_trans = Cartesiano_Pantalla(p13_rot, p10_trans)


    # figura 3

    p14 = [escala, 0]
    p14_rot = Rotacion_h(p14, angulo90)
    p14_trans = Cartesiano_Pantalla(p14_rot, p13_trans)

    p15 = [escala*2, 0]
    p15_rot = Rotacion_h(p15, angulo225)
    p15_trans = Cartesiano_Pantalla(p15_rot, p14_trans)

    p16 = [escala, 0]
    p16_rot = Rotacion_h(p16, angulo270)
    p16_trans = Cartesiano_Pantalla(p16_rot, p15_trans)

    p17 = [escala, 0]
    p17_rot = Rotacion_h(p17, angulo225)
    p17_trans = Cartesiano_Pantalla(p17_rot, p16_trans)

    p18 = [escala*2, 0]
    p18_rot = Rotacion_h(p18, angulo270)
    p18_trans = Cartesiano_Pantalla(p18_rot, p17_trans)

    # Techos figura 3

    p19 = [escala, 0]
    p19_rot = Rotacion_h(p19, angulo135)
    p19_trans = Cartesiano_Pantalla(p19_rot, p14_trans)

    p20 = [escala*2, 0]
    p20_rot = Rotacion_h(p20, angulo225)
    p20_trans = Cartesiano_Pantalla(p20_rot, p19_trans)

    p21 = [escala, 0]
    p21_rot = Rotacion_h(p21, angulo270)
    p21_trans = Cartesiano_Pantalla(p21_rot, p20_trans)

    p22 = [escala, 0]
    p22_rot = Rotacion_h(p22, angulo225)
    p22_trans = Cartesiano_Pantalla(p22_rot, p21_trans)

    p23 = [escala*2, 0]
    p23_rot = Rotacion_h(p23, angulo270)
    p23_trans = Cartesiano_Pantalla(p23_rot, p22_trans)

    #Figura 4

    p24 = [escala*2, 0]
    p24_rot = Rotacion_h(p24, angulo315)
    p24_trans = Cartesiano_Pantalla(p24_rot, p14_trans)

    p25 = [escala, 0]
    p25_rot = Rotacion_h(p25, angulo270)
    p25_trans = Cartesiano_Pantalla(p25_rot, p24_trans)

    p26 = [escala, 0]
    p26_rot = Rotacion_h(p26, angulo315)
    p26_trans = Cartesiano_Pantalla(p26_rot, p25_trans)

    p27 = [escala*2, 0]
    p27_rot = Rotacion_h(p27, angulo270)
    p27_trans = Cartesiano_Pantalla(p27_rot, p26_trans)

    # Figura3 Techo

    p28 = [escala, 0]
    p28_rot = Rotacion_h(p28, angulo45)
    p28_trans = Cartesiano_Pantalla(p28_rot, p14_trans)

    p29 = [escala*2, 0]
    p29_rot = Rotacion_h(p29, angulo315)
    p29_trans = Cartesiano_Pantalla(p29_rot, p28_trans)

    p30 = [escala, 0]
    p30_rot = Rotacion_h(p30, angulo270)
    p30_trans = Cartesiano_Pantalla(p30_rot, p29_trans)

    p31 = [escala, 0]
    p31_rot = Rotacion_h(p31, angulo315)
    p31_trans = Cartesiano_Pantalla(p31_rot, p30_trans)

    p32 = [escala*2, 0]
    p32_rot = Rotacion_h(p32, angulo270)
    p32_trans = Cartesiano_Pantalla(p32_rot, p31_trans)
    

    #Arreglos de cada cara.

    cara1 = [centro, p1_trans, p2_trans, p3_trans]
    cara2 = [p3_trans, p4_trans, p5_trans, p6_trans ]
    cara3 = [p2_trans, p3_trans, p4_trans, p9_trans, p8_trans, p7_trans]
    cara4 = [p7_trans, p8_trans, p11_trans, p10_trans]
    cara5 = [p8_trans, p9_trans, p12_trans, p11_trans]
    cara6 = [p10_trans, p11_trans, p12_trans, p13_trans]
    cara7 = [p5_trans, p4_trans, p9_trans, p12_trans, p13_trans, p14_trans, p15_trans, p16_trans, p17_trans, p18_trans]
    cara8 = [p19_trans, p20_trans, p15_trans, p14_trans]
    cara9 = [p20_trans, p21_trans, p16_trans, p15_trans]
    cara10 = [p23_trans, p22_trans, p17_trans, p18_trans]
    cara11 = [p22_trans, p21_trans, p16_trans, p17_trans]
    cara12 = [p13_trans, p14_trans, p24_trans, p25_trans, p26_trans, p27_trans, p1_trans, p2_trans, p7_trans, p10_trans]
    cara13 = [p14_trans, p28_trans, p29_trans, p24_trans]
    cara14 = [p25_trans, p30_trans, p29_trans, p24_trans]
    cara15 = [p25_trans, p30_trans, p31_trans, p26_trans]
    cara16 = [p27_trans, p32_trans, p31_trans, p26_trans]

    caras = [cara1, cara2, cara3, cara4, cara5, cara6,cara7, cara8, cara9, cara10, cara11, cara12, cara13, cara14, cara15, cara16]
    return caras