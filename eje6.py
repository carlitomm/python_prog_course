def funcionPrint(n):
    while n >= 0:
        # print("%(n)d" %{"n":n})
        print(n, end =",")
        n = n - 1

n = int(input("Ingrese un numero "))
funcionPrint(n)
