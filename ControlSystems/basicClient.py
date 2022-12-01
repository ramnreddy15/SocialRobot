import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.86.136', 12345))

full_msg = ''
while True:
    action = s.recv(1024).decode('UTF-8')
    if len(action) > 0:
        print("Received|"+action)