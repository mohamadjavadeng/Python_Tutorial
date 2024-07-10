import serial
import minimalmodbus
from time import sleep
import paho.mqtt.client as mqtt
import time
import json

client1 = minimalmodbus.Instrument('COM13', 1, debug=False)  # port name, slave address (in decimal)
client1.serial.baudrate = 9600  # baudrate
client1.serial.bytesize = 8
client1.serial.parity   = serial.PARITY_NONE
client1.serial.stopbits = 1
client1.serial.timeout  = 0.2      # seconds
client1.address         = 1        # this is the slave address number
client1.mode = minimalmodbus.MODE_RTU # rtu or ascii mode
client1.clear_buffers_before_each_transaction = True
#######################################################
UBIDOTS_TOKEN = "BBUS-Wq9Agm0jLaHdEr3U1n5VLT7jgqA1nk"
DEVICE_LABEL = "pymqtt"
VARIABLE_LABEL = "temp"
BROKER = "industrial.api.ubidots.com"
PORT = 1883
TOPIC = f"/v1.6/devices/{DEVICE_LABEL}"
# Callback functions
def on_connect1(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    if rc == 0:
        print("Connection successful")
    else:
        print("Connection failed")

def on_connect2(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    if rc == 0:
        print("Connection successful")
        client.subscribe(TOPIC)
    else:
        print("Connection failed")

def on_publish(client, userdata, mid):
    print("Data published with message id: ", mid)


def on_message(client, userdata, msg):
    global res
    global val
    print(f"Message received on topic {msg.topic}")
    payload = json.loads(msg.payload.decode('utf-8'))
    print(f"Payload: {payload}")
    res = 1
    val = payload

# Create an MQTT client instance
client = mqtt.Client()

# Assign callback functions
client.on_connect = on_connect1
client.on_publish = on_publish


# Set the username and password (token)
client.username_pw_set(UBIDOTS_TOKEN, password="")
#######################################################
print("program started")
coil_value = client1.read_bit(1282, functioncode=1)
# Print the value
print(f"Value of coil 0: {coil_value}")
client1.write_bit(1282, not coil_value, functioncode=5)
input_stats  = client1.read_register(4096, 1, 3) # read single register 2bytes (16bit)
print(f"input stats: {input_stats}")
#########################################################
# Connect to the Ubidots broker
client.connect(BROKER, PORT, 60)

# Start the client loop
client.loop_start()

# Prepare the payload
payload = json.dumps({VARIABLE_LABEL: input_stats})  # Replace with your data

# Publish the data to the topic
client.publish(TOPIC, payload)

# Stop the client loop
client.loop_stop()

# Disconnect the client
client.disconnect()
#########################################################
output_stats  = client1.read_register(4097, 1, 3) # read single register 2bytes (16bit)
print("output stats: {}".format(output_stats))
output_stats  = client1.read_register(4098, 1, 3) # read single register 2bytes (16bit)
print("output stats: {}".format(output_stats))
client1.write_register(4098, 500) # write single register
#########################################################
VARIABLE_LABEL = "y0"
TOPIC = f"/v1.6/devices/{DEVICE_LABEL}/{VARIABLE_LABEL}/lv"
client.on_connect = on_connect2
client.on_message = on_message
# client.username_pw_set(UBIDOTS_TOKEN, password="")
received_message = None
client.connect(BROKER, PORT, 60)
client.loop_start()
j = 0
res = 0

while j < 10 and res == 0:
    time.sleep(1)
    print(j)
    j = j + 1

client.loop_stop()

if res == 0:
    print("No message received within the timeout period")
else:
    client1.write_bit(1280, int(val))
#########################################################

client1.close_port_after_each_call = True