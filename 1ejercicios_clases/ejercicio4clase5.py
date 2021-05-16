arc = input("ingrese el nombre del archivo: \n")
try:
    file = open(arc)
except:
    print('Error en la apertura del archivo')
    exit()
lista = list()

for linea in file:
    palabra = linea.rstrip().split()
    for dato in palabra:
        if dato in lista:
            continue
        else:
            lista.append(dato)

lista.sort()
print (lista)