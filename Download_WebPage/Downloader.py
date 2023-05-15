import socket

class Downloader:
    def __init__(self, url):
        self.url = url
        self.host = url.split('/')[2]
        self.path = '/' + '/'.join(url.split('/')[3:])

    def InitSocket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.host, 80))
        return sock
    
    def SendRequest(self, sock):
        print('Connecting GET %s HTTP/1.0' % self.path)
        request = 'GET %s HTTP/1.0\r\nHost: %s\r\n\r\n' % (self.path, self.host)
        sock.send(request.encode())

    def ReceiveResponse(self, sock):
        response = b''
        while True:
            data = sock.recv(4096)
            if not data:
                break
            response += data
        return response
    
    def download(self):
        print('Downloading: %s' % self.url)
        sock = self.InitSocket()
        self.SendRequest(sock)
        page = b''
        page = self.ReceiveResponse(sock)
        sock.close()
        return page

    def save(self, filename):
        page = self.download()
        with open(filename, 'wb') as f:
            f.write(page)
        return page


if __name__ == '__main__':
    url = 'https://crawler-test.com/'
    downloader = Downloader(url)
    downloader.save('CrawlerTest.html')
    print('Done!')
