import cv2

image = cv2.imread('/home/carlos/Documents/UACJ_prog_avanzada/MicrosoftTeams-image.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 10,150)
canny = cv2.dilate(canny, None, iterations=1)
canny = cv2.erode(canny, None, iterations=1)

cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in cnts:
    epsilon = 0.01 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)
    # print(len(approx))
    x,y,w,h = cv2.boundingRect(approx)
    if len(approx) == 3:
        cv2.putText(image, 'tringle', (x,y-5), 1, 1.5, (0,255,0),2)
    if len(approx) == 4:
        aspect_ratio = float(w)/h
        if (aspect_ratio) == 1:
            cv2.putText(image, 'cuadrado', (x,y-5), 1, 1.5, (0,255,0),2)
        else:
            cv2.putText(image, 'rectangulo', (x,y-5), 1, 1.5, (0,255,0),2)
    if len(approx) == 5:
        cv2.putText(image, 'pentagono', (x,y-5), 1, 1.5, (0,255,0),2)
    if len(approx) == 6:
        cv2.putText(image, 'hexagono', (x,y-5), 1, 1.5, (0,255,0),2)
    if len(approx) > 10:
        cv2.putText(image, 'circulo', (x,y-5), 1, 1.5, (0,255,0),2)

    cv2.drawContours(image, [approx], 0, (0,255,0), 2)

    cv2.imshow('gray',image)
cv2.waitKey(0)