from socket import *
import struct

file_name='2.jpg'
server_ip='192.168.0.104'
s=socket(AF_INET,SOCK_DGRAM)
data=struct.pack('!H%dsb5sb'%len(file_name),1,file_name.encode(),0,'octet'.encode(),0)
s.sendto(data,(server_ip,69))
file_name=open(file_name,'ab')
while True:
    recv=s.recvfrom(1024)
    caozuoma,ackma=struct.unpack('!HH',recv[0][:4])
    if caozuoma==5:
        print('文件不存在')
        break
    port=recv[1][1]
    file_name.write(recv[0][4:])
    if len(recv[0])<516:
        print('文件传输完毕')
        break
    yanzhenma=struct.pack('!HH',4,ackma)
    s.sendto(yanzhenma,(server_ip,port))

