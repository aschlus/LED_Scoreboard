# import socket
# import json
# import _thread
from helpers import render
from flask import Flask, request


def start_server(server_socket, matrix, board):
    app = Flask(__name__)

    @app.route("/data", methods=['POST'])
    def home():
        newBoard = request.json['board']
        if newBoard != board.name:
            board.name = newBoard
            render.push_to_board(matrix, None, board, newBoard)
        matrix.brightness = request.json['brightness']
        return "Done"

    app.run(host='192.168.1.248', port=5000)
