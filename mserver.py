import socket
import mysql.connector as qw
#dat = qw.connect(host='localhost',user='root',passwd='')
#up = dat.cursor()
#up.execute('create database if not exists  backup;')
#up.execute('use backup;')
#up.execute('create table if not exists message (inmessage varchar(200),Date date,timing  time);')
s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host,port))
print('socket is create code is ',host)
s.listen(2)

con , addr = s.accept()
con1 , addr1 = s.accept()
print(f'connection 1 is {addr}')
print(f'connection 2 is {addr1}')
print('server has connect to  ; {}'.format(addr))
message = str('Welcome').encode()
message = con.send(bytes(message))
message = con1.send(bytes(message))
while True:
     inmess = con.recv(1024)
     inmess = inmess.decode()
     inmess2= con1.recv(1024)
     inmess2= inmess2.decode()
#     up.execute('insert into  message values("{}",curdate(),curtime())'.format(inmess))
 #    dat.commit()
     print(f' message form connection 1 {inmess}')
     print(f'message form connection 2 {inmess2}')
     
     
