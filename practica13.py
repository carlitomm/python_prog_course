# se podria usar tambien el metodo "exists()" de la libreria "os" para verificar 
# que el archivo existe
try:
    file = open("conta.txt","x")
    file.write('0')
    file.close()
except:
    file= open("conta.txt", "r")
finally:
    try:
        file= open("conta.txt", "r")
        number = file.readline()
        while True:
            print (number)
            number = int(number)
            file.close()
            command = input("Ingrese el comando\n inc: incrementar\n dec: decrementar \n x: salir\n")
            if command == "inc":
                number += 1
            elif command == "dec":
                number -= 1
            elif command =='x':
                break
            file = open("conta.txt", "w")
            file.write(str(number))
    except: 
        print("Archivo corrupto")
file.close()