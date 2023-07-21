#!/usr/bin/env python
import time
import sys
import cairosvg

from io import BytesIO

# rgbmatrix = Scoreboard.matrixmodule.rpi-rgb-led-matrix.bindings.python.rgbmatrix
sys.path.append('matrixmodule/rpi-rgb-led-matrix/bindings/python')

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw, ImageFont

url1 = 'http://thecraftchop.com/files/images/washington-capitals2.svg'

out1 = BytesIO()
# cairosvg.svg2png(url=url, write_to=out)
cairosvg.svg2png(url=url1, write_to=out1)
# cairosvg.svg2png(file_obj=open("DesktopScoreboard/Logo_Files/WSH_alt.svg", "rb"), write_to=out1)
image_file1 = Image.open(out1)
img = image_file1.crop(image_file1.getbbox())

h = img.height
w = img.width

# Get image
img = img.resize((w,h), Image.ANTIALIAS)
# Set to array
img_arr = np.asarray(img)
# Get the shape so we know x,y coords
h,w,c = img_arr.shape

# Then draw our mona lisa
mona_lisa = ''
for x in range(h):
    for y in range(w):
        pix = img_arr[x][y]
        color = ' '
        # 90% of our image is black, and the pi sometimes has trouble writing to the terminal
        # quickly. So default the color to blank, and only fill in the color if it's not black
        if sum(pix) > 0:
            color = get_color(pix[0], pix[1], pix[2])
        mona_lisa += color
sys.stdout.write(mona_lisa)
sys.stdout.flush()
