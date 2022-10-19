#!/usr/bin/env python3
import os
import threading
import time
import train_loop

from helpers import render
from PIL import ImageFont

module = "Metro"


def run_train(matrix, board):

    canvas = matrix.CreateFrameCanvas()

    font = ImageFont.truetype(get_file("assets/fonts/Test_Font.ttf"), 8)
    font2 = ImageFont.truetype(get_file("assets/fonts/sonic_advance_2.ttf"), 16)

    next_train = []
    loop = threading.Thread(target=train_loop.data_loop, args=[next_train])
    loop.setDaemon(True)
    loop.start()

    while True:
        shown = False
        switch = False
        render.draw_text(canvas, "NEXT TRAIN", font, "white", "center_status")
        for train in next_train:
            switch = True
            train.display_train()
            if not shown:
                render.draw_text(canvas, train.line, font, train.color, "center_time")
                render.draw_text(canvas, train.time, font2, "white", "center_score")
                shown = True
        print("-------------------------------")

        if switch:
            canvas = render.push_to_board(matrix, canvas, board, module)
            canvas.Clear()

        time.sleep(5)


def get_file(path):
    dir = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(dir, path)
