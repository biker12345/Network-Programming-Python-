''' server script that runs three client requests on different threads using
the threading module of python (version 3.x)
'''
#import required modules 
import socket
import threading
import socketserver

#host address , port and size of buffer 
SERVER = 'localhost'
PORT = 0 # port will be dynamically choosen 
SIZE = 1024 # buffer size 

def client(ip,port,msg):
    #connection to the server 
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((ip,port))
    try:
        # send the message ,message should be encoded for python3.x
        sock.sendall(msg)
        response = sock.recv(SIZE)
        print('client recevied : %s'%response)
    finally :
        sock.close()


# request handler ,using the predefined socket server module features 
class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        current_thread = threading.current_thread
        response = str('%s: %s'%(current_thread,data)).encode()
        self.request.sendall(response)

# nothing to do ,hence pass used ,everything already inherited 
class ThreadedTCPServer(socketserver.ThreadingMixIn,socketserver.TCPServer):
    pass


# driver area for the server and creation of three clients 
if __name__ == '__main__':
    server = ThreadedTCPServer((SERVER,PORT),ThreadedTCPRequestHandler)
    ip,port = server.server_address
    server_thread = threading.Thread(target = server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print("server loop running on thread : %s"%server_thread.name)
    client(ip,port,b"hello from client 1")
    client(ip,port,b"hello from client 2")
    client(ip,port,b"hello from client 3")
    server.shutdown()
