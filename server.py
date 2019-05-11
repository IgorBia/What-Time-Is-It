import socket
import sys
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10001)
data = [0, 0]
myTime = 0
i = 0

print('starting up on {} port {}'.format(*server_address))

sock.bind(server_address)
sock.listen(1)

print('waiting for a connection', i)
connection, client_address = sock.accept()
try:
    print('connection from', client_address)

    while i<=1:
        data[i] = (connection.recv(120000))
        if i==0:
            myTime = time.time()
        print('received {!r}'.format(data[i]))
        if data[i] and i<=1:
                print('sending data back to the client')
                connection.send(data[i])
                i+=1
        else:
            break

finally:
    connection.close()

difference = myTime - (float(data[0].decode()) + float(data[1].decode()))
print (difference, "- this is difference of times")
