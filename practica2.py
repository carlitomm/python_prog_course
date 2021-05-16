
try:
    bread = input("ingrese el numero de barras de pan vendidas que no son del dia \n")
    iva = input("ingrese el iva del producto\n")
    ieps = input("ingrese el ieps del producto\n")

    if float(bread) < 0 or float(iva) < 0 or float(ieps) < 0:
        raise ValueError

    price = float(iva) + float(ieps) + 17.55    #se calcula el precio por unidad
    print ("El precio de la barra de pan es : " + str(round(price ,2)))

    discount = price * 0.7                      #se calcula el descuento por undad de pan
    print ("Con un descuento de 70% queda con un precio de :" + str(round(discount,2)))

    total_sell = discount * float(bread)        #se calcula la cantidad vendida ya con descuento incluido
    print("sus ventas totales en el dia son de " + str(round(total_sell,2)) + "pesos \n")
except:
    print("-------ERROR, entrada incorrecta de datos--------")
