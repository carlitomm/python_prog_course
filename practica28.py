import pyaudio
import struct
import math
import serial
import time

serialPort = '/dev/ttyUSB0'
baudRate = 9600

try:
    serialConnection = serial.Serial(serialPort, baudRate)
except Exception as e:
    print("error con el puerto serie")
    print(e)

class TapTester(object):
    def __init__(self):
        self.INITIAL_TAP_THRESHOLD = 0.010
        self.FORMAT = pyaudio.paInt16 
        
        self.CHANNELS = 2
        self.RATE = 44100  
        
        INPUT_BLOCK_TIME = 0.05
        self.INPUT_FRAMES_PER_BLOCK = int(self.RATE*INPUT_BLOCK_TIME)
        self.OVERSENSITIVE = 15.0/INPUT_BLOCK_TIME                    
        self.UNDERSENSITIVE = 120.0/INPUT_BLOCK_TIME 
        self.MAX_TAP_BLOCKS = 0.15/INPUT_BLOCK_TIME
        self.pa = pyaudio.PyAudio()
        self.stream = self.open_mic_stream()
        self.tap_threshold = self.INITIAL_TAP_THRESHOLD
        self.noisycount = self.MAX_TAP_BLOCKS+1 
        self.quietcount = 0 
        self.errorcount = 0

        self.counter = 0

    def stop(self):
        self.stream.close()
    
    def get_rms(self, block):

        SHORT_NORMALIZE = (1.0/32768.0)
        count = len(block)/2
        format = "%dh"%(count)
        shorts = struct.unpack( format, block )

        sum_squares = 0.0
        for sample in shorts:
            n = sample * SHORT_NORMALIZE
            sum_squares += n*n

        return math.sqrt( sum_squares / count )

    def find_input_device(self):
        device_index = None            
        for i in range( self.pa.get_device_count() ):     
            devinfo = self.pa.get_device_info_by_index(i)   
            print( "Device %d: %s"%(i,devinfo["name"]) )

            for keyword in ["mic","input"]:
                if keyword in devinfo["name"].lower():
                    print( "Found an input: device %d - %s"%(i,devinfo["name"]) )
                    device_index = i
                    return device_index

        if device_index == None:
            print( "No preferred input found; using default input device." )

        return device_index

    def open_mic_stream( self ):
        device_index = self.find_input_device()

        stream = self.pa.open(   format = self.FORMAT,
                                 channels = self.CHANNELS,
                                 rate = self.RATE,
                                 input = True,
                                 input_device_index = device_index,
                                 frames_per_buffer = self.INPUT_FRAMES_PER_BLOCK)

        return stream

    def tapDetected(self):
        self.counter += 1
        serialConnection.write('l')
        print( str(self.counter) + "Tap!")

    def listen(self):
        try:
            block = self.stream.read(self.INPUT_FRAMES_PER_BLOCK)
        except IOError as e:
            # dammit. 
            self.errorcount += 1
            print( "(%d) Error recording: %s"%(self.errorcount,e) )
            self.noisycount = 1
            return

        amplitude = self.get_rms( block )
        if amplitude > self.tap_threshold:
            # noisy block
            self.quietcount = 0
            self.noisycount += 1
            if self.noisycount > self.OVERSENSITIVE:
                # turn down the sensitivity
                self.tap_threshold *= 1.1
        else:            
            # quiet block.

            if 1 <= self.noisycount <= self.MAX_TAP_BLOCKS:
                self.tapDetected()
            self.noisycount = 0
            self.quietcount += 1
            if self.quietcount > self.UNDERSENSITIVE:
                # turn up the sensitivity
                self.tap_threshold *= 0.9

if __name__ == "__main__":
    tt = TapTester()

    serialConnection.write('l')

    while(True):
        tt.listen()

# https://alumnosuacj-my.sharepoint.com/:v:/g/personal/al206563_alumnos_uacj_mx/EdUqTG5-HRVBvdqOIF5hBM0BVdAnAr9xTpIdCzcxdS8ljg