import serial
import minimalmodbus
from time import sleep
import requests as re

def write_data(M0, M1, D0, Y0, Y1):
    return re.get(f"https://script.google.com/macros/s/AKfycbzAoIICl2e86ovNTc6KfEihjEA0kEy0Sq5j4zvOaole0zXipHe_Oz-nu9ql_RDXuqXW/exec?sts=write&M0={M0}&M1={M1}&D0={D0}&Y0={Y0}&Y1={Y1}")

def read_data():
    rd =re.get(f"https://script.google.com/macros/s/AKfycbzAoIICl2e86ovNTc6KfEihjEA0kEy0Sq5j4zvOaole0zXipHe_Oz-nu9ql_RDXuqXW/exec?sts=read")
    if rd.text == ',,,,':
        re.get(f"https://script.google.com/macros/s/AKfycbzAoIICl2e86ovNTc6KfEihjEA0kEy0Sq5j4zvOaole0zXipHe_Oz-nu9ql_RDXuqXW/exec?sts=write&M0=0&M1=0&D0=0&Y0=0&Y1=0")
        return [0,0,0,0,0]
    rd = list(rd.text.split(','))
    for i in range(0, len(rd)):
        rd[i] = int(rd[i])
    return rd


client1 = minimalmodbus.Instrument('COM23', 1, debug=False)  # port name, slave address (in decimal)
client1.serial.baudrate = 9600  # baudrate
client1.serial.bytesize = 7
client1.serial.parity   = serial.PARITY_EVEN
client1.serial.stopbits = 1
client1.serial.timeout  = 0.1      # seconds
client1.address         = 1        # this is the slave address number
client1.mode = minimalmodbus.MODE_ASCII # rtu or ascii mode
client1.clear_buffers_before_each_transaction = True


while True:
    RD = read_data()
    # M0_data = client1.read_bit(2048, functioncode=1)
    try:
        M0_data = client1.read_bit(2048, functioncode=1)
    except minimalmodbus.InvalidResponseError as e:
        print(f"Invalid response received: {e}")
        print(f"Raw response: {e.response}")
    M1_data = client1.read_bit(2049, functioncode=1)
    D0_data = client1.read_register(4096, 1, 3)
    Y0_data = client1.read_bit(1280, functioncode=1)
    Y1_data = client1.read_bit(1281, functioncode=1)
    print([M0_data, M1_data, D0_data, Y0_data, Y1_data])
    print('-'*20)
    print(RD)
    if [M0_data, M1_data, D0_data, Y0_data, Y1_data] == RD:
        print("nothing changed")
    else:
        print("else now")
        client1.write_bit(2048, RD[0], functioncode=5)
        client1.write_bit(2049, RD[1], functioncode=5)
        client1.write_register(4096, RD[2], 1, functioncode=16)
        client1.write_bit(1280, RD[3], functioncode=5)
        client1.write_bit(1281, RD[4], functioncode=5)
        write_data(RD[0], RD[1], RD[2], RD[3], RD[4])
    
    sleep(7)
