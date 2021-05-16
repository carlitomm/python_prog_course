for i in range(11):
    print("imprimo el numero",i)
try:
    print("Holo")
    print(1/0)
except ZeroDivisionError:
    print("Error divisioón por cero")
finally:
    print("el fianlly se ejecuta siempre")
