import numpy

is_vegeterian = int(input("es su pizza vegeteriana \nTipos de pizza \n\t1-Vegetariana \n\t2-Normal"))

if is_vegeterian == 1:
    ingrediante = int(input("ingredientes de pizza Vegeteraina \n\t1-Pimeinto \n\t2-Tofu \n"))
    print("la pizza vegetariana con mozarella, tomate y", end="")
    if (ingrediante == 1):
        print("piminto")
    else:
        print("Tofu")
else:
    ingrediante = int(input("ingredientes de pizza Vegeteraina \n\t1-Bacon \n\t2-Jamon \n\t3-queso"))
    print("la pizza con mozarella, tomate y ", end="")
    if ingrediante == 1:
        print("Bacon")
    elif ingrediante == 2:
        print("Jamon")
    else:
        print("queso")
