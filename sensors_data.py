import random
import time
import json

def generate_air_quality_data():
    sensor_id = random.randint(1, 5)  
    return {
        "sensor_id": sensor_id,
        "pm2_5": round(random.uniform(0, 100), 2),
        "pm10": round(random.uniform(0, 150), 2),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

def generate_temperature_data():
    sensor_id = random.randint(1, 5)
    return {
        "sensor_id": sensor_id,
        "value": round(random.uniform(-10, 40), 2),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

def generate_humidity_data():
    sensor_id = random.randint(1, 5)
    return {
        "sensor_id": sensor_id,
        "value": round(random.uniform(0, 100), 2),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

