#!/usr/bin/env python3
import time
import sys
import cairosvg

from io import BytesIO

# rgbmatrix = Scoreboard.matrixmodule.rpi-rgb-led-matrix.bindings.python.rgbmatrix
sys.path.append('matrixmodule/rpi-rgb-led-matrix/bindings/python')

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw, ImageFont

# if len(sys.argv) < 2:
#     sys.exit("Require an image argument")
# else:
#     image_file = sys.argv[1]


def run2():
    url1 = 'http://thecraftchop.com/files/images/washington-capitals2.svg'
    url2 = 'https://assets.nhle.com/logos/nhl/svg/ANA_dark.svg'

    out1 = BytesIO()
    out2 = BytesIO()
    # cairosvg.svg2png(url=url, write_to=out)
    cairosvg.svg2png(url=url1, write_to=out1)
    # cairosvg.svg2png(file_obj=open("DesktopScoreboard/Logo_Files/WSH_alt.svg", "rb"), write_to=out1)
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
    options.brightness = 100

    matrix = RGBMatrix(options=options)

    # Make image fit our screen.
    image1.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
    image2.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
    image1 = image1.resize([int(.85 * s) for s in image1.size])
    # image1 = image1.resize([int(1.1 * s) for s in image1.size])
    image2 = image2.resize([int(.8 * s) for s in image2.size])

    matrix.SetImage(image1.convert('RGB'), (-matrix.width / 4) + 1, 2)
    # matrix.SetImage(image1.convert('RGB'), -11, -6)

    matrix.SetImage(image2.convert('RGB'), (matrix.width * 2 / 4) - 7, 3)
    # matrix.SetImage(image2.convert('RGB'), 22, 3)


    blackout = Image.new(mode="RGB", size=(21, 32))
    blackoutdraw = ImageDraw.Draw(blackout)
    blackoutdraw.rectangle([(0, 0), (21, 32)], fill="black")
    blackout.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)

    matrix.SetImage(blackout.convert('RGB'), 21, 0)

    today = Image.new("RGB", size=(matrix.width, matrix.height))

    todaydraw = ImageDraw.Draw(today)
    font = ImageFont.truetype("04B_24__.TTF", 8)
    todaydraw.text((0, 0), "TODAY", font=font, fill="white")
    today = today.crop(today.getbbox())

    matrix.SetImage(today.convert('RGB'), 22, 1)

    timeline = Image.new("RGB", size=(matrix.width, matrix.height))

    timedraw = ImageDraw.Draw(timeline)
    timedraw.text((0, 0), "7:00", font=font, fill="white")
    timeline = timeline.crop(timeline.getbbox())

    matrix.SetImage(timeline.convert('RGB'), 25, 7)

    font2 = ImageFont.truetype("sonic_advance_2.ttf", 16)

    vs = Image.new("RGB", size=(matrix.width, matrix.height))

    vsdraw = ImageDraw.Draw(vs)
    vsdraw.text((0, 0), "VS", font=font2, fill="white")
    vs = vs.crop(vs.getbbox())

    matrix.SetImage(vs.convert('RGB'), 25, 15)
