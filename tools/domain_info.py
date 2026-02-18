import socket

domain = input("Enter domain: ")
print("IP:", socket.gethostbyname(domain))
