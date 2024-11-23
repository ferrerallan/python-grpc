import socket
from time import sleep

def get_time_from_server():
    """Connects to the server, gets the time, and prints it."""
    host = '127.0.0.1'  # The server's hostname or IP address
    port = 65432        # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            s.sendall(b'hi')  # Send a message to the server
            data = s.recv(1024)
            print(f"Received from server: {data.decode()}")

            sleep(2)

if __name__ == "__main__":
    get_time_from_server()