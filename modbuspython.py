import serial
import minimalmodbus
from time import sleep

client1 = minimalmodbus.Instrument('COM4', 1, debug=False)  # port name, slave address (in decimal)
client1.serial.baudrate = 9600  # baudrate
client1.serial.bytesize = 8
client1.serial.parity   = serial.PARITY_NONE
client1.serial.stopbits = 1
client1.serial.timeout  = 0.2      # seconds
client1.address         = 1        # this is the slave address number
client1.mode = minimalmodbus.MODE_RTU # rtu or ascii mode
client1.clear_buffers_before_each_transaction = True

sleep(2)
print("program started")

coil_value = client1.read_bit(1, functioncode=1)

# Print the value
print(f"Value of coil 0: {coil_value}")
client1.write_bit(1, not coil_value, functioncode=5)

input_stats  = client1.read_register(0, 1, 3) # read single register 2bytes (16bit)
print("input stats: {0:016b}".format(input_stats))
output_stats  = client1.read_register(1, 1, 3) # read single register 2bytes (16bit)
print("output stats: {0:016b}".format(output_stats))
output_stats  = client1.read_register(2, 1, 3) # read single register 2bytes (16bit)
print("output stats: {0:016b}".format(output_stats))


client1.close_port_after_each_call = True