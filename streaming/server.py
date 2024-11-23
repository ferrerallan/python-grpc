import grpc
from concurrent import futures
import time

import sensor_monitoring_pb2
import sensor_monitoring_pb2_grpc

class SensorMonitoringServiceServicer(sensor_monitoring_pb2_grpc.SensorMonitoringServiceServicer):
    def StreamSensorData(self, request_iterator, context):
        for sensor_data in request_iterator:
            print(f"Received: {sensor_data}")
            message = f"Sensor {sensor_data.sensor_id} - Temperature: {sensor_data.temperature}, Humidity: {sensor_data.humidity}"
            yield sensor_monitoring_pb2.Alert(message=message, 
                                              critical=True if sensor_data.temperature > 20 else False)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sensor_monitoring_pb2_grpc.add_SensorMonitoringServiceServicer_to_server(
        SensorMonitoringServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()