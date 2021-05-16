def salario(horas, ra):
    if horas > 40:
        over = horas - 40
        pay = (40 * ra)+(float(over)*(ra*1.5))
        return pay
    else:
        pay = horas*ra
        return pay

horas = int(input("Ingrrese la cantidad de horas a traajar "))
ra = int(input("Ingrese el rate de salario a trabajar "))
print(salario(horas , ra))
