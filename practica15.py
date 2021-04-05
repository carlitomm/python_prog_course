file = open("mbox-short.txt",'r')

index = 0
for line in file:
    if "From " in line: #se analizan las lineas que comienzan com 'From'
        for world in line.split():
            index += 1
            if index == 2:
                print(world) #se imprime el correo de quien lo mando
        index = 0