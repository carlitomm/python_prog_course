import tkinter as tk
from tkinter import *
from time import sleep
import time
from pyfirmata import Arduino, util, SERVO

import serial

import threading

serialPort = '/dev/ttyUSB1'
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

text = Label(root, text="Door closed", font=("Helvetica", 18))
text.place(x=125,y=115)

date = Label(root, text="", font=("Helvetica", 18))
date.place(x=125,y=155)

def continuo_ad():
        def iniciar():
            while(True):
                if arduino.in_waiting > 0:
                    now = time.strftime("%H:%M:%S")
                    data = arduino.readline()
                    data = str(data).strip()
                    print(data[2])
                    if data[2] == 'o':
                        text.configure(text='Door opened')
                        date.configure(text='at: ' +now)
                    else:
                        text.configure(text='Door closed')

        
        thread1 = threading.Thread(target=iniciar)
        thread1.start()

continuo_ad()
    
# text.grid(column = 2, row = 1)


root.mainloop()

# https://alumnosuacj-my.sharepoint.com/:v:/g/personal/al206563_alumnos_uacj_mx/EfdZ7GZmzUhOjEQKHPQOY6IBr6yUQuoAdUokIid2dD6Liw