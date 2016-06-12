''' script that sends message to you cell using way2sms .com , works only on python 2.x version'''

#import required modules 
import urllib2
import cookielib
from getpass import getpass
import os
import sys

#enter the way2sms registered number and password
username = raw_input("Enter Sender's Number :")
passwd = raw_input("Enter Sender's Password :")

# enter the message you want to send with the number you want to do so 
message = raw_input("Enter Message :")
number = raw_input("Enter reciever phone number :")

#add + after each word in the message to create the message in sendable format 
message = "+".join(message.split(' '))


#Logging into the SMS Site
url = 'http://site24.way2sms.com/Login1.action?'
data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
    

#For Cookies:
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))


# Adding Header detail:
opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]


try:
    #open the url using the above data 
    usock = opener.open(url, data)

except IOError:
    print "\n CAN NOT CONNECT TO SERVER...CHECK USERNAME AND PASSWORD AND INTERNET CONNECTION ALSO"
    raw_input("\n PRESS ENTER TO EXIT")
    sys.exit(1)


#create session id ,create the post url 
session_id = str(cj).split('~')[1].split(' ')[0]
send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
send_sms_data = 'ssaction=ss&Token='+session_id+'&mobile='+number+'&message='+message+'&msgLen=136'
opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+session_id)]
    

try:
    #send the data to webpage 
    sms_sent_page = opener.open(send_sms_url,send_sms_data)

except IOError:
    print "\n ERROR WHILE SENDING THE SMS...PLEASE UPDATE THE CONTACT LIST"
    sys.exit(1)

#print in case of success
print "\n\n\t[+] SMS SENT"

  
