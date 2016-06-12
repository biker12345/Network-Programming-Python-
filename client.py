''' client script for echo server '''

#import required modules 
import socket
import sys
import argparse
import time

host = 'localhost'

def echo_client(port):
    #socket connection
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #make an address,port tupple
    server_address = (host,port)

    #connection to the server
    sock.connect(server_address)

    try:
        msg = b'hello server how are you today everything good?'

        #send data to server
        sock.sendall(msg)
        
        #look for response
        amt_rec = 0
        amt_exp = len(msg)
        #receive untill received data not equal to the length of sent data
        while amt_rec < amt_exp:
            data = sock.recv(2)
            amt_rec += len(data)
            time.sleep(1)
            print("received :"+str(data))
    except Exception:
        print("Exception occured")
    finally :
        print("closing connection")
        sock.close()

# take port number as command line argument 
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= "client exmple")
    parser.add_argument('--port',action='store',dest='port',type=int,required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)
    
