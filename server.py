import SocketServer
import socket
import pickle
import numpy as np
from classifier import Classifier
from PIL import Image
import cv2

encoding = 'utf-8'
BUFSIZE = 1024

class MyServer(SocketServer.StreamRequestHandler):
    def handle(self):
        while True:
            length = self.request.recv(16)
            if length:
                str_data = self.request.recv(int(length))

                data = np.frombuffer(str_data, np.uint8)
                img = cv2.imdecode(data, cv2.IMREAD_COLOR)

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
    s = SocketServer.ThreadingTCPServer((host, port), MyServer)
    s.serve_forever()