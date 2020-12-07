#!C:\Users\18656\AppData\Local\Programs\Python\Python38-32\python.exe
# -*- coding: UTF-8 -*-
print ('Content-Type: text/html')
print ('')
import socket,pickle,cgi

form=cgi.FieldStorage()
# get the picture and deal with it.
# store the img information in the img variable
s = socket.socket()
s.connect(('192.168.1.102',1234)) # enter server node ip address
#data = img # image information
data_s = 'test,test'
num = 0 # try 10 times
while(num<10):
    try:
        s.send(data_s)
        rcv = s.recv(1024) # reveive the result( a number)
        s.close()
        break
    except Exception:
        num = num + 1
        print('[!] Server not found ot not open')
        continue
##################return the html page with rcv result################