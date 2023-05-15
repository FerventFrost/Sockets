import socket
import threading

class ServerFieleTransfer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.FileName = input("Enter the name of the file Location you want to save: ")
        self.InitSockets()

    def InitSockets(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(2)

        print(f"Server started on {self.host}:{self.port}")
        
        client_socket, client_address = self.server_socket.accept()
        self.handle_client(client_socket, client_address)
                

    def handle_client(self, client_socket, client_address):
        try:
            self.SaveFile(client_socket)
        except Exception as e:
            print(f"Error handling client: {client_address[0]}\n{e}")
            
        client_socket.close()

    def SaveFile(self, client_socket):
        with open(self.FileName, 'wb') as file:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                file.write(data)
        

if __name__ == '__main__':
    server_address = 'localhost'
    server_port = 9979

    server = ServerFieleTransfer(server_address, server_port)
    server.StartServer()


