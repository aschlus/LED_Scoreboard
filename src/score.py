#!/usr/bin/env python3
import os
import json
import time

from helpers import render
from PIL import ImageFont


def run2(matrix):

    canvas = matrix.CreateFrameCanvas()

    font = ImageFont.truetype(get_file("assets/fonts/04B_24__.TTF"), 8)
    font2 = ImageFont.truetype(get_file("assets/fonts/sonic_advance_2.ttf"), 16)

    data = json.load(open(get_file("config/scoreboard_config.json")))

    x = 0

    while True:
        image1 = render.convert(data['teams'][x]['logo'])
        # image2 = render.convert(data['teams'][1]['logo'])

        render.draw_img(canvas, image1, data['teams'][x]['position']['scale'],
                        data['teams'][x]['position']['home'])
        render.draw_img(canvas, image1, data['teams'][x]['position']['scale'],
                        data['teams'][x]['position']['away'])

        render.draw_rect(canvas, [21, 32], "black", [21, 0])

        render.draw_text(canvas, "TODAY", font, [22, 1])
        render.draw_text(canvas, "7:00", font, [25, 7])
        render.draw_text(canvas, "VS", font2, [25, 15])

        canvas = matrix.SwapOnVSync(canvas)
        canvas.Clear()

        time.sleep(1.5)
        if (x == len(data['teams']) - 1):
            x = 0
        else:
            x = x + 1


def get_file(path):
    dir = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(dir, path)
