import json

############### pagar factura ######################3
def pay_factura(dic, key, current_debt):
    current_debt += dic[key]
    dic.pop(key)
    values = dic.values()
    print("=============================================")
    print("La cantidad Cobrada en la sesión actual es de: " + str(current_debt))
    print("La cantidad a Cobrar ahora es de: " + str(sum(values)))
    print("=============================================")
    return current_debt, dic

############## añadir factura ###############3
def add_factura(dic, key, value):
    dic[key] = value
    values = dic.values()
    print("=============================================")
    print("La cantidad Cobrada en la sesión actual es de: " + str(current_debt))
    print("La cantidad a Cobrar ahora es de: " + str(sum(values)))
    print("=============================================")
    return dic

########### salvar y cargar el diccionario en un archivo json ###########
def save_dict(dic):
    file = open("facturas.json", "w")
    json.dump(dic, file)
    file.close()

def load_dict():
    file = open("facturas.json", "r")
    dic = json.load(file)
    print(dic)
    file.close()
    return dic

################ IMPRIMIR el diccionario ##########
def print_dict(dic):
    print("=============================================")
    print(dic)
    print("=============================================")


######################### MAIN #######################
if __name__ == '__main__': 
    current_debt = 0
    try:
        dic = load_dict()
    except:
        print("archivo corrupto o removido. creando nuevo archivo")
        dic = dict()
    try:
        while True:
            opt = input("Ingrese la opcion \n 1-Pagar factura \n 2-Agregar factura \n 3-Listar facturas \n x-para salir \n")
            
            if opt =='1':
                key = input("Ingrese el numero de la factura a pagar ")
                current_debt, dic = pay_factura(dic, key, current_debt)
                save_dict(dic)
            elif opt == '2':
                key = input("Ingrese el numero de la factura ")
                try:
                    val = float(input("Ingrese el valor de la factura "))
                except Exception as e:
                    print(e)
                dic = add_factura(dic, key, val)
                save_dict(dic)
            elif opt == '3':
                print_dict(dic)
            elif opt == 'x':
                break
            else:
                print("Ingrese la opción adecuada")

    except Exception as e:
        print(e)

# video https://alumnosuacj-my.sharepoint.com/:v:/g/personal/al206563_alumnos_uacj_mx/EXP20_16SMFDs85-0-kpYtMByGzh0xHnDuE9hdCf9Tywuw