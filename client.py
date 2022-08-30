import socket
import time
c = socket.socket()
host = 'Admin-PC'
port = 8080
c.connect((host,port))
message = c.recv(1024)
message = message.decode()
print(message)
while 1:
     ot = input(str('enter : '))
     ot = ot.encode()
     ot = c.send(ot)
#time.sleep(3)
             
