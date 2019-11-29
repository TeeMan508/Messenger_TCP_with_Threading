import socket
import threading

class Server:
        sock =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connections = []

        def __init__(self):
            self.sock.bind(('0.0.0.0', 9090))
            self.sock.listen(2)

        def handler(self, con, adr):
            while True:
                data = con.recv(1024)
                print('data received')
                for connection in self.connections:
                    connection.send(data)
                print('data sended')
                if not data:
                    break


        def run(self):
            while True:
                conn, addr = self.sock.accept()
                conn.send('You are connected'.encode('utf-8'))
                hThread=threading.Thread(target=self.handler, args = (conn, addr))
                hThread.daemon = True
                hThread.start()
                self.connections.append(conn)
                print(self.connections)


my_server = Server()
my_server.run()



