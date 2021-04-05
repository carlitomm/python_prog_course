dic = {}
file = open("mbox-short.txt",'r')

"""
llenamos las llaves del diccionario que son las direcciones email de los autores
"""
listaTemp = [] #lista usada para almacenar todos los autores temporalmente 
for line in file:
    if "From" in line:
        temp = line.split()
        listaTemp.append(temp[1])
        if not temp[1] in dic.keys():
            dic[temp[1]] = 0
            
"""
llenamos los valores del diccionario que corresponden a la cantidad de emails por autor
"""
for i in listaTemp:
    dic[i] += 1

print(dic)

"""
buscamos por el mayor autor
"""
authors = dic.keys()
gratest_value = 0   #numero de emails del mejor autor
author = ""         #nombre del mejor autor
for i in authors:
    if dic[i] > gratest_value:
        gratest_value = dic[i]
        author = i

print ("El autor con mayor número de emails mandados es " + author + " con " + str(gratest_value) + " emails enviados") 

# https://alumnosuacj-my.sharepoint.com/:v:/g/personal/al206563_alumnos_uacj_mx/EYznxDHB-oJCjVrRJgdx8vUBZtfMmrKMoWA9-KL9uRJuSA