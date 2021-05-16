import tkinter
from tkinter import *
from time import sleep

from pyfirmata import Arduino, util, SERVO

import serial

board = Arduino('/dev/ttyUSB0')

sleep(5)
board.digital[4].mode = SERVO

def servo(posiciones):
    board.digital[4].write(posiciones)

def led_on():
    board.digital[13].write(1)

def led_off():
    board.digital[13].write(0)

root = Tk()

root.title('control de un servo')
root.minsize(300, 150)

# control de la barra
angulo = Scale(
    root,
    command = servo,
    from_ = 0,
    to = 180,
    orient = HORIZONTAL,
    length = 300,
    troughcolor = 'red',
    width = 30,
    cursor = 'dot',
    label = 'angulo del servo')

angulo.grid(column = 2, row = 1)

bon = Button(root, text = 'Led On', command = led_on)
bon.grid(column = 1, row = 3)

boff = Button(root, text = 'Led Off', command = led_off)
boff.grid(column = 3, row = 3)

root.mainloop()


