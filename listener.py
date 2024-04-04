import socket
import subprocess

def start_listener(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', port))
    server_socket.listen(5)

    print(f"Listening on port {port}...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        while True:
            data = client_socket.recv(1024).decode().strip()
            if not data:
                break
            elif data.lower() == 'exit':
                client_socket.close()
                break
            else:
                try:
                    result = subprocess.check_output(data, shell=True)
                    client_socket.send(result)
                except Exception as e:
                    client_socket.send(str(e).encode())

if __name__ == "__main__":
    listener_port = 8080  
    start_listener(listener_port)
