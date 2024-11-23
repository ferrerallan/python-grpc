import grpc
import time
import random
import sys

import sensor_monitoring_pb2
import sensor_monitoring_pb2_grpc

def run(sensor_name):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = sensor_monitoring_pb2_grpc.SensorMonitoringServiceStub(channel)

        def generate_sensor_data():
            while True:
                request = sensor_monitoring_pb2.SensorData(
                    sensor_id=sensor_name,
                    temperature=random.uniform(10, 25),  
                    humidity=random.uniform(40, 60),    
                    timestamp=int(time.time())
                )
                yield request
                time.sleep(0.5)

        responses = stub.StreamSensorData(generate_sensor_data())
        for response in responses:
            if response.critical:
                print("\033[91m" + f"CRITICAL ALERT: {response.message}" + "\033[0m") 
            else:
                print(f"[*] {response.message}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python client.py <sensor_name>")
        sys.exit(1)
    sensor_name = sys.argv[1]
    run(sensor_name)