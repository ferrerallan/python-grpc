import grpc
from concurrent import futures
import order_pb2
import order_pb2_grpc

class OrderService(order_pb2_grpc.OrderServiceServicer):
    def CreateOrder(self, request, context):        
        order_id = "ORDER-123"
        message = f"Order created! ID: {order_id}"
        return order_pb2.OrderConfirmation(order_id=order_id, message=message)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_pb2_grpc.add_OrderServiceServicer_to_server(OrderService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()