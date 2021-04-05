def euclides(larger, smallest):
    if (larger%smallest == 0):
        return smallest
    else:
        temp1 = int(larger/smallest)
        temp2 = smallest * temp1
        temp3 = larger - temp2
        return euclides(smallest, temp3)

# funcion recursiva del algoritmo de euclides
def EuclidesMCD(num1, num2):
    if num1 > num2:
        return euclides(num1, num2)
    elif num1 < num2:
        return euclides(num2, num1)
    else:
        return num1
def mcm(num1, num2):
    return num1*num2/euclides(num1, num2)
try:
    num1 = int(input("ingrese el numero 1 "))
    num2 = int(input("ingrese el numero 2 "))
    print ("el maximo comun divisor: " + str(euclides(num1, num2)) + "\nEl minimo comun multiplo: " + str(mcm(num1, num2)))
except:
    print(".....ERROR...ingrese numeros enteros")

# https://alumnosuacj-my.sharepoint.com/:v:/g/personal/al206563_alumnos_uacj_mx/Ecdy5jtvdudAv4X6wql4DCgBjzNvaobPoF_3NSWQnfnU9Q