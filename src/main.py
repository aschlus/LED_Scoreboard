#!/usr/bin/env python3
import sys
import os
import time
import threading
import score
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw, ImageFont
# from assets import fonts


def run():
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

    loading = Image.new("RGB", size=(matrix.width, matrix.height))
    loadingdraw = ImageDraw.Draw(loading)
    loadingdraw.text((0, 0), "LOADING...", font=font, fill="white")
    loading = loading.crop(loading.getbbox())

    matrix.SetImage(loading.convert('RGB'), 1, 10)
    time.sleep(3)

    t = threading.Thread(target=score.run2, args=[matrix])
    t.setDaemon(True)
    t.start()

    while True:
        time.sleep(100)


def get_file(path):
    dir = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(dir, path)


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("Quit Received")
        sys.exit(0)
