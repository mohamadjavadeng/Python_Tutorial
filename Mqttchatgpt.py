import paho.mqtt.client as mqtt
import time
import json

# Ubidots MQTT credentials
BROKER_ENDPOINT = "industrial.api.ubidots.com"
TLS_PORT = 1883  # Secure port
UBIDOTS_USERNAME = "BBUS-qgOqmuIQlf3tDj0yZgotfyXjVdJWNn"
UBIDOTS_PASSWORD = ""
# CLIENT_ID = "your-client-id"
TOPIC = "/v1.6/devices/{device_label}/{variable_label}/lv"
QOS = 1

# Define the callback functions for MQTT events
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def on_publish(client, userdata, mid):
    print("Message published with mid: " + str(mid))

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed to topic with mid " + str(mid))

def on_message(client, userdata, message):
    print("Received message '" + str(message.payload) + "' on topic '" + message.topic + "'")


# Create an MQTT client instance
client = mqtt.Client()
client.username_pw_set(UBIDOTS_USERNAME, password=UBIDOTS_PASSWORD)

# Assign callback functions
client.on_connect = on_connect
client.on_publish = on_publish
client.on_subscribe = on_subscribe
client.on_message = on_message

client.connect(BROKER_ENDPOINT, TLS_PORT, 60)

client.subscribe(TOPIC.format(device_label="pythonmqtt", variable_label="temp"), QOS)


# Loop to maintain the connection
client.loop_start()
# Publish a message to a variable
for i in range(1,80):
    variable_value = 42
    message = {"temp": variable_value}
    client.publish(TOPIC.format(device_label="pythonmqtt", variable_label="temp"), payload=json.dumps(message), qos=QOS)

    # Wait for a few seconds before unsubscribing and disconnecting
    time.sleep(1)
time.sleep(5)
# Unsubscribe from the variable
client.unsubscribe(TOPIC.format(device_label="pythonmqtt", variable_label="temp"))

# Disconnect from the broker
client.disconnect()

# Stop the MQTT client loop
client.loop_stop()

