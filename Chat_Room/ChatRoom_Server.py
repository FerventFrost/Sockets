import socket
import threading

class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.InitSocket()

    def InitSocket(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)

        self.clients = []  # List to store client sockets

        print(f"Server started on {host}:{port}")

        # Server main loop
        while True:
            client_socket, client_address = self.server_socket.accept()
            self.clients.append(client_socket)

            ClientName = client_socket.recv(1024).decode('utf-8')
            self.broadcast_message(f"{ClientName} has joined the chat room.", client_socket)

            # Start a new thread to handle the client connection
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
            client_thread.start()

    # Function to handle client connections
    def handle_client(self, client_socket, client_address):
        while True:
            try:
                # Receive message from client
                message = client_socket.recv(1024).decode('utf-8')
                if message:
                    print(f"{message}")
                    self.broadcast_message(message, client_socket)
            except Exception as e:
                print(f"Error handling client: {client_address[0]}\n{e}")
                break

        # Remove client from the list
        self.clients.remove(client_socket)
        client_socket.close()

    # Function to broadcast message to all clients
    def broadcast_message(self, message, sender_socket):
        for client in self.clients:
            if client != sender_socket:
                    client.send(f"{message}".encode('utf-8'))
                    

if __name__ == "__main__":
    host = 'localhost'
    port = 5555
    ChatServer(host, port)