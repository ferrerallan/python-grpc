import socket
import time

def get_current_time():    
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def handle_client(client_socket):    
    try:
        while True: 

            client_socket.recv(1024) 

            current_time = get_current_time()

            client_socket.send(current_time.encode()) 
    finally:
        client_socket.close()

def start_server():
    host = '127.0.0.1' 
    port = 65432       

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")
        while True:
            conn, addr = s.accept()
            print(f"Connected by {addr}")
            handle_client(conn)

if __name__ == "__main__":
    start_server()