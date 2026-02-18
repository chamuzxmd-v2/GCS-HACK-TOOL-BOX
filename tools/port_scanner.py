import socket

host = input("Host: ")
for port in range(1,100):
    s = socket.socket()
    s.settimeout(0.5)
    if s.connect_ex((host,port))==0:
        print("Open Port:", port)
    s.close()
