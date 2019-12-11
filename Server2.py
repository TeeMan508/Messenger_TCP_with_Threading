import socket
import threading


class Server:

        def __init__(self):
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connections = []
            self.clients_adr = []
            self.sock.bind(('0.0.0.0', 9090))
            self.sock.listen(2)

        def handler(self, con, adr):
            while True:
                try:
                    data = con.recv(1024)
                    print('data received')
                    for connection in self.connections:
                        #if con != connection:
                            connection.send(data)
                    print('data sended')
                except socket.error:
                    print('Someone disconected')
                    break


        def run(self):
            while True:
                conn, addr = self.sock.accept()
                #conn.send('You are connected'.encode('utf-8'))
                #conn.send('Test'.encode('utf-8'))
                hThread=threading.Thread(target=self.handler, args = (conn, addr))
                hThread.daemon = True
                hThread.start()
                self.clients_adr.append(addr)
                self.connections.append(conn)
                print(self.connections)


my_server = Server()
my_server.run()



