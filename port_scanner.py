'''
Script to check the numebr of ports open on a remote machine

Python Version required - 3.x 

'''

#import socket module 
from socket import *

print ("Simple port scanner")
print ("-------------------")
print ("")

# ip address of machine you want to run a port scanner 
adress = input("Enter adress (or localhost): ")
ip = gethostbyname(adress)

#range of ports you want to run a port scan
alpha = int(input("Port (min):"))
omega = int(input("Port (max):"))

# function to facilitate port scanning 
def scanner(ip,alpha, omega):
    count = 0    
    for ports in range(alpha, omega):
        try:
            print ("Scanning port :%d" %(ports,))
            #making a scoket object for TCP protocol 
            s = socket(AF_INET, SOCK_STREAM)
            #connection timeout
            s.settimeout(3)
            #try to connect to each port 
            s.connect((ip, ports))
            s.settimeout(3)
            print ("Port %d: is OPEN" % (ports,))
            count = count + 1
        except:
            print ("Port %d is CLOSED" % (ports,))
        s.close()
    print ("Scanning finshed !")
    print ("")
    print ("Found %d open ports" % (count))          



if __name__ == "__main__":
    print ("")
    print ("Beggin to scan...")
    scanner(ip,alpha,omega)
