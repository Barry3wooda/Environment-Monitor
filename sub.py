import paho.mqtt.client as mqtt
from pymongo import MongoClient
import mysql.connector
from neo4j import GraphDatabase
import json

# Database connections
mongo_conn = MongoClient("mongodb://localhost:27017/")
print("Connected to MongoDB")

mysql_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="sensors")
print("Connected to MySQL")

neo4j_conn = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "12345678"))
print("Connected to Neo4j")



broker = 'localhost'
port = 1883


# MQTT topic
TOPIC_AIR_QUALITY = 'sensors/air_quality'
TOPIC_TEMP = 'sensors/temp'
TOPIC_HUMIDITY = 'sensors/humidity'

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        client.subscribe([(TOPIC_AIR_QUALITY, 0), (TOPIC_TEMP, 0), (TOPIC_HUMIDITY, 0)])
    else:
        print("Connection failed")

# function to insert temp data into MySQL
cursor = mysql_conn.cursor() 
def mysql_temp_insert(cursor, data):
    try:
        # create table if not exists
        cursor.execute("CREATE TABLE IF NOT EXISTS temperature (id INT AUTO_INCREMENT PRIMARY KEY, sensor_id INT, value FLOAT, timestamp VARCHAR(50))")
        # insert data
        cursor.execute("INSERT INTO temperature (sensor_id, value, timestamp) VALUES (%s, %s, %s)",
                       (data["sensor_id"], data["value"], data["timestamp"]))
        mysql_conn.commit()
    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")

# function to insert humidity data into Neo4j
neo4j_session = neo4j_conn.session()


def neo4j_insert_humidity(data):
    try:
        neo4j_session.run("MERGE (s:Sensor {sensor_id: $sensor_id}) "
                          "MERGE (h:Humidity {value: $value, timestamp: $timestamp}) "
                          "MERGE (s)-[:MEASURED]->(h)",
                          sensor_id=data["sensor_id"], value=data["value"], timestamp=data["timestamp"])
    except Exception as e:
        print(f"Neo4j Error: {e}")

# function to insert all the data into MongoDB
def mongo_insert(collection, data):
    try:
        mongo_conn['sensors'][collection].insert_one(data)
    except Exception as e:
        print(f"MongoDB Error: {e}")

# function to handle incoming messages
def on_message(client, userdata, msg):
    print(f"{msg.topic} -> {msg.payload.decode()}")
    try:
        data = json.loads(msg.payload)
        if msg.topic == TOPIC_AIR_QUALITY:
            mongo_insert("air_quality", data)
        elif msg.topic == TOPIC_TEMP:
            mysql_temp_insert(cursor, data)
            mongo_insert("temp", data)
        elif msg.topic == TOPIC_HUMIDITY:
            neo4j_insert_humidity(data)
            mongo_insert("humidity", data)
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
    except Exception as e:
        print(f"Error processing message: {e}")

# MQTT client
client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message


client.connect(broker, port, 60) # 60 seconds keepalive
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Subscriber stopped")
    client.disconnect()
    cursor.close()
    mysql_conn.close()
    neo4j_session.close()
    mongo_conn.close()

