def fromC2F(tempCent):
    tempFaren = (tempCent * 9/5) + 32
    return tempFaren

def fromF2C(tempFaren):
    tempCent = (tempFaren - 32) * 5/9
    return tempCent

tempFaren = int(input("ingrese la temperatura en grados Faren "))
temp = 0
file = open("tempFile.txt", "w")
while temp <= tempFaren:
    value = fromF2C(temp)
    print(value)
    file.write(str(temp) + "F" + "\t |\t" + str(value)+ "C" + "\n")
    temp += 10
    
file.close()