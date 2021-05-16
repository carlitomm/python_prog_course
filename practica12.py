def prom_file():
    file = open("mbox-short.txt",'r')
    suma = 0
    count = 0

    for line in file:
        if "X-DSPAM-Confidence" in line:
            print(line)
            number = float(line[19:])
            suma += number
            count += 1
    prom = suma/count
    file.close()
    return prom

print(prom_file())
