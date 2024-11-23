
# Python gRPC Streaming - Sensor Monitoring

## Description

This project demonstrates a proof of concept for using gRPC with Python to implement a streaming server for sensor data monitoring. The project consists of a server that receives sensor data from multiple clients and streams back alerts in real-time based on the sensor readings. The communication between the clients and server occurs via gRPC, which allows for efficient and scalable bidirectional streaming.

The system simulates multiple sensor clients sending temperature and humidity data to the server. The server processes the data and sends back alerts if certain conditions are met (e.g., temperature exceeds a threshold).

This can serve as a useful reference for those looking to implement real-time communication between clients and servers using gRPC in Python.

## Requirements

- Python 3.8 or higher
- gRPC tools for Python

You can install the dependencies via pip:

```bash
pip install -r requirements.txt
```

## Mode of Use

### 1. Clone the repository:
```bash
git clone https://github.com/ferrerallan/python-grpc
cd python-grpc
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Compile the protobuf definitions:
Before running the server and client, compile the `.proto` file to generate the necessary Python code.

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. sensor_monitoring.proto
```

### 4. Run the server:
Start the gRPC server that listens for sensor data streams and sends alerts.

```bash
python server.py
```

### 5. Run the client:
Each client simulates a sensor device sending data. You can start multiple clients to simulate multiple sensors.

```bash
python client.py <sensor_name>
```

For example, to start a client for a sensor named "sensor_1":

```bash
python client.py sensor_1
```

You can start multiple clients, each with a unique sensor name, in different terminal windows to simulate a multi-sensor environment.

### 6. Monitor alerts:
The server will process the incoming data from the clients and return alerts. The clients will display these alerts in real-time. If the temperature exceeds a threshold, a critical alert will be shown.

## Protobuf Definitions

The project uses `sensor_monitoring.proto` to define the structure of the gRPC service and messages. The service allows bidirectional streaming for sensor data and alerts.

- **SensorData**: Represents the data sent by each sensor, including temperature, humidity, and a timestamp.
- **Alert**: Represents the alerts sent by the server, which may include a critical flag if certain conditions are met.


