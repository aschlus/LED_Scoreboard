#!/usr/bin/env python3
import socket
import json


host = '192.168.1.248'
port = 5000

json_m = {
    'brightness': 100,
    'board': 'scoreboard',
    'kill_flag': True
}

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
client_socket.sendall(json.dumps(json_m))
# data = client_socket.recv(1024)
# print("Received: " + str(data))
client_socket.shutdown(socket.SHUT_RDWR)
client_socket.close()
