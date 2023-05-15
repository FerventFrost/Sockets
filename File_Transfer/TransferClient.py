import socket
import threading

class ClientFileTransfer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.FileName = input("Enter the name of the file Location you want to send: ")
        self.InitSockets()

    def InitSockets(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))

        self.SendFile(self.FileName)


    def SendFile(self, FileName):
        print(f"Sending File...")
        with open(FileName, 'rb') as file:
            while True:
                data = file.read(1024)
                if not data:
                    break
                self.client_socket.send(data)

        print(f"File '{FileName}' sent successfully!")


if __name__ == "__main__":
    host = 'localhost'
    port = 9979
    ClientFileTransfer(host, port)

