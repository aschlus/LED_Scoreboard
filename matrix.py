#!/usr/bin/env python
import time
import sys
import cairosvg

from io import BytesIO

# rgbmatrix = Scoreboard.matrixmodule.rpi-rgb-led-matrix.bindings.python.rgbmatrix
sys.path.append('matrixmodule/rpi-rgb-led-matrix/bindings/python')

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

# if len(sys.argv) < 2:
#     sys.exit("Require an image argument")
# else:
#     image_file = sys.argv[1]

url = 'https://assets.nhle.com/logos/nhl/svg/WSH_light.svg'

out = BytesIO()
# cairosvg.svg2png(url=url, write_to=out)
cairosvg.svg2png(file_obj=open("DesktopScoreboard/Logo_Files/WSH_alt.svg", "rb"), write_to=out)
print(out)
image_file = Image.open(out)
image = image_file.crop(image_file.getbbox())

# image = Image.open(image_file)

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat-pwm'
options.gpio_slowdown = 2

matrix = RGBMatrix(options=options)

# Make image fit our screen.
image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)

matrix.SetImage(image.convert('RGB'), 5, 5)

try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)
