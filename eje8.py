list = []
dataIn = None

def printLowHigh(list):
    high = list[0]
    low = list[0]
    for i in range(len(list)):
        if i < low:
            low = list[i]
        if i > high:
            high = list[i]
    print (low, high)

def Promedio(list):
    suma = 0
    for i in range(len(list)):
        suma = suma + list[i]
    promedio = suma / len(list)
    return promedio


while True:
    dataIn=int(input("ingrese el valor "))
    if dataIn == -1:
        break
    list.append(int(dataIn))

printLowHigh(list)
print (Promedio(list))
