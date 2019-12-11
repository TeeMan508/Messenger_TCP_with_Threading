import socket
import threading
import datetime


class Client:

    def rec_data(self):
        while True:
            data = self.sock.recv(1024)
            print()
            print(data.decode('utf-8'))

    def send_data(self):
         while True:
            self.sock.send((str(datetime.datetime.now()) + ' ' + self.name + '(' + self.address + ')' + ' said: ' + input("Input Your message: ")).encode('utf-8'))
            #print('data sent')


    def __init__(self, address):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((address, 9090))
        self.name = input("Input your name: ")
        self.address = address


    def run(self):
            threading.Thread(target=self.rec_data, daemon=False).start()
            threading.Thread(target=self.send_data).start()




my_client = Client('127.0.0.1')
my_client.run()

