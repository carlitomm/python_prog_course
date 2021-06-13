
import serial

class serialConect:
    def __init__(self):
        serialPort = '/dev/ttyUSB0'
        baudRate = 9600

        try:
            self.serialConnection = serial.Serial(serialPort, baudRate)
        except Exception as e:
            print("error con el puerto serie")
            print(e)
    
    def getSerialData(self):
        value = self.serialConnection.readline().split()
        humidity = float(value[0])
        temperatue = float(value[1])
        return humidity, temperatue

def sendEmail():
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.application import MIMEApplication

    import smtplib
    from datetime import datetime
    from datetime import date

    try:
        # crear una instancia pra el objeto msge
        msge = MIMEMultipart()
        now = datetime.now()

        # añadiendo un archivo adjunto
        file = 'Temp_humP24.txt'
       
        with open(file, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name="Temp_humP24.txt"
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename=Temp_humP24.txt' 
        msge.attach(part)

        fecha = now.strftime('%d-%m-%Y %H:%M:%S')
        mensage = 'Adjunto le envio 15 mediciones de humedad y temperatura' + ' ' + str(fecha)

        # setup de los parametros del msge
        password = "11235813Cmm*"
        msge['From'] = "carlostestuacj@gmail.com"
        msge['To'] = "cmiguelezmachado@gmail.com"
        msge['Subject'] = "practica24 mediciones de temperatura y humedad"
        
        # body of the message if i wanna send just a text
        msge.attach(MIMEText(mensage, 'plain'))
        msge.attach(part)

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

def write_file(humidity, temperatue):
    file = open("Temp_humP24.txt",'a+')
    print("La humedad es de " + str(humidity) + "%, y la temeratur de " + str(temperatue) + "ºC ")
    file.write("La humedad es de " + str(humidity) + " %, y la temeratur de " + str(temperatue) + " ºC \n")
    file.close()
Sc = serialConect()

for i in range(15):
    humidity, temperatue = Sc.getSerialData()
    write_file(humidity, temperatue)

sendEmail()


    
