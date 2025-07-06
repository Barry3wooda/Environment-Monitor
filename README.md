# Environment Monitor

This project simulates the monitoring of environmental data using sensors. It generates data for air quality, temperature, and humidity, publishes it to an MQTT broker, and stores the data in MongoDB, MySQL, and Neo4j databases.

## Project Structure

- `docker-compose.yaml`: Configuration for running the required services (MongoDB, MySQL, Neo4j) using Docker.
- `pub.py`: Publishes generated sensor data to the MQTT broker.
- `sub.py`: Subscribes to MQTT topics, processes incoming data, and stores it in databases.
- `sensors_data.py`: Contains functions to generate sensor data for air quality, temperature, and humidity.
- `README.md`: Documentation for the project.
- `requirements.txt`: Lists Python dependencies for the project.

## Installation and Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/Barry3wooda/EnvironmentMonitor
    cd EnvironmentMonitor
    ```

2. Set up a Python virtual environment and install dependencies:

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Set up databases using Docker:
   
   Ensure Docker is installed on your system. Use the following Docker commands to run the MongoDB, MySQL, and Neo4j containers.

    ```bash
    # Set up the database services
    docker compose up -d
    ```

4. Run the system:
   - Start the MQTT subscriber by running `sub.py`:

    ```bash
    python sub.py
    ```

   - Start the MQTT publisher by running `pub.py`:

    ```bash
    python pub.py
    ```

