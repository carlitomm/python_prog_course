# graficar en python la señal enviada de arduino
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import serial

def getSerialData(serialConnection):
    value = serialConnection.readline().rstrip()
    return value

serialPort = '/dev/ttyUSB0'
baudRate = 9600

try:
    serialConnection = serial.Serial(serialPort, baudRate)
except Exception as e:
    print("error con el puerto serie")
    print(e)

xmin = 0
xmax = 100
ymin = -1
ymax = 1

fig = plt.figure(figsize=(13,6))
ax = plt.axes(xlim=(xmin,xmax), ylim=(ymin, ymax))
ax.set_xlabel("muestras")
ax.set_ylabel("muestras")

lines = ax.plot([],[], label="hello")
while (True):
    print(getSerialData(serialConnection))

