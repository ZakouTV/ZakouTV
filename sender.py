import socket

def send_command(host, port, command):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        client_socket.send(command.encode())
        response = client_socket.recv(4096).decode()
        print(response)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    target_host = '127.0.0.1'  # Change to the target host IP address
    target_port = 8080  # Change to the listener port number
    command_to_send = input("Enter ur command  and type 'exit' if u want to quit: ")

    while command_to_send.lower() != 'exit':
        send_command(target_host, target_port, command_to_send)
        command_to_send = input("Enter ur command and type 'exit' if u want to quit:  ")
