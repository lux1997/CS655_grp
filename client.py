#!/usr/bin/python3.7
# -*- coding: UTF-8 -*-
print ('Content-Type: text/html')
print ('')
import socket,pickle,cgi,os,time
from PIL import Image

form=cgi.FieldStorage()
fileitem=form['filename']



fn=os.path.basename(fileitem.filename)

open(fn,'wb').write(fileitem.file.read())
#message = mpimg.imread('/Users/chuci/apa/CGI-Executables/files/'+fn)
img = Image.open(fn)

# get the picture and deal with it.
# store the img information in the img variable
s = socket.socket()
s.connect(('204.102.244.63',1234)) # enter server node ip address

#data = img # image information
#data_b = Image.open("dog.jpg")
data_s = pickle.dumps(img)
num = 0 # try 10 times
while(num<10):
    try:
        print(time.asctime( time.localtime(time.time()) ) + ": send image - attempt " + str(num + 1) + "<br>")
        s.send(str(len(data_s)).encode())
        len = s.recv(1024)
        s.send(data_s)
        print(time.asctime( time.localtime(time.time()) ) + ": successfully send, wait for response...<br>")
        res = s.recv(1024)
        res = res.decode()
        print(time.asctime( time.localtime(time.time()) ) + ": receive response<br><br>")
        print("Result: " + res)
        s.close()
        break
    except Exception:
        num = num + 1
        print('[!] Server not found ot not open')
        continue

##################return the html page with rcv result################

############## connnection part ends

else:
    print ("""\
    <html>
    <head>
    <meta charset="utf-8">
    <title>CS655 geni project</title>
    </head>
    <body>
    <h1>uploading faild!</h1>
    <a href="/index.html">
        <button>back</button>
    </a>
    </body>
    </html>
    """)
