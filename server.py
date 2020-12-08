import socketserver
import socket
import pickle
from classifier import Classifier
import numpy as np
from PIL import Image
import cv2

encoding = 'utf-8'
BUFSIZE = 1024

class MyServer(socketserver.StreamRequestHandler):
    def handle(self):
        while True:
            length_s = self.request.recv(BUFSIZE)
            if length_s:
                length_s = length_s.decode()
                length = int(length_s)
                str_data = b""
                num = 0
                while num < length:
                    packet = self.request.recv(4096)
                    if not packet:
                        break
                    str_data += packet
                    num += 4096
                    #print(num)
                #print(length)
                img = pickle.loads(str_data)
                #img.save("img2.jpg", "JPEG")
                clf = Classifier()
                # img = Image.open("data/dog.jpg")
                res = clf.predict(img)
                print(res)
                self.request.send(pickle.dumps(res))
            else:
                break

if __name__ == "__main__" :
    host = socket.gethostname()
    port = 1234
    s = socketserver.ThreadingTCPServer((host, port), MyServer)
    s.serve_forever()
