import socket
import threading

HOST = '10.64.173.71' # Enter IP or Hostname of your server
PORT = 12345 # Pick an open Port (1000+ recommended), must match the server port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

try:
    s.bind((HOST, PORT))
except socket.error:
    print ('Bind failed ')

s.listen(5)
print ('Socket awaiting messages')
(conn, addr) = s.accept()
print ('Connected')

def telemetryReceive():
while True:
reply = s.recv(1024)
if reply != None:
print(reply)

def telemetrySend():
while True:
command = input('Enter your command: ')
if command != None:
s.send(bytes(command, 'utf-8'))

def main():
threading.Thread(target=telemetryReceive).start()
threading.Thread(target=telemetrySend).start()

main()