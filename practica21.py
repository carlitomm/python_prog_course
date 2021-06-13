import pyfirmata2
import time
import sys,tty,termios
from pynput.keyboard import Key, Controller

# port = pyfirmata2.Arduino('/dev/ttyUSB5')
board = pyfirmata2.Arduino('/dev/ttyUSB6')
board.samplingOn(100)

def acordeon():
        board.digital[4].write(1)
        board.digital[5].write(0)
        board.digital[6].write(0)
        board.digital[7].write(1)
        time.sleep(0.1)
        board.digital[4].write(0)
        board.digital[5].write(1)
        board.digital[6].write(1)
        board.digital[7].write(0)
        time.sleep(0.1)

def rebote():

        board.digital[4].write(0)
        board.digital[5].write(1)
        board.digital[6].write(1)
        board.digital[7].write(1)
        time.sleep(0.1)
        board.digital[4].write(1)
        board.digital[5].write(0)
        board.digital[6].write(1)
        board.digital[7].write(1)
        time.sleep(0.1)
        board.digital[4].write(1)
        board.digital[5].write(1)
        board.digital[6].write(0)
        board.digital[7].write(1)
        time.sleep(0.1)
        board.digital[4].write(1)
        board.digital[5].write(1)
        board.digital[6].write(1)
        board.digital[7].write(0)
        time.sleep(0.1)
        # backward
        board.digital[4].write(1)
        board.digital[5].write(1)
        board.digital[6].write(0)
        board.digital[7].write(1)
        time.sleep(0.1)
        board.digital[4].write(1)
        board.digital[5].write(0)
        board.digital[6].write(1)
        board.digital[7].write(1)
        time.sleep(0.1)
        board.digital[4].write(0)
        board.digital[5].write(1)
        board.digital[6].write(1)
        board.digital[7].write(1)
        time.sleep(0.1)

print("Hello 🙂")
command=input(("Seleccione movimiento\n a: Acordeon \n r: Rebote  "))
board.analog[0].enable_reporting()
board.analog[1].enable_reporting()
while True:
    if command == 'a':
        if (board.analog[0].read() != None and board.analog[0].read() > 0.7):
            command='r'
        acordeon()
    elif command == 'r':
        if (board.analog[1].read() != None and board.analog[1].read() > 0.7):
            command='a'
        rebote()
    else:
        print("seleccione comando correcto")
