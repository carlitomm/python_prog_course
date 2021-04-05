import sqlite3

conn = sqlite3.connect('base.sqlite')
cur = conn.cursor()

name = input("ingrese nombre")
last = input("ingrese appellido")
phone = input("ingrese telefono")
email = input("ingrese correo")

cur.execute('INSERT INTO Usuarios(Nombre, Apellido, Telefono, Correo) VALUES(?,?,?,?)', (name, last, phone, email))
conn.commit()

print("los datos de la base de datos son")
cur.execute('SELECT ID, Nombre, Apellido, Telefono FROM Usuarios')

for fila in cur:
    print(fila)
