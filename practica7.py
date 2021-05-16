def signo(birthYear):
    sign = birthYear%12
    return sign

try:
    year = int(input("ingrese el ano de su nacimiento "))
    CnSign = signo(year)
    if CnSign == 0:
        print("mono")
    elif CnSign == 1:
        print("Gallo")
    elif CnSign == 2:
        print("Perro")
    elif CnSign == 3:
        print("Cerdo")
    elif CnSign == 4:
        print("Rata")
    elif CnSign == 5:
        print("Buey")
    elif CnSign == 6:
        print("Tigre")
    elif CnSign == 7:
        print("Conejo")
    elif CnSign == 8:
        print("Dragon")
    elif CnSign == 9:
        print("Serpiente")
    elif CnSign == 10:
        print("Caballo")
    elif CnSign == 11:
        print("Cabra")
except:
    print("ingrese un año valido")

# https://alumnosuacj-my.sharepoint.com/:v:/g/personal/al206563_alumnos_uacj_mx/EfWAu-HJMydBmhIKHIPYjOsBfxG05XsCq4z--sWCXkPSyQ