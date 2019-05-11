import socket
import sys
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10001)
print('connecting to {} port {}'.format(*server_address))

def TCP(message):

    try:

        print('sending', message)
        sock.send(bytes(message, 'utf-8'))

        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(1024)
            amount_received += len(data)
            print('received', data)

    finally:
        return data

sock.connect(server_address)

firstTime = TCP(str(time.time()))
difference = time.time() - float(firstTime.decode())

TCP(str(difference*0.5))
print('closing socket')
sock.close()
