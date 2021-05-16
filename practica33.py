import cv2
import numpy as np

def figColor(imagenHSV):
    # red 
    rojoBajo1 = np.array([0,100,20],np.uint8)
    rojoAlto1 = np.array([10,255,255],np.uint8)
    rojoBajo2 = np.array([175,100,20],np.uint8)
    rojoAlto2 = np.array([180,255,255],np.uint8)

    #orange
    naranjaBajo = np.array([11,100,20],np.uint8)
    naranjaAlto = np.array([19,255,255],np.uint8)

    # yellow
    amarilloBajo = np.array([20,100,20],np.uint8)
    amarilloAlto = np.array([32,255,255],np.uint8)

    # verde
    verdeBajo = np.array([36,100,20],np.uint8)
    verdeAlto = np.array([70,255,255],np.uint8)

    # azul
    azulBajo = np.array([71,100,20],np.uint8)
    azulAlto = np.array([129,255,255],np.uint8)


    # violeta
    violetaBajo = np.array([130,100,20],np.uint8)
    violetaAlto = np.array([164,255,255],np.uint8)

    # rosa
    rosaBajo = np.array([165,50,20],np.uint8)
    rosaAlto = np.array([170,255,255],np.uint8)

    # gris
    grisBajo = np.array([0,0,0],np.uint8)
    grisAlto = np.array([255,5,30],np.uint8)

    # masks
    maskRojo1 = cv2.inRange(imagenHSV, rojoBajo1, rojoAlto1)
    maskRojo2 = cv2.inRange(imagenHSV, rojoBajo2, rojoAlto2)
    maskRojo = cv2.add(maskRojo1,maskRojo2)
    maskNaranja = cv2.inRange(imagenHSV, naranjaBajo, naranjaAlto)
    maskAmarillo = cv2.inRange(imagenHSV, amarilloBajo, amarilloAlto)
    maskVerde = cv2.inRange(imagenHSV, verdeBajo, verdeAlto)
    maskAzul = cv2.inRange(imagenHSV, azulBajo, azulAlto)
    maskVioleta = cv2.inRange(imagenHSV, violetaBajo, violetaAlto)
    maskRosa = cv2.inRange(imagenHSV, rosaBajo, rosaAlto)
    maskGris = cv2.inRange(imagenHSV, grisBajo, grisAlto)

    cntsRojo = cv2.findContours(maskRojo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    cntsNaranja = cv2.findContours(maskNaranja, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    cntsAmarillo = cv2.findContours(maskAmarillo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    cntsVerde = cv2.findContours(maskVerde, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    cntsAzul = cv2.findContours(maskAzul, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    cntsVioleta = cv2.findContours(maskVioleta, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    cntsRosa = cv2.findContours(maskRosa, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    cntsGris = cv2.findContours(maskGris, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    # print("===========colores contornos==========")
    # print(len(cntsRojo))
    # print(len(cntsNaranja))
    # print(len(cntsAmarillo))
    # print(len(cntsVerde))
    # print(len(cntsVioleta))
    # print(len(cntsRosa))

    color = ''
    if len(cntsRojo)>0: color='Rojo'
    elif len(cntsNaranja)>0: color='Naranja'
    elif len(cntsAmarillo)>0: color='Amarillo'
    elif len(cntsVerde)>0: color='Verde'
    elif len(cntsAzul)>0: color='Azul'
    elif len(cntsVioleta)>0: color='Violeta'
    elif len(cntsRosa)>0: color='Rosa'
    elif len(cntsGris)>0: color='Gris'

    return color

def figName(contorno,width,height):
    epsilon = 0.007*cv2.arcLength(contorno,True)
    approx = cv2.approxPolyDP(contorno,epsilon,True)
    namefig = ''
    print (len(approx))
    if len(approx) == 2:
        namefig = 'lineas'
    if len(approx) == 3:
        namefig = 'Triangulo'
    if len(approx) == 4:
        aspect_ratio = float(width)/height
        if aspect_ratio == 1:
            namefig = 'Cuadrado'
        else:
            namefig = 'Rectangulo'
    if len(approx) == 5:
        namefig = 'Pentagono'
    if len(approx) == 6:
        namefig = 'Hexagono'
    if len(approx) == 7:
        namefig = 'Flecha'
    if len(approx) == 8:
        aspect_ratio = float(width)/height
        if aspect_ratio >= 0.7 and aspect_ratio <= 1.3:
            namefig = 'estrella 4 puntas'
        else:
            namefig = 'Bandera'
    if len(approx) == 9:
        namefig = 'enagono'
    if len(approx) == 10:
        namefig = 'estrella 5 puntas'
    if len(approx) == 12:
        namefig = 'estrella 6 puntas'
    if len(approx) > 12:
        aspect_ratio = float(width)/height
        if aspect_ratio == 1:
            namefig = 'Circulo'
        else:
            namefig = 'Ovalo'
        

    return namefig

imagen = cv2.imread('figuras3.png')


gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 10,150)
canny = cv2.dilate(canny, None, iterations=1)
canny = cv2.erode(canny, None, iterations=1)
cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


imageHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

for c in cnts:
    if cv2.contourArea(c) > 50:
        x,y,w,h = cv2.boundingRect(c)
        imAux = np.zeros(imagen.shape[:2],dtype="uint8")
        imAux = cv2.drawContours(imAux,[c],-1,255,-1)
        maskHSV = cv2.bitwise_and(imageHSV, imageHSV, mask=imAux)
        name = figName(c,w,h)
        color = figColor(maskHSV)

        nameColor = name +' '+color
        cv2.putText(imagen, nameColor, (x,y-5), 1, 0.8, (0,255,0),1)
        cv2.imshow('ima',imagen)
        cv2.waitKey(0)