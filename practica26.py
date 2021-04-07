# graficar en python la señal enviada de arduino
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import serial
import collections

def getSerialData (self, Samples, serialConnection, lines, lineValueText, lineLabel):
    try:
        value = float(serialConnection.readline().rstrip())  
    except:
        value = -1
    finally:
        if value > 80:
            ax.set_facecolor('r')
        else: 
            ax.set_facecolor('g')
        data.append(value)
        lines.set_data(range(Samples),data)
        lineValueText.set_text(lineLabel + " = " + str(round(value,2)))

serialPort = '/dev/ttyUSB0'
baudRate = 9600

try:
    serialConnection = serial.Serial(serialPort, baudRate)
except Exception as e:
    print("error con el puerto serie")
    print(e)

Samples = 100
data = collections.deque([0]*Samples, maxlen=Samples)
sampleTime = 100

xmin = 0
xmax = Samples
ymin = 30
ymax = 130

fig = plt.figure(figsize=(13,6))
ax = plt.axes(xlim=(xmin,xmax), ylim=(ymin, ymax))
ax.set_xlabel("Tiempo")
ax.set_ylabel("Ritmo Cardiaco")

lineLabel = "ritmo simulado"
lines = ax.plot([],[], label=lineLabel)[0]
lineValueText = ax.text(0.85, 0.95,'', transform=ax.transAxes)


anim = animation.FuncAnimation(
    fig, 
    getSerialData, 
    fargs=(Samples, serialConnection, lines, lineValueText, lineLabel),
    interval = sampleTime
    )
plt.show()

serialConnection.close()

# https://alumnosuacj-my.sharepoint.com/:v:/g/personal/al206563_alumnos_uacj_mx/Eekgg9zO_UBJnbFiC03X59oB4_Zx1uwFhDVYSbRtO6dTFw


