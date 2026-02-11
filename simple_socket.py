import socket

####### https://docs.python.org/3/library/socket.html#socket.socket.sendfile #######
#socket.gethostbyname(str(socket.gethostname()))#

HEADER, FORMAT = 64, "utf-8"


class Client:
    def __init__(self, servip, port):
        self.servip = servip
        self.port = port

    def connect(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        ADDR = (self.servip, self.port)
        self.client.connect(ADDR)

    def send(self, msg):
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b" " * (HEADER - len(send_length))
        self.client.sendall(send_length)
        self.client.sendall(message)
    
    def rcv(self):
        msg_length = self.client.recv(HEADER).decode(FORMAT)
        total_received = 0
        if msg_length:
            msg = []
            while total_received < int(msg_length):
                data = self.client.recv(int(msg_length))
                total_received += len(data)
                msg.append(data)
            return b"".join(msg).decode(FORMAT)
        return ""
    
    def close(self):
        self.client.close()
    

class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def start(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ADDR = (self.ip, self.port)
        self.server.bind(ADDR)
        self.conns = []

    def lsn(self, conns=0):
        if conns > 0:
            self.server.listen(conns)
        else:
            self.server.listen()
    
    def accept(self):
        conn, addr = self.server.accept()
        conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.conns.append(conn)
        return conn, addr
        
    def send(self, conns, msg):
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b" " * (HEADER - len(send_length))
        for conn in conns:
            conn.sendall(send_length)
            conn.sendall(message)

    def rcv(self, conn):
        msg_length = conn.recv(HEADER).decode(FORMAT)
        total_received = 0
        if msg_length:
            msg = []
            while total_received < int(msg_length):
                data = conn.recv(int(msg_length))
                total_received += len(data)
                msg.append(data)
            return b"".join(msg).decode(FORMAT)
        return ""
    
    def close(self, conn):
        conn.close()
        self.conns.remove(conn)

