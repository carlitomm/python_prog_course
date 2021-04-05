try:
    horas=int(input("\nIngrese la cntidad de horas trbajadas:\n"))
    pagoHora=float(input("ingrese el salario por hora de su empleado:\n"))

    if (horas < 0 or pagoHora < 0): # Si el usuario entra numero negativo levantamos manualmente un error
        raise TypeError

    horasExtra = 0  # inicializando la variable de horas extra para mostrar luego
    isr = 0         # inicializando la variable de isr

    # a continuación se calcula el subtotal de sueldo en dependencia de las horas trabajadas
    if horas <= 40:
        pagaMensual = horas * pagoHora
    else:                               #si se trabajaron horas extra se calcula la nomina segun las horas extra
        horasExtra = horas - 40
        if horasExtra <= 15:

            pagaMensual = (40 * pagoHora)
            pagaMensual = pagaMensual + 2*pagoHora*horasExtra

        else:
            pagaMensual = (40 * pagoHora) + 2 * pagoHora * 15
            ExtraExtraHoras = horas - 65
            pagaMensual = pagaMensual + ((3*pagoHora*ExtraExtraHoras) + (horas*pagoHora*0.15))

    # a continuación se calcula el isr segun el salario del empleado
    if ((pagaMensual > 8000) and (pagaMensual <= 13500)):
        isr = 0.1 * pagaMensual
    elif ((pagaMensual > 13500) and (pagaMensual <= 25000)):
        isr = 0.19 * pagaMensual
    elif pagaMensual > 25000:
        isr = 0.22 * pagaMensual

    #luego se calcula el total
    total = (pagaMensual - isr)

    #salida de datos
    print("Total de Horas: \t" + str(round(horas, 2))      + " h")
    print("Horas Extra:    \t" + str(round(horasExtra, 2)) + " h")
    print("Pago por Hora:  \t" + str(round(pagoHora,2))    + " pesos/h")
    print("Sub. de pago:   \t" + str(round(pagaMensual,2)) + " pesos")
    print("ISR:            \t" + str(round(isr,2))         + " pesos")
    print("Paga total      \t" + str(round(total, 2))      + " pesos")

#manejo de errores
except TypeError: #se maneja error de entrada de dats negativo
    print("---ERROR---Ingrese un numero positivo de horas y de pago por hora")
except:           #se maneja error genérico por si el usuario ingresa una letra 
    print("---ERROR---Entrada de datos Incorrecta")
finally:
    print("-----Su Programa ha Finalizado------\n")
