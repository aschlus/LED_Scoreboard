#!/usr/bin/env python3
import sys
import os
import time
import threading
import active_board
import scoreboard_control
import mlb_scoreboard_control
import train_control
import server
import socket
from helpers import render
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import ImageFont


def run(server_socket):

    options = RGBMatrixOptions()
    options.rows = 32
    options.cols = 64
    options.chain_length = 1
    options.parallel = 1
    options.hardware_mapping = 'adafruit-hat-pwm'
    options.gpio_slowdown = 2
    options.brightness = 100

    matrix = RGBMatrix(options=options)

    font = ImageFont.truetype(get_file("assets/fonts/04B_24__.TTF"), 16)

    render.draw_text(matrix, "LOADING...", font, "white", "loading")

    board = active_board.Board()
    board.name = "MLB Scoreboard"

    server_thread = threading.Thread(target=server.start_server, args=[server_socket, matrix, board])
    server_thread.setDaemon(True)
    server_thread.start()

    board_thread = threading.Thread(target=scoreboard_control.run2, args=[matrix, board])
    board_thread.setDaemon(True)
    board_thread.start()

    board_thread = threading.Thread(target=mlb_scoreboard_control.run2, args=[matrix, board])
    board_thread.setDaemon(True)
    board_thread.start()

    train_thread = threading.Thread(target=train_control.run_train, args=[matrix, board])
    train_thread.setDaemon(True)
    train_thread.start()

    while True:
        time.sleep(5)


def get_file(path):
    dir = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(dir, path)


if __name__ == "__main__":
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        run(server_socket)
    except KeyboardInterrupt:
        print("Quit Received")
        server_socket.close()
        print("Socket Closed")
        sys.exit(0)
