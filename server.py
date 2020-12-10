import socketserver
import socket
import pickle
import time
from classifier import Classifier
import numpy as np
from PIL import Image

encoding = 'utf-8'
BUFSIZE = 1024
clf = Classifier()

class MyServer(socketserver.StreamRequestHandler):
    def handle(self):
        while True:
            length_s = self.request.recv(BUFSIZE)
            if length_s:
                length_s = length_s.decode()
                length = int(length_s)
                self.request.send('Image size received...'.encode())
                str_data = b''
                num = 0
                while num < length:
                    packet = self.request.recv(BUFSIZE)
                    if not packet:
                        break
                    str_data += packet
                    num += len(packet)
                    
                img = pickle.loads(str_data)
                #img.save("img2.jpg", "JPEG")
                # img = Image.open("data/dog.jpg")
                res = clf.predict(img)
                print(res)
                self.request.send(res.encode())
            else:
                break
            time.sleep(3600)

if __name__ == "__main__" :
    host = socket.gethostname()
    port = 1234
    s = socketserver.ThreadingTCPServer((host, port), MyServer)
    s.serve_forever()
