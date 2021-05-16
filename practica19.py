file = open('romeo.txt', "r")
text = file.read()

dic = dict()
word_list = text.split()
for i in range(len(word_list)):
    if word_list[i] not in dic.keys():
        new_word = word_list[i] 
        dic[new_word] = 1
        for j in range(i+1, len(word_list)):
            if word_list[j] == new_word:
                dic[new_word] += 1
print(dic)

# {'and': 3, 'envious': 1, 'already': 1, 'fair': 1,
# 'is': 3, 'through': 1, 'pale': 1, 'yonder': 1,
# 'what': 1, 'sun': 2, 'Who': 1, 'But': 1, 'moon': 1,
# 'window': 1, 'sick': 1, 'east': 1, 'breaks': 1,
# 'grief': 1, 'with': 1, 'light': 1, 'It': 1, 'Arise': 1,
# 'kill': 1, 'the': 3, 'soft': 1, 'Juliet': 1}

# https://alumnosuacj-my.sharepoint.com/:v:/g/personal/al206563_alumnos_uacj_mx/EclWXMaF_WNJsJKwJeydXNgBayqLeIH4i_jl6MxeQsKfSA