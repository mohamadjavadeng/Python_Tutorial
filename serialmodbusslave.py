import serial
import time

receiver = serial.Serial(     
     port='COM8',        
     baudrate = 9600,
     parity=serial.PARITY_EVEN,
     stopbits=serial.STOPBITS_ONE,
     bytesize=serial.SEVENBITS,
     timeout=1
     
     )

while 1:
      x = receiver.readline()
      print(x)
      time.sleep(3)