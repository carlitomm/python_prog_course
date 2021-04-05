import pyfirmata2
import time
import sys,tty,termios
from pynput.keyboard import Key, Controller

# port = pyfirmata2.Arduino('/dev/ttyUSB5')
board = pyfirmata2.Arduino('/dev/ttyUSB6')
board.samplingOn(100)

def multimetro(value):
    if value <= 1.25:
        board.digital[4].write(1)
        board.digital[5].write(1)
        board.digital[6].write(1)
        board.digital[7].write(1)
    elif value > 1.25 and value <= 2.5:
        board.digital[4].write(0)
        board.digital[5].write(1)
        board.digital[6].write(1)
        board.digital[7].write(1)
    elif value > 2.5 and value <= 3.75:
        board.digital[4].write(0)
        board.digital[5].write(0)
        board.digital[6].write(1)
        board.digital[7].write(1)
    elif value > 3.75 and value <= 4.8:
        board.digital[4].write(0)
        board.digital[5].write(0)
        board.digital[6].write(0)
        board.digital[7].write(1)
    elif value > 4.8:
        board.digital[4].write(0)
        board.digital[5].write(0)
        board.digital[6].write(0)
        board.digital[7].write(0)



board.analog[0].enable_reporting()
while True:
    if (board.analog[0].read() == None):
        continue
    else:
        value = board.analog[0].read()*5
        print(value)
        multimetro(value)

# https://alumnosuacj-my.sharepoint.com/:v:/g/personal/al206563_alumnos_uacj_mx/EbDN9s4W2g9Evh_aFtYZsGABmqnI32v_mRtIlOU8AoWuSg