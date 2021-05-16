# with open('mbox-short.txt', 'r') as file:
#     lines = file.readlines()
#     for linea in lines:
#         # if linea.startswith("From"):
#         #     linea = linea.rstrip()
#         #     print(linea)
#         # if '@uct.ac.za' in linea:
#         #     linea = linea.rstrip()
#         #     print(linea)
#         if linea.find('@uct.ac.za') != -1:
#             linea = linea.rstrip()
#             print(linea)
#     file.close()

file2 = open('file.txt','w')
file2.write("priemera linea \n")
file2.write("segunda linea \n")

# file = open("mbox-short.txt",'r')

# for line in file:
#     print(line)

# file.close()
# # content = file.read()
# # print(content)