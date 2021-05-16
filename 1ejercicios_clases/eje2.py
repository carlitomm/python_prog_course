import numpy

nombre = input("ingresa tu nombre")
sexo = input("ingresa genero (H o M)")

if ((sexo.upper() is "M" and nombre[0].lower() < "M") or (sexo.upper() is "H" and nombre[0].lower() > "N")):
    print("you are in group A")
else:
    print("you are in group B")
