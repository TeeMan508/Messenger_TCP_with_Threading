import socket
import threading
import time


class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send_data(self):
         while True:
            self.sock.send(input("Input your message").encode('utf-8'))
            print('data sent')

    def __init__(self, address):
        self.sock.connect((address, 9090))
        iThread = threading.Thread(target=self.send_data())
        iThread.daemon = True
        iThread.start()
        while True:
            iThread.join()
            data = self.sock.recv(1024)


            if not data:
                  #print('No data')
                  break

            print('data received')
            print(data.decode('utf-8'))

my_client = Client('192.168.0.70')




