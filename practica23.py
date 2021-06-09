import serial

def sendEmail():
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    import smtplib
    from datetime import datetime
    from datetime import date

    try:
        # crear una instancia pra el objeto msge
        msge = MIMEMultipart()
        now = datetime.now()

        fecha = now.strftime('%d-%m-%Y %H:%M:%S')
        mensage = 'Aguien se acerco mucho al sensor!!!! ' + ' ' + str(fecha)

        # setup de los parametros del msge
        password = ""
        msge['From'] = ""
        msge['To'] = ""
        msge['Subject'] = "practica23"


        # body of the message if i wanna send just a text
        msge.attach(MIMEText(mensage, 'plain'))

        # coneccion con el servidor
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(msge['From'], password)

        # enviar el msge al serviror
        server.sendmail(msge['From'], msge['To'], msge.as_string())
        server.quit()

        print("se ha enviado el correo electronico a %s: " %msge['To'])
    
    except Exception as e:
        print("ocurrio algun error en el envio del correo")
        print(e)
        

def getSerialData(serialConnection):
    value = float(serialConnection.readline().strip())
    return value

serialPort = '/dev/ttyUSB0'
baudRate = 9600

try:
    serialConnection = serial.Serial(serialPort, baudRate)
except:
    print("error")


while True:
    data = getSerialData(serialConnection)
    if data < 10 and data != -1:
        print("sending email")
        sendEmail()







