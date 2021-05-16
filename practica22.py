import pyfirmata2
import time
import sys,tty,termios
from pynput.keyboard import Key, Controller
import webbrowser
import datetime

# port = pyfirmata2.Arduino('/dev/ttyUSB5')
try:
    board = pyfirmata2.Arduino('/dev/ttyUSB0')
except:
    print("error opening the port")
board.samplingOn(100)

openweb = False
stillPressed = False

board.analog[0].enable_reporting()
file = open('record.txt', "a+")

print("presione el boton para abrir el navegador")
while True:
    time.sleep(0.1)
    if (board.analog[0].read() != None and board.analog[0].read() > 0.7 and stillPressed == False):
        openweb = True
        stillPressed = True
    
    if (board.analog[0].read() != None and board.analog[0].read() < 0.2): #checkeo de banderas para que solo se abra una vez la pagina
        stillPressed = False

    if openweb == True:
        openweb = False
        webbrowser.open_new_tab("https://youtu.be/FsW7nHsoHxo")
        file.write(str(datetime.datetime.now())+"\n")

# https://alumnosuacj-my.sharepoint.com/:v:/g/personal/al206563_alumnos_uacj_mx/EXXv069Td7VBlbnmAURiw9YBABMqu0Ghp_pASG0g-YIvJw