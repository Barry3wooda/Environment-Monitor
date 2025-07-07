# Environment Monitor

## System Architecture

The Environment Monitor system is designed to simulate and monitor environmental data using sensors. It consists of the following components:

1. **Sensors Data Generation**:
   - `sensors_data.py`: Generates simulated data for air quality, temperature, and humidity.

2. **Publisher**:
   - `pub.py`: Publishes the generated sensor data to an MQTT broker.

3. **Subscriber**:
   - `sub.py`: Subscribes to MQTT topics, processes incoming data, and stores it in databases.

4. **Databases**:
   - **MongoDB**: Stores air quality, temperature, and humidity data.
   - **MySQL**: Stores temperature data.
   - **Neo4j**: Stores location and humidity data.

5. **Docker**:
   - `docker-compose.yaml`: Configuration for running MongoDB, MySQL, and Neo4j services using Docker.

## Technologies Used

- **Python**: Core programming language for data generation, publishing, and subscribing.
- **MQTT**: Protocol for lightweight messaging between publisher and subscriber.
- **VerneMQ**: MQTT broker used for message handling.
- **MongoDB**: NoSQL database for storing sensor data.
- **MySQL**: Relational database for storing temperature data.
- **Neo4j**: Graph database for storing relationships between sensors and environmental data.
- **Docker**: Containerization platform for running database services.

## Installation and Setup

### Prerequisites

- Python 3.8 or higher
- Docker installed on your system

### Steps

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/Barry3wooda/Environment-Monitor
    cd EnvironmentMonitor
    ```

2. **Set Up Python Environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Set Up Databases and MQTT Broker (VenrneMQ) Using Docker**:

    ```bash
    # run docker-compose.yaml
    docker compose up -d
    ```

4. **Run the System**:

    - Start the MQTT subscriber:

        ```bash
        python sub.py
        ```

    - Start the MQTT publisher:

        ```bash
        python pub.py
        ```

## Usage

1. **Publisher**:
   - Generates and sends sensor data to the MQTT broker.
   - Topics:
     - `sensors/air_quality`
     - `sensors/temp`
     - `sensors/humidity`

2. **Subscriber**:
   - Receives data from the MQTT broker.
   - Stores data in MongoDB, MySQL, and Neo4j.

## System Flow

1. **Data Generation**:
   - `sensors_data.py` generates simulated data for air quality, temperature, and humidity.

2. **Publishing**:
   - `pub.py` sends the generated data to the MQTT broker.

3. **Subscribing**:
   - `sub.py` receives the data and processes it.

4. **Storage**:
   - Data is stored in MongoDB, MySQL, and Neo4j for further analysis and visualization.

