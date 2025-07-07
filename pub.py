import paho.mqtt.client as mqtt
import time
import random
import json
from sensors_data import generate_air_quality_data, generate_temperature_data, generate_humidity_data

#broker configuration

broker_address = "localhost" 
port = 1883

TOPIC_AIR_QUALITY = 'sensors/air_quality'
TOPIC_TEMP = 'sensors/temp'
TOPIC_HUMIDITY = 'sensors/humidity'
cid = f"python-publisher"


def on_connect(client, userdata, flags, rc):
    if rc == 0:  #return code 
        print("Connected to MQTT Broker!")
    else:
        print(f"Failed to connect, return code {rc}\n")

client = mqtt.Client(client_id=cid) 
client.on_connect = on_connect



client.connect(broker_address, port)
client.loop_start() # Start a non-blocking thread loop for network traffic




msg_count = 0
while True:
    time.sleep(1)

    # Generate and send air quality data
    air_quality_msg = json.dumps(generate_air_quality_data())
    result = client.publish(TOPIC_AIR_QUALITY, air_quality_msg, qos=1) #quality of service (At least once delivery)
    if result[0] == 0:
        print(f"Sent {TOPIC_AIR_QUALITY}: `{air_quality_msg}`")
    else:
        print(f"Failed to send message to topic {TOPIC_AIR_QUALITY}")

    # Generate and send temperature data
    temp_msg = json.dumps(generate_temperature_data())
    result = client.publish(TOPIC_TEMP, temp_msg, qos=1) 
    if result[0] == 0:
        print(f"Sent {TOPIC_TEMP}: `{temp_msg}`")
    else:
        print(f"Failed to send message to topic {TOPIC_TEMP}")

    # Generate and send humidity data
    humidity_msg = json.dumps(generate_humidity_data())
    result = client.publish(TOPIC_HUMIDITY, humidity_msg, qos=1)
    if result[0] == 0:
        print(f"Sent {TOPIC_HUMIDITY}: `{humidity_msg}`")
    else:
        print(f"Failed to send message to topic {TOPIC_HUMIDITY}")

    msg_count += 1
    if msg_count > 10:
        break

client.loop_stop()
client.disconnect()
print("Publisher disconnected.")