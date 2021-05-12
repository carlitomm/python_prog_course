import cv2
import numpy as np

cap = cv2.VideoCapture('terminal.mp4')

# fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
# fgbg = cv2.BackgroundSubtractorMOG2()
# fgbg = cv2.BackgroundSubtractorKNN()
fgbg = cv2.createBackgroundSubtractorMOG2()

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

while True:

    ret, frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    cv2.rectangle(frame,(0,0),(frame.shape[1],40),(0,0,0),-1)
    color = (0,255,255)
    text_estado = 'no movment'

    area_pts =np.array([[240,320],[480,320],[620,frame.shape[0]],[50,frame.shape[0]]])

    imAux = np.zeros(shape=(frame.shape[:2]),dtype=np.uint8)
    imAux = cv2.drawContours(imAux, [area_pts], -1,(255),-1)
    image_area = cv2.bitwise_and(gray, gray, mask=imAux)

    fgmask = fgbg.apply(image_area)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel) #morph_open limpia la imagen
    fgmask = cv2.dilate(fgmask, None, iterations = 0)

    cnts = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for cnt in cnts:
        if cv2.contourArea(cnt)>500:
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),2)
            text_estado = 'hay movimiento'
            color = (255,255,0)


    # visualizar el area
    cv2.drawContours(frame,[area_pts],-1,color,2)

    cv2.putText(frame, text_estado,(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,color,2)

    if ret is False: break
    cv2.imshow('frame', frame)
    # cv2.imshow('other', image_area)

    k = cv2.waitKey(70) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()