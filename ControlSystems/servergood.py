import socket
import threading


p = input("Enter the server IP: ")
HOST = p  # Enter IP or Hostname of your server
PORT = 12345 # Pick an open Port (1000+ recommended), must match the server port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

clientsocket, address = s.accept()
print(f"Connection from {address} has been established.")

def telemetryReceive():
    while True:
        reply = clientsocket.recv(1024)
        if len(reply) > 2:
            print(reply)

def telemetrySend():
    while True:
        command = input('Enter your command: ')
        if command != None:
            clientsocket.send(bytes(command, 'utf-8'))

def main():
    threading.Thread(target=telemetryReceive).start()
    threading.Thread(target=telemetrySend).start()


main()
