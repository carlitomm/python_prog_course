
import sqlite3
import serial

conn = sqlite3.connect('practica27.sqlite')
cur = conn.cursor()

serialPort = '/dev/ttyUSB0'
baudRate = 9600

try:
    serialConnection = serial.Serial(serialPort, baudRate)
except Exception as e:
    print("error con el puerto serie")
    print(e)

def getSerialData (serialConnection):
    try:
        values = serialConnection.readline().split()
        return float(values[0]) ,float(values[1])
    except:
        value = -1


class magnet_sensor_model():
    def __init__(self, pp, np):
        self.positive_pole = pp
        self.negative_pole = np
    
    def save(self):
        cur.execute('INSERT INTO magnetic_field(positive_pole, negative_pole) VALUES(?,?)', (
            self.positive_pole, 
            self.negative_pole)
        )
        conn.commit()
    
    @staticmethod
    def fetchAll():
        cur.execute('SELECT id, positive_pole, negative_pole FROM magnetic_field')
        for fila in cur:
            print(fila)

    @staticmethod
    def deleteById(Id):
        try:
            cur.execute('DELETE FROM magnetic_field WHERE id=?', (Id, ))
            conn.commit()
            return True
        except:
             return False  
    

class magnet_controller():
    
    @staticmethod
    def add_meassurement():
        serialConnection.write(str.encode('l'))  
        positive_pole, negative_pole = getSerialData(serialConnection)
        mg = magnet_sensor_model(positive_pole, negative_pole)
        mg.save()
        return positive_pole, negative_pole 
    @staticmethod
    
    def delete_meassurement(id):
        return magnet_sensor_model.deleteById(id)

    def getAll_meassuremetns():
        magnet_sensor_model.fetchAll()

if __name__ == '__main__': 
    while True:
        try:
            cmd = input("presione \n s para guardar los datos \n d para borrar un dato \n f para mostrar los datos por pantalla \n x para salir")
            if cmd is 's':
                positive_pole, negative_pole = magnet_controller.add_meassurement()
                print("los valores a guardar son " + str(positive_pole) +" y "+ str(negative_pole))
                print("-----------------------------------------------------------------")
            elif cmd is 'f':
                print("los datos de la base de datos son")
                magnet_controller.getAll_meassuremetns()
                print("-----------------------------------------------------------------")
            elif cmd is 'd':
                Id = int(input("ingrese ID de la medición a borrar"))
                if (magnet_controller.delete_meassurement(Id)):
                    print("borrado correctamente")
                else:
                    print("Al parecer ocurrio un problema")
            else:
                break
        except Exception as e:
            print(e)
            serialConnection.close
            break
# https://alumnosuacj-my.sharepoint.com/:v:/g/personal/al206563_alumnos_uacj_mx/EZFT684Vp1JHs0ERVw2vBu8BnXmsksYpRi_P_c1vh-XzBw