n = int (input("introduzca el numero"))
fname = 'tabla' + str(n) + '.txt'
file = open(fname,'w')
for i in range(1,11):
    file.write(str(n)+ '*' + str(i) + ' = ' + str(n*i) + '\n' )
file.close()