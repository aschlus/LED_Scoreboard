# import socket
# import json
# import _thread
from flask import Flask, request, jsonify


def start_server(server_socket, matrix, board):
    app = Flask(__name__)

    @app.route("/data", methods=['POST'])
    def home():
        board.name = request.json['board']
        matrix.brightness = request.json['brightness']
        return "Done"

    app.run(host='192.168.1.248', port=5000)
