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
# board.digital[4].mode = SERVO
red = '00'
green = '00'
blue = '00'

int_red = 0
int_green = 0
int_blue = 0

def red_sat(sat):
    global red
    global int_red
    int_red = int(sat)
    red=str(hex(int(sat)))
    red = red[2:]
    if (len(red) == 1):
        red = '0' + red 
    red_color= '#' + red + green + blue
    root.configure(bg=red_color)

    # arduino.write(str.encode(red_color))
  

def green_sat(sat):
    global green
    global int_green
    int_green = int(sat)
    green=str(hex(int(sat)))
    green = green[2:]
    if (len(green) == 1):
        green = '0' + green 
    green_color='#'+ red + green + blue
    root.configure(bg=green_color)

    # arduino.write(str.encode(green_color))

def blue_sat(sat):
    global blue
    global int_blue
    int_blue = int(sat)
    blue=str(hex(int(sat)))
    blue = blue[2:]
    if (len(blue) == 1):
        blue = '0' + blue
    blue_color='#'+ red + green + blue
    root.configure(bg=blue_color)

    # arduino.write(str.encode(blue_color))
    


root = Tk()

root.title('control rgb')
root.minsize(350, 250)
root.configure(bg='#'+red+green+blue)

# control de la barra
red_scale = Scale(
    root,
    command = red_sat,
    from_ = 0,
    to = 255,
    orient = HORIZONTAL,
    length = 300,
    troughcolor = 'red',
    width = 30,
    cursor = 'dot',
    label = 'red')

green_scale = Scale(
    root,
    command = green_sat,
    from_ = 0,
    to = 255,
    orient = HORIZONTAL,
    length = 300,
    troughcolor = 'green',
    width = 30,
    cursor = 'dot',
    label = 'green')

blue_scale = Scale(
    root,
    command = blue_sat,
    from_ = 0,
    to = 255,
    orient = HORIZONTAL,
    length = 300,
    troughcolor = 'blue',
    width = 30,
    cursor = 'dot',
    label = 'blue')

def continuo_ad():
        def iniciar():
            while(True):
                # print(b'#'+str.encode(red+green+blue))
                # arduino.write(str.encode(red+green+blue))
                arduino.write(b'r')
                arduino.write(str.encode(str(int_red)))
                # time.sleep(0.5)

                arduino.write(b'g')
                arduino.write(str.encode(str(int_green)))
                # time.sleep(0.5)

                arduino.write(b'b')
                arduino.write(str.encode(str(int_blue)))
                time.sleep(0.5)
        
        thread1 = threading.Thread(target=iniciar)
        thread1.start()

continuo_ad()
    
red_scale.grid(column = 2, row = 1)
green_scale.grid(column = 2, row = 2)
blue_scale.grid(column = 2, row = 3)



root.mainloop()

# https://alumnosuacj-my.sharepoint.com/:v:/g/personal/al206563_alumnos_uacj_mx/EUK2taZRqFBNuhjrdYehR8QBsuxsfh9pM5Wj7aXwHzL1xQ