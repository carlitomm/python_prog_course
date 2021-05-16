dic = {}
words = input("ingrese la lista de palabras en formato y la tradusccio deparadas por coma")

for i in words.split(','):
    key, value = i.split(':')
    dic[key] = value

phrase = input('ingrese la frase en español')
for i in phrase.split():
    if i in dic:
        print(dic[i], end=' ')