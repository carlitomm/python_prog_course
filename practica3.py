import numpy as np
try:
    peso = float(input("ingrese su peso en kg \n"))        # se pide el peso en Kg
    estatura = float(input("ingrese su estatura en metros")) # se pide la estatura en m

    if peso < 0 or estatura <0:
        raise TypeError

    imc = peso/pow(estatura,2)                          #se calcula el indice de masa corporal

    print("Tu índice de masa corporal es " + str(round(imc,2)))

except ZeroDivisionError:
    print("---ERROR---ingresada una estatura nula")
except TypeError:
    print("---ERROR---ingresados numeros negativos")
except:
    print("---ERROR---entrada incorrecta de datos--------")
finally:
    print("---PROGAMA FINALIZADO---")
