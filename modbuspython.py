import serial
import minimalmodbus
from time import sleep

client1 = minimalmodbus.Instrument('COM23', 1, debug=False)  # port name, slave address (in decimal)
client1.serial.baudrate = 9600  # baudrate
client1.serial.bytesize = 7
client1.serial.parity   = serial.PARITY_EVEN
client1.serial.stopbits = 1
client1.serial.timeout  = 0.1      # seconds
client1.address         = 1        # this is the slave address number
client1.mode = minimalmodbus.MODE_ASCII # rtu or ascii mode
client1.clear_buffers_before_each_transaction = True

input_stats  = client1.read_register(4101, 1, 3) # read single register 2bytes (16bit)
print("input stats: {0:016b}".format(input_stats))
output_stats  = client1.read_register(4096, 1, 3) # read single register 2bytes (16bit)
print("output stats: {0:016b}".format(output_stats))
output_stats  = client1.read_register(4096, 1, 3) # read single register 2bytes (16bit)
print("output stats: {0:016b}".format(output_stats))
coil_value = client1.read_bit(1280, functioncode=1)

# Print the value
print(f"Value of coil 0: {coil_value}")
client1.write_bit(1280, not coil_value, functioncode=5)

client1.close_port_after_each_call = True