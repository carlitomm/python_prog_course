numlist = list()

while True:
    inp = input('ingrese um valor')
    if inp == 'fin': break
    numlist.append(float(inp))

prom = sum(numlist)/len(numlist)
print(prom)