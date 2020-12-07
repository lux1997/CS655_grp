import SocketServer
import socket
import pickle

encoding = 'utf-8'
BUFSIZE = 1024

class MyServer(SocketServer.StreamRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(BUFSIZE)
            if data:
                img = pickle.loads(data)
                
                # 
                # res = classifier.predict(img)

                res = "hello, client"
                print(res)
                self.request.send(pickle.dumps(res))
            else:
                break

if __name__ == "__main__" :
    host = socket.gethostname()
    port = 1234
    s = SocketServer.ThreadingTCPServer((host, port), MyServer)
    s.serve_forever()