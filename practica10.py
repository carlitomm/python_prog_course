def printer(number):
    for i in range(number,0,-1):
        for j in range(i,0,-1):
            print (j, end=" ")
        print("")

try:
    number = int(input("ingrese un numero "))
    printer(number)
except:
    print(".....ERROR...ups something went wrong!!!!")

# https://alumnosuacj-my.sharepoint.com/:v:/g/personal/al206563_alumnos_uacj_mx/Eesfp8a-DkJOnaXQj7hU1TQBgU4gkyExnVeD40nk2efJbQ