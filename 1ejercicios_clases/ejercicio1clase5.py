subjects = ['math', 'fis', 'quim', 'his']
scores = []
for index in subjects:
    scores.append(input("ingrese la nota de la materia:  " + index))

for i in range(len(subjects)):
    print("En " + subjects[i] + "has obtenido " + scores[i])