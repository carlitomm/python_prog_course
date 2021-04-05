import numpy

age = int(input("ingresa tu edad: "))

try:
    if age > 18:
        print("es mayor de edad")
    else:
        print("es menor de edad")
except TypeError:
    print("You entered a wrong tyoe of data")
finally:
    print("Thid code was escecuted correctly :)")
