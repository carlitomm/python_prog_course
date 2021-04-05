#!/usr/bin/env python

import serial
import matplotlib.pyplot as plt
import time
import collections
import matplotlib.animation as animation
import numpy as np

def getSerialData(self, Samples, serialConnection, lines, linesValuesText, lineLabel):
    value = float(serialConnection.readline().strip())
    data.append(value)
    lines.set_data(range(Samples),data)
    linesValuesText.set_text(lineLabel + '=' + str(round(value,2)))

serialPort = '/dev/ttyUSB0'
baudRate = 9600

try:
    serialConnection = serial.Serial(serialPort, baudRate)
except:
    print("error")

Samples = 100
data = collections.deque([0]*Samples, maxlen=Samples)
smapletime = 100

xmin = 0
xmax = Samples
ymin = 0
ymax = 6

fig = plt.figure(figsize= (13,6))
ax = plt.axes(xlim=(xmin,xmax), ylim(ylim,ymax))
ax.set_xlabels("Mustras")
ax.set_ylabels("Voltaje (V)")

lineLabel = "Voltaje"
lines = ax.plot([],[],label = lineLabel)[0]
linesValueText = ax.text(0.85, 0.95, '', transform = ax.transAxes)
anim = animation.FuncAnimation(fig, getSerialData, fargs=(Samples, lines, lineValueText, lineLabel), interval = sampleTime)




