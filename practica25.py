import serial 
from datetime import datetime
from datetime import date
def report2PFD(array):

    import time
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter

    now = datetime.now()
    fecha = now.strftime('%d-%m-%Y %H:%M:%S')

    c= canvas.Canvas(fecha+".pdf", pagesize=letter)
    c.setFont('Times-Roman', 12)
    c.setLineWidth(.3)

    for i in range(len(array)):
        c.drawString(30,750-i*15,str(i+1)+ " | " + array[i])
  


    c.showPage()
    c.save()

def getSerialData(serialConnection):
    value = serialConnection.readline().split()
    valuex = float(value[0])
    valuey = float(value[1])
    return valuex, valuey

serialPort = '/dev/ttyUSB0'
baudRate = 9600

try:
    serialConnection = serial.Serial(serialPort, baudRate)
except Exception as e:
    print("error con el puerto serie")
    print(e)

counter = 0
array = []
while True:
    data = getSerialData(serialConnection)
    if counter < 50:
        line = " x: " + str(data[0]) + ", y: " + str(data[1])
        array.append(line)
        counter += 1
    if counter == 50:
        report2PFD(array)
        counter += 1
    print(data)

# El sensor usado en arduino es un MPU6050 gyroscopio para medir las rotaciones en los ejes x,y 
# las mismas se almacenaron en un archivo pdf las primeras 50 tomadas. El nombre del fichero pdf es la fecha y la hora con la que fue creado.
# https://alumnosuacj-my.sharepoint.com/:v:/g/personal/al206563_alumnos_uacj_mx/EeCXbqNcGd1Jo9NfP2cCpnYBElWXPgckZznGQq1RmH03gA
