#!/usr/bin/env python3
import time
import sys

import render

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw, ImageFont


def run2():
    url1 = 'http://thecraftchop.com/files/images/washington-capitals2.svg'
    url2 = 'https://assets.nhle.com/logos/nhl/svg/ANA_dark.svg'
    url3 = 'https://assets.nhle.com/logos/nhl/svg/NYR_dark.svg'

    # cairosvg.svg2png(file_obj=open("DesktopScoreboard/Logo_Files/WSH_alt.svg", "rb"), write_to=out1)

    # Configuration for the matrix
    options = RGBMatrixOptions()
    options.rows = 32
    options.cols = 64
    options.chain_length = 1
    options.parallel = 1
    options.hardware_mapping = 'adafruit-hat-pwm'
    options.gpio_slowdown = 2
    options.brightness = 100

    matrix = RGBMatrix(options=options)

    image1 = render.convert(url1)
    image2 = render.convert(url3)

    # matrix.SetImage(image1.convert('RGB'), -11, -6)
    # matrix.SetImage(image2.convert('RGB'), 22, 3)

    render.draw_img(matrix, image1, .85, [(-matrix.width / 4) + 1, 2])
    render.draw_img(matrix, image2, .80, [(matrix.width * 2 / 4) - 7, 3])

    render.draw_rect(matrix, [21, 32], "black", [21, 0])

    font = ImageFont.truetype("04B_24__.TTF", 8)
    font2 = ImageFont.truetype("sonic_advance_2.ttf", 16)

    render.draw_text(matrix, "TODAY", font, [22, 1])
    render.draw_text(matrix, "7:00", font, [25, 7])
    render.draw_text(matrix, "VS", font2, [25, 15])
