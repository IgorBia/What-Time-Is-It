import socket
import sys
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("IP")
parser.add_argument("PORT", type=int)
args = parser.parse_args()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (args.IP, args.PORT)
data = [0, 0]
myTime = 0
i = 0

print("starting up on {} port {}".format(*server_address))

sock.bind(server_address)
sock.listen(1)

print("waiting for a connection...")
connection, client_address = sock.accept()
try:
    print("connection from", client_address)

    while i<=1:
        data[i] = (connection.recv(120000))
        if i==0:
            myTime = time.time()
        print("received {!r}".format(data[i].decode()))
        if data[i]:
                print("sending data back to the client...")
                connection.send(data[i])
                i+=1
        else:
            break
    difference = myTime - (float(data[0].decode()) + float(data[1].decode()))
    print (difference, " seconds - this is difference of times")
    connection.send(str(difference).encode())

finally:
    connection.close()
