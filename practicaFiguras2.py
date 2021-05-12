import cv2
import numpy as np

def figColor(imageHSV):
    # red 
    redLow1 = np.array([0,100,20],np.uint8)
    redHigh1 = np.array([10,255,255],np.uint8)

    redLow2 = np.array([175,100,20],np.uint8)
    redHigh2 = np.array([180,255,255],np.uint8)

    #orange
    orangeLow1 = np.array([11,100,20],np.uint8)
    orangeHigh1 = np.array([19,255,255],np.uint8)

    # yellow
    yellowLow1 = np.array([20,100,20],np.uint8)
    yellowHigh1 = np.array([32,255,255],np.uint8)

    # verde
    verdeLow1 = np.array([36,100,20],np.uint8)
    verdeHigh1 = np.array([70,255,255],np.uint8)

    # violeta
    violetaLow1 = np.array([130,100,20],np.uint8)
    violetaHigh1 = np.array([145,255,255],np.uint8)

    # rosa
    rosaLow1 = np.array([146,100,20],np.uint8)
    rosaHigh1 = np.array([170,255,255],np.uint8)

    # masks
    maskRojo1 = cv2.inRange(imageHSV, redLow1, redHigh1)
    maskRojo2 = cv2.inRange(imageHSV, redLow2, redHigh2)
    maskRojo = cv2.add(maskRojo1,maskRojo2)

    maskorange1 = cv2.inRange(imageHSV, orangeLow1, orangeHigh1)

    maskyellow1 = cv2.inRange(imageHSV, yellowLow1, yellowHigh1)

    maskverde = cv2.inRange(imageHSV, verdeLow1, verdeHigh1)

    maskvioleta = cv2.inRange(imageHSV, violetaLow1, violetaHigh1)

    maskrosa = cv2.inRange(imageHSV, rosaLow1, rosaHigh1)

    cntsRojo = cv2.findContours(maskRojo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cntsnaranja = cv2.findContours(maskorange1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cntsamarillo = cv2.findContours(maskyellow1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cntsverde = cv2.findContours(maskverde, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cntsvioleta = cv2.findContours(maskvioleta, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cntsrosa = cv2.findContours(maskrosa, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    print(len(cntsnaranja))

    color = ''
    if len(cntsRojo)>0: color='Rojo'
    elif len(cntsnaranja)>0: color='orange'
    elif len(cntsamarillo)>0: color='amarillo'
    elif len(cntsverde)>0: color='verde'
    elif len(cntsvioleta)>0: color='violeta'
    elif len(cntsrosa)>0: color='rosa'
    else: color = 'no color'

    return color

def figName(contorno,width,height):
  epsilon = 0.01*cv2.arcLength(contorno,True)
  approx = cv2.approxPolyDP(contorno,epsilon,True)
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
  if len(approx) > 10:
    namefig = 'Circulo'
  return namefig

image = cv2.imread('/home/carlos/Documents/UACJ_prog_avanzada/MicrosoftTeams-image.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 10,150)
canny = cv2.dilate(canny, None, iterations=1)
canny = cv2.erode(canny, None, iterations=1)
cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    imAux = np.zeros(image.shape[:2],dtype="uint8")
    imAux = cv2.drawContours(imAux,[c],-1,-255,-1)
    maskHSV = cv2.bitwise_and(imageHSV, imageHSV, mask=imAux)
    name = figName(c,w,h)
    color = figColor(maskHSV)

    nameColor = name +' '+color
    cv2.putText(image, nameColor, (x,y-5), 1, 1.5, (0,255,0),2)
cv2.imshow('ima',image)
cv2.waitKey(0)

