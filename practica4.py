try:
    money = float(input("ingrese la cantidad de dinero depostado  ")) #dinero depositado

    if money < 0:
        raise TypeError
    #se calcula la taza de interes suponeindo interes compuesto
    frtYearSaves = (money + (money*6.25/100))
    sndYearSaves = (frtYearSaves + (frtYearSaves * 6.25/100)) #suponiendo que es interes compuesto
    trdYearSaves = (sndYearSaves + (sndYearSaves * 6.25/100))  #suponiendo que es interes compuesto

    print("con una cantidad inicial de: " + str(round(money,3)))
    print("se tienen ahorros de:")
    print(str(round(frtYearSaves,3)) + " pesos en el primer año")
    print(str(round(sndYearSaves,3)) + " pesos en el segundo año")
    print(str(round(trdYearSaves,3)) + " pesos en el tercer año ")
    print("durante los proximos 3 años\n")

except:  #ya sea una entrada de datos negativo como un caracter se maneja el mismo error
    print("-------ERROR, entrada incorrecta de datos--------")
