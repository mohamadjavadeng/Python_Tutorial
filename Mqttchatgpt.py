import paho.mqtt.client as mqtt
import time
import json

# # Ubidots MQTT credentials
# BROKER_ENDPOINT = "industrial.api.ubidots.com"
# TLS_PORT = 1883  # Secure port
# UBIDOTS_USERNAME = "BBUS-qgOqmuIQlf3tDj0yZgotfyXjVdJWNn"
# UBIDOTS_PASSWORD = ""
# # CLIENT_ID = "your-client-id"
# TOPIC = "/v1.6/devices/{device_label}/{variable_label}/lv"
# QOS = 1

# # Define the callback functions for MQTT events
# def on_connect(client, userdata, flags, rc):
#     print("Connected with result code " + str(rc))

# def on_publish(client, userdata, mid):
#     print("Message published with mid: " + str(mid))

# def on_subscribe(client, userdata, mid, granted_qos):
#     print("Subscribed to topic with mid " + str(mid))

# def on_message(client, userdata, message):
#     print("Received message '" + str(message.payload) + "' on topic '" + message.topic + "'")


# # Create an MQTT client instance
# client = mqtt.Client()
# client.username_pw_set(UBIDOTS_USERNAME, password=UBIDOTS_PASSWORD)

# # Assign callback functions
# client.on_connect = on_connect
# client.on_publish = on_publish
# client.on_subscribe = on_subscribe
# client.on_message = on_message

# client.connect(BROKER_ENDPOINT, TLS_PORT, 60)

# client.subscribe(TOPIC.format(device_label="pythonmqtt", variable_label="temp"), QOS)


# # Loop to maintain the connection
# client.loop_start()
# # Publish a message to a variable
# for i in range(1,2):
#     variable_value = i * 10
#     # message = {"temp": variable_value}
#     message = json.dumps({"temp": variable_value})
#     client.publish(TOPIC.format(device_label="pythonmqtt", variable_label="temp"), payload=json.dumps(message), qos=QOS)

#     # Wait for a few seconds before unsubscribing and disconnecting
#     time.sleep(1)
# time.sleep(5)
# # Unsubscribe from the variable
# print(client.is_connected())
# client.unsubscribe(TOPIC.format(device_label="pythonmqtt", variable_label="temp"))

# # Stop the MQTT client loop
# client.loop_stop()
# # Disconnect from the broker
# client.disconnect()


# Ubidots constants
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

# Connect to the Ubidots broker
client.connect(BROKER, PORT, 60)

# Start the client loop
client.loop_start()

# Prepare the payload
payload = json.dumps({VARIABLE_LABEL: 12})  # Replace with your data

# Publish the data to the topic
client.publish(TOPIC, payload)

# Stop the client loop
client.loop_stop()

# Disconnect the client
client.disconnect()

# client = mqtt.Client()
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
    print("Message received")