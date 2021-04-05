from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib
from datetime import datetime
from datetime import date

# crear una instancia pra el objeto msge
msge = MIMEMultipart()
now = datetime.now()

# añadiendo un archivo adjunto
file = 'facturas.json'

fecha = now.strftime('%d-%m-%Y %H:%M:%S')

mensage = 'Echale ganas a la clase de progra o si on conacyt te qitara la beca ahora te adjunto un archivo' + ' ' + str(fecha)

# setup de los parametros del msge
password = "11235813Cmm*"
msge['From'] = "carlostestuacj@gmail.com"
msge['To'] = "carlostestuacj@gmail.com"
msge['Subject'] = "correo de prueba con adjunto"


# body of the message if i wanna send just a text
msge.attach(MIMEText(mensage, 'plain'))
msge.attach(MIMEText(file).read())

# coneccion con el servidor
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(msge['From'], password)

# enviar el msge al serviror
server.sendmail(msge['From'], msge['To'], msge.as_string())
server.quit()

print("se ha enviado el correo electronico a %s: " %msge['To'])