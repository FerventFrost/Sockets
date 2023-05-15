import socket
import threading


class ChatClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.InitSocket()


    def InitSocket(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))

        self.ClientName = input("Enter your name: ")
        self.client_socket.send(self.ClientName.encode('utf-8'))

        self.receive_thread = threading.Thread(target=self.receive_messages, args = (self.ClientName,))
        self.receive_thread.start()

        self.send_thread = threading.Thread(target=self.send_messages, args = (self.ClientName,))
        self.send_thread.start()
        
    def receive_messages(self, ClientName):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    print(f"...\n{message}\n{ClientName} > ", end="")
            except Exception as e:
                print(f"Error receiving message from server:\n{e}")
                break

    def send_messages(self, ClientName):
        while True:
            message = input(f"{self.ClientName} > ")
            self.client_socket.send(f"{ClientName} > {message}".encode('utf-8'))


if __name__ == "__main__":
    host = 'localhost'
    port = 5555
    ChatClient(host, port)