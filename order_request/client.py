import grpc
import order_pb2
import order_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = order_pb2_grpc.OrderServiceStub(channel)
        response = stub.CreateOrder(order_pb2.OrderRequest(
            customer_name="João Silva",
            product_name="Produto A",
            quantity=2
        ))
        print(f"Answer from server: {response.message}")

if __name__ == '__main__':
    run()