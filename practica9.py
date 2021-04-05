def dec2bin(number):
    bin = ""
    if number == 0:
        return "0"
    while number > 0:
        bin = bin + (str(number%2))
        number = int(number / 2)
    return bin[::-1]

try:
    number = int(input("ingrese el numero a convertir "))
    print (dec2bin(number))
except:
    print(".....ERROR...ingrese un numero entero")

# https://alumnosuacj-my.sharepoint.com/:v:/g/personal/al206563_alumnos_uacj_mx/EUJUj7VVHQVHvXrDWYs2DJYB412bbZZkbi-RXDY7K2o_yw
