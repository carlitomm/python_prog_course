import tkinter as tk
from tkinter import *
from time import sleep
import time
from pyfirmata import Arduino, util, SERVO

import serial

import threading

serialPort = '/dev/ttyUSB0'
baudRate = 9600

try:
    arduino = serial.Serial(serialPort, baudRate)
except Exception as e:
    print("error con el puerto serie")
    print(e)

sleep(5)

root = Tk()

root.title('control rgb')
root.minsize(350, 250)

motor = Label(root, text="motor detenido", font=("Helvetica", 18))
motor.place(x=125,y=115)

pir = Label(root, text="PIR Inactivo", font=("Helvetica", 18))
pir.place(x=20,y=155)

def continuo_ad():
        def iniciar():
            while(True):
                if arduino.in_waiting > 0:
                    now = time.strftime("%H:%M:%S")
                    data = arduino.readline()
                    data = str(data).strip()
                    print(data[2])
                    if data[2] == 'o':
                        motor.configure(text='motor en movimiento')
                        pir.configure(text='PIR activo: Se detecta alguien!!')
                    else:
                        motor.configure(text='motor detenido')
                        pir.configure(text='PIR inactivo: no hay nadie!!')

        
        thread1 = threading.Thread(target=iniciar)
        thread1.start()

continuo_ad()
   
motor.grid(column = 2, row = 1)
motor.grid(column = 2, row = 2)


root.mainloop()

# https://alumnosuacj-my.sharepoint.com/:v:/g/personal/al206563_alumnos_uacj_mx/ER6lnvAD3PlDqjzowWfmQmwBD27-a2IfDs_E3iW0FJ_7fw