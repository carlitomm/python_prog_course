
def DogAge2Human(dogAge, Size):
    humanAge = 0
    if Size == "small":
        humanAge = 16 + (dogAge * 4)
    elif Size == "medium":
        if dogAge < 6:
            humanAge = 16 + (dogAge * 4)
        elif dogAge == 6:
            humanAge = 42
        elif dogAge == 7:
            humanAge = 47
        elif dogAge == 8:
            humanAge = 50
        elif dogAge == 9:
            humanAge = 51
        elif dogAge == 10:
            humanAge = 60
        elif dogAge == 11:
            humanAge = 65
        elif dogAge == 12:
            humanAge = 69
    else:
        if dogAge < 6:
            humanAge = 16 + (dogAge * 4)
        elif dogAge == 6:
            humanAge = 45
        elif dogAge == 7:
            humanAge = 50
        elif dogAge == 8:
            humanAge = 55
        elif dogAge == 9:
            humanAge = 61
        elif dogAge == 10:
            humanAge = 66
        elif dogAge == 11:
            humanAge = 72
        elif dogAge == 12:
            humanAge = 77
        pass
    return humanAge

try:
    dogAge = int(input("ingrese la edadd del perro "))
    size =  (input("ingrese el tamaño del perro (small medium large)")).lower()
    if (size != "small" and size != "medium" and size != "large"):
         raise ValueError
    print(DogAge2Human(dogAge,size))
except:
    print("ingrese una edad y tamaño valido")

# https://alumnosuacj-my.sharepoint.com/:v:/g/personal/al206563_alumnos_uacj_mx/EWsT0RTjKy5IjtEZs4tW8l0BC-UL4RxIuBItewhzhhNdGw