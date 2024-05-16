import paho.mqtt.client as mqttClient
import time
import json
import ssl

# Get the default system TLS certificate store path


connected = False  # Stores the connection status
BROKER_ENDPOINT = "industrial.api.ubidots.com"
TLS_PORT = 8883  # Secure port
MQTT_USERNAME = "BBUS-qgOqmuIQlf3tDj0yZgotfyXjVdJWNn"  # Put here your Ubidots TOKEN
MQTT_PASSWORD = ""  # Leave this in blank
TOPIC = "/v1.6/devices/"
DEVICE_LABEL = "pythonmqtt"
TLS_CERT_PATH = "C:/Users/Mohamad/AppData/Local/Programs/Python/Python311/Lib/site-packages/certifi/cacert.pem" # Put here the path of your TLS cert


def on_connect(client, userdata, flags, rc):
    global connected  # Use global variable
    if rc == 0:

        print("[INFO] Connected to broker")
        connected = True  # Signal connection
    else:
        print("[INFO] Error, connection failed")

def on_publish(client, userdata, result):
    print("Published!")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


def connect(mqtt_client, mqtt_username, mqtt_password, broker_endpoint, port):
    global connected

    if not connected:
        mqtt_client.username_pw_set(mqtt_username, password=mqtt_password)
        mqtt_client.on_connect = on_connect
        mqtt_client.on_publish = on_publish
        mqtt_client.on_message = on_message
        mqtt_client.tls_set(ca_certs=TLS_CERT_PATH, certfile=None,
                            keyfile=None, cert_reqs=ssl.CERT_REQUIRED,
                            tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
        mqtt_client.tls_insecure_set(False)
        mqtt_client.connect(broker_endpoint, port=port)
        mqtt_client.loop_start()

        attempts = 0

        while not connected and attempts < 5:  # Wait for connection
            print(connected)
            print("Attempting to connect...")
            time.sleep(1)
            attempts += 1

    if not connected:
        print("[ERROR] Could not connect to broker")
        return False

    return True
def publish(mqtt_client, topic, payload):

    try:
        mqtt_client.publish(topic, payload)

    except Exception as e:
        print("[ERROR] Could not publish data, error: {}".format(e))

def subscribe(mqtt_client, topic, variable):
    topic = "{}/{}".format(topic, variable)
    try:
        mqtt_client.subscribe(topic)
    except Exception as e:
        print("[ERROR] Could not subscribe data, error: {}".format(e))



def main(mqtt_client):
    for i in range(1,50):
        variable = "varistor"
        payload = json.dumps({"temp": i})
        topic = "{}{}".format(TOPIC, DEVICE_LABEL)

    

        if not connect(mqtt_client, MQTT_USERNAME,
                    MQTT_PASSWORD, BROKER_ENDPOINT, TLS_PORT):
            return False

        publish(mqtt_client, topic, payload)
        subscribe(mqtt_client, topic, variable)
        time.sleep(1)

    return True

if __name__ == '__main__':
    mqtt_client = mqttClient.Client()
    while True:
        main(mqtt_client)
        time.sleep(10)