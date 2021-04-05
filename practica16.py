def name_changer(lista): #funcion para realizar el campbio de la ext del archivo
    ind = 0
    for i in lista:
        temp = i.split('.') #dividimos el archivo de su ext
        if temp[1] == 'hpp':
            lista[ind] = temp[0]+'.h'
        ind += 1 


filenames=["program.c","stdio.hpp","sample.hpp","a.out","math.hpp","hpp.out","yata.hpp","arriba_el_ame.hpp"]

print()
print("la lista inicial era ", filenames)
print()

name_changer(filenames)

print("la lista con las ext. cambiadas es ", filenames)
print()