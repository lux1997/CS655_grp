#!C:\Users\18656\AppData\Local\Programs\Python\Python38-32\python.exe
# -*- coding: UTF-8 -*-
print ('Content-Type: text/html')
print ('')
import socket,pickle,cgi
import cv2
import numpy
import time
import sys
from PIL import Image
import pickle

form=cgi.FieldStorage()
# get the picture and deal with it.
# store the img information in the img variable
s = socket.socket()
s.connect((socket.gethostname(),1234)) # enter server node ip address

#data = img # image information
data_b = Image.open("data/dog.jpg")
data_s = pickle.dumps(data_b)
print(len(data_s))

num = 0 # try 10 times
while(num<10):
    try:
        s.send(str(len(data_s)).encode())
        rcv = s.recv(1024)  # reveive the result( a number)
        rcv = rcv.decode()
        print(rcv)
        s.send(data_s)
        res = s.recv(1024)  # reveive the result( a number)
        res = rcv.decode()
        print("result: ", res)
        s.close()
        break
    except Exception:
        num = num + 1
        print('[!] Server not found ot not open')
        continue
##################return the html page with rcv result################