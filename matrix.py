#!/usr/bin/env python
import time
import sys
import cairosvg

from io import BytesIO

# rgbmatrix = Scoreboard.matrixmodule.rpi-rgb-led-matrix.bindings.python.rgbmatrix
sys.path.append('matrixmodule/rpi-rgb-led-matrix/bindings/python')

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw

# if len(sys.argv) < 2:
#     sys.exit("Require an image argument")
# else:
#     image_file = sys.argv[1]

url1 = 'https://assets.nhle.com/logos/nhl/svg/WSH_light.svg'
url2 = 'https://assets.nhle.com/logos/nhl/svg/ANA_dark.svg'

out1 = BytesIO()
out2 = BytesIO()
# cairosvg.svg2png(url=url, write_to=out)
cairosvg.svg2png(file_obj=open("DesktopScoreboard/Logo_Files/WSH_alt.svg", "rb"), write_to=out1)
image_file1 = Image.open(out1)
image1 = image_file1.crop(image_file1.getbbox())

cairosvg.svg2png(url=url2, write_to=out2)
image_file2 = Image.open(out2)
image2 = image_file2.crop(image_file2.getbbox())

# image = Image.open(image_file)

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat-pwm'
options.gpio_slowdown = 2
options.brightness = 80

matrix = RGBMatrix(options=options)

# Make image fit our screen.
image1.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
image2.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
image1 = image1.resize([int(.85 * s) for s in image1.size])
image2 = image2.resize([int(.8 * s) for s in image2.size])

matrix.SetImage(image1.convert('RGB'), (-matrix.width / 4) + 1, 2)
matrix.SetImage(image2.convert('RGB'), (matrix.width * 2 / 4) - 7, 3)

blackout = Image.new(mode="RGB", size=(22, 32))
blackoutdraw = ImageDraw.Draw(blackout)
blackoutdraw.rectangle([(0, 0), (21, 32)], fill="black")
blackout.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)

matrix.SetImage(blackout.convert('RGB'), 21, 0)


try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)
