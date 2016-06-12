''' Script to run an echo server on a local host and connect with client programs '''

#required modules
import sys
import socket
import argparse

#global variables
host = 'localhost'
data_payload = 2048 #amout of data to read from client message
backlog = 5 #maximum number of waiting connections allowed

def echo_server(port):

    #socket connections
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #enable reuse address or port
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    #address and port binding
    server_address = (host,port)

    #binding of socket object
    print("starting the server")
    sock.bind(server_address)

    #start listing to the client with backlog count
    sock.listen(backlog)

    while True:
        print("waiting for the client ")
        client,add = sock.accept()

        #receving data from the client with data_palyload limit
        data = client.recv(data_payload)

        #sending of data back to client and closing of connection
        if data:
            print("sent data back to client ")
            client.send(data)
        client.close()


if __name__ == '__main__':
    #getting port as command line argument 
    parser = argparse.ArgumentParser(description = "socket server")
    parser.add_argument ('--port',action='store',dest='port',type=int,required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)
    
