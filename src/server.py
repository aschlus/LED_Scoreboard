# import socket
# import json
# import _thread
from flask import Flask, request, jsonify


def start_server(server_socket, matrix, board):
#     host = '192.168.1.248'
#     port = 5000
#
#     server_socket.bind((host, port))
#
#     print("Server running at " + host + ":" + str(port))
#
#     server_socket.listen(2)
#
#     kill_flag = False
#
#     while True:
#         conn, address = server_socket.accept()
#         print("Connection from: " + str(address))
#
#         while True:
#             data = conn.recv(1024).decode('utf-8')
#             if not data:
#                 print("Closing...")
#                 break
#             parsed_data = json.loads(data)
#             print(parsed_data)
#             matrix.brightness = parsed_data['brightness']
#             board = parsed_data['board']
#             kill_flag = parsed_data['kill_flag']
#
#         print("Connection closed")
#         conn.close()
#         if kill_flag:
#             print("Killing...")
#             _thread.interrupt_main()
    app = Flask(__name__)

    @app.route("/data", methods=['POST'])
    def home():
        # print(jsonify(request))
        matrix.brightness = request.json['brightness']
        return "Hello World!"

    app.run(host='192.168.1.248', port=5000)
