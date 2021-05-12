def ej1():
    import cv2

    # cv2.namedWindow('myCamera')
    vc = cv2.VideoCapture(0)

    while True:
        ret, frame = vc.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gauss = cv2.GaussianBlur(gray,(7,7), 1.5, 1.5)
        cam = cv2.Canny(gauss, 0, 30,3)

        cv2.imshow('myCamera',cam) 

        if cv2.waitKey(1000/12) & 0xff == ord("q"):
            break

    vc.release()
    cv2.destroyAllWindows()

def ej2():
    import numpy as np
    import cv2

    cap = cv2.VideoCapture(0)

    # definir los codecs
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('video.avi', fourcc, 60.0, (640,480))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            out.write(frame)
            cv2.imshow('myCam', frame)

            if cv2.waitKey(1000/12) & 0xff == ord("q"):
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()

def ej3():
    import cv2
    import numpy as np
    cap = cv2.VideoCapture(0)

    low_red1 = np.array([0,100,20], np.uint8)
    high_red1 = np.array([8,255,255], np.uint8)

    low_red2 = np.array([175,100,20], np.uint8)
    high_red2 = np.array([179,255,255], np.uint8)

    while True:
        ret, frame = cap.read()
        if ret == True:
            frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            maskread1 = cv2.inRange(frameHSV, low_red1, high_red1)
            maskread2 = cv2.inRange(frameHSV, low_red2, high_red2)
            maskRed = cv2.add(maskread1, maskread2)
            maskRedvis = cv2.bitwise_and(frame, frame, mask=maskRed)

            cv2.imshow('frame', frame)
            cv2.imshow('masked', maskRed)
            cv2.imshow('masked2', maskRedvis)

            if cv2.waitKey(1000/12) & 0xff == ord("q"):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()