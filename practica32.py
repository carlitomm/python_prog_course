import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'tesseract'

adresses = ['matriculas/1.jpg',
                'matriculas/2.jpg',
                'matriculas/3.jpg',
                'matriculas/4.jpg',
                'matriculas/5.jpg',
                'matriculas/6.jpg',
                'matriculas/7.jpg'
            ]

paises = ['cuba', 'Colombia', 'Mexico', 'USA']

estados_mexico = ['aguascalientes', 'baja california','baja california sur',
            'campeche','coahuila de zaragoza','colima','chiapas','chihuahua',
            'distrito federal','durango','guanajuato','guerrero',
            'hidalgo',
            'jalisco',
            'michoacan de ocampo',
            'morelos',
            'nayarit',
            'nuevo Leon',
            'oaxaca',
            'puebla',
            'queretaro',
            'quintana roo',
            'san luis potosi',
            'sinaloa',
            'sonora',
            'tabasco',
            'tamaulipas',
            'tlaxcala',
            'veracruz de ignacio de la llave',
            'yucatan',
            'zacatecas']

class chapa:
    def __init__(self, pais, estado, matricula):
        self.pais = pais
        self.estado = estado
        self.matricula = matricula
    
    def print_chapa(self):
        print('El pais de la matricula es: '+ self.pais + ' del estado: '+ self.estado)
        print('matricula ' + self.matricula)

chapas = []
no_identificadas = []
identified = False


for i in range( len(adresses) ):
    
    image = cv2.imread(adresses[i])
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    
    text = pytesseract.image_to_string(gray)

    identified= False
    text = text.split()

    if len(text) == 0:
        text = pytesseract.image_to_string(image)
        text = text.split()
    
    symbol = True
    counter = len(text)+1
    while (symbol is True and counter >0):
        counter-=1
        for j in range(counter):
            if text[j] == '&' or text[j] == '<' or text[j] =='<_<' or text[j] =='=' or text[j] =='-' or text[j] =='{' or text[j] == '——':
                text.pop(j)
                break
            elif j >= counter :
                symbol = False  


    print('Texto: ', text)
    for j in range(len(text)):
        if text[j].lower() in estados_mexico:
            if text[j].lower() == 'queretaro':
                chap = chapa('Mexico',text[j],text[9])
            else:
                chap = chapa('Mexico',text[j],'not identificada matricula')
            chapas.append(chap)
            identified = True
            break
        elif text[j].lower() == 'columbia':
            chap = chapa('Canada','British Columbia',text[3])
            chapas.append(chap)
            identified = True
            break
    if not identified:
        no_identificadas.append(i)



for i in no_identificadas:
    
    image = cv2.imread(adresses[i])
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    dilate = cv2.dilate(gray, None, iterations=1)

    text = pytesseract.image_to_string(dilate)
    text = text.split()
    print(text)

    for j in range(len(text)):
        if text[j].lower() in estados_mexico:
            chap = chapa('Mexico',text[j],'not identificada matricula')
            chapas.append(chap)
            no_identificadas.remove(i)
        elif text[j].lower() in paises:  
            chap = chapa(text[j],'no estado', text[2] + text[3])
            chapas.append(chap)
            no_identificadas.remove(i)


file = open("matriculas.txt", "w")
print ("==============las matriculas identificadas son===============")
for i in range(len(chapas)):
    print(chapas[i].print_chapa())
    file.write(str(i) +' Pais: ' + chapas[i].pais + ' estado: '+ chapas[i].estado + ' matricula: '+ chapas[i].matricula +'\n')
    print('-------------------------------------')

print ("las matriculas NO identificadas son")
for i in range(len(no_identificadas)):
    i= no_identificadas[i]
    image = cv2.imread(adresses[i])
    text = pytesseract.image_to_string(image)
    text = text.split()
    strf=''
    for j in range(len (text)):
        strf+=text[j]+','
    file.write('no identificada '+ strf)
    print(text)