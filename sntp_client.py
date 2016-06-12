''' SNTP (simple network transfer protocol )client script to get time,
    day and date from a remote SNTP server '''

#import area
import socket
import struct
import sys
import time

#global variables
NTP_SERVER = "0.uk.pool.ntp.org" #remote NTP server Address
TIME = 2208988800 #Epoch

def sntp_client():

    #socket connection 
    client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #data formated
    data = str("\x1b"+ 47 * '\0').encode()

    #send data to the server
    client.sendto(data,(NTP_SERVER,123))

    #recieve 1024 bytes of data chunk
    data ,address = client.recvfrom(1024)

    #unpack the data using the unpack function of struct module
    t = struct.unpack('!12I',data)[10] #actual data starts from 10th index

    #subtact the 1970 time (epoch) to get the current time
    t -= TIME

    # print the time 
    print (time.ctime(t))



if __name__ == "__main__":
    sntp_client()
