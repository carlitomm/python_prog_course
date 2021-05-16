import tkinter as tk
from tkinter import ttk
import serial, time
import threading

arduino = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)
time.sleep(2)

class PasosFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.L1 = tk.Label(self)
        self.L1["Text"] = ('Numeros de Pasos')
        self.L1.pack()

        self.EntPas = ttk.Entry(self)
        self.EntPas.pack(pady = 10, side = 'top')

        self.gAd = ttk.Button(self, text = "Paso adelante", command = self.pasoAd)
        self.gAd.pack(pady = 10, ipadx = 8, ipady = 8, side='right')

        self.gAt = ttk.Button(self, text = "Paso atras", command = self.pasoAt)
        self.gAt.pack(pady = 10, ipadx = 8, ipady = 8, side='left')
    
    def pasoAd(self):
        self.numPasos = int(self.EntPas.get())
        for i in range (0, self.numPasos):
            arduino.write(b'1')
            print(i)
            time.sleep(0.1)
    
    def pasoAt(self):
        self.numPasos = int(self.EntPas.get())
        for i in range (0, self.numPasos):
            arduino.write(b'2')
            print(i)
            time.sleep(0.1)

class ContinuoFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title = tk.Label(self)
        self.title["Text"] = ('Giro automático')
        self.title.pack()

        self.bAd = ttk.Button(self, text = "adelante", command = self.autoAd)
        self.bAd.pack(pady = 10, ipadx = 8, ipady = 8, side='right')

        self.bAt = ttk.Button(self, text = "atras", command = self.autoAt)
        self.bAt.pack(pady = 10, ipadx = 8, ipady = 8, side='left')

        self.bstop = ttk.Button(self, text = "stop", command = self.stop)
        self.bstop.pack(pady = 10, ipadx = 8, ipady = 8, side='center')
    
    def continuo_ad(self):
        def iniciar():
            while(switch_ad == True):
                arduino.write(b'1')
                time.sleep(0.1)
        
        thread1 = threading.Thread(target=iniciar)
        thread1.start()
    
    def autoAd(self):
        global switch_ad
        switch_ad = True
        self.continuo_ad()
    
    def continuo_at(self):
        def inicio():
            while(switch_ad == True):
                arduino.write(b'2')
                time.sleep(0.1)
        
        thread2 = threading.Thread(target=inicio)
        thread2.start()

    def autoAt(self):
        global switch_at
        switch_at = True
        self.continuo_at()
    
    def stop(self):
        switch_ad = False
        switch_at = False


class ManualFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title = tk.Label(self)
        self.title["Text"] = ('control manual')
        self.title.pack()

        self.bAd = ttk.Button(self, text = "adelante", command = self.autoAd)
        self.bAd.pack(pady = 10, ipadx = 8, ipady = 8, side='right')

        self.bAt = ttk.Button(self, text = "atras", command = self.autoAt)
        self.bAt.pack(pady = 10, ipadx = 8, ipady = 8, side='left')

    def autoAd(self):
        arduino.write(b'1')
    
    def autoAt(self):
        arduino.write(b'2')

class Interface(ttk.Frame):

    def __init__(self, principal):
        super().__init__(principal)

        principal.title('Control steper')
        
        self.notebook = ttk.Notebook(self, width = 350, height=200)

        self.paso_frame = PasosFrame(self.notebook)
        self.notebook.add(self.paso_frame, text='ventana 1')

        self.auto_frame = ContinuoFrame(self.notebook)
        self.notebook.add(self.auto_frame, text='ventana 2')

        self.manual_frame = ManualFrame(self.notebook)
        self.notebook.add(self.manual_frame, text='ventana 3')

        self.notebook.pack(padx=10, pady=10)

principal = tk.Tk
# principal.geometry('400x300')
# principal.resizable(width=False, height=False)

app = Interface(principal)
app.mainloop()