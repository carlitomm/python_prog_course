data = input("ingrese un valor de temperatura en grados Fahenhaith ")
try:
    fahr = float(data)
    tc = (fahr - 32.0) * (5/9)
    print("la temperatura en grados centrigrados es "+ str(tc))
except TypeError:
    print("error en el tipo de dato ingresado, ingrese un numero")
except ValueError:
    print("error ingrese un numero")
