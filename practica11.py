frase = input("introduzca la frase ")
letra = input("introduzca la letra ")
counter = 0

for i in range(len(frase)):
    if frase[i] == letra:
        counter += 1

print("la letra " + letra + "aparece " + str(counter) + "en la frase")