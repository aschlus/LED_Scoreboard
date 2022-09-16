import cairosvg
import math
from io import BytesIO
from PIL import Image, ImageDraw


def draw_text(canvas, text, font, color, position):
    img = Image.new("RGB", size=(canvas.width, canvas.height))
    img_draw = ImageDraw.Draw(img)
    img_draw.text((0, 0), text, font=font, fill=color)
    img = img.crop(img.getbbox())

    coords = []

    if position == "center_status":
        coords.append(math.floor((canvas.width - img.width) / 2))
        coords.append(1)
    elif position == "center_time":
        mod = 0
        if text == "1ST" or text == "2ND" or text == "3RD":
            mod = 1
        coords.append(math.floor((canvas.width - img.width) / 2) + mod)
        coords.append(7)
    elif position == "center_score":
        coords.append(math.floor((canvas.width - img.width) / 2))
        coords.append(15)
    elif position == "loading":
        coords.append(1)
        coords.append(10)

    canvas.SetImage(img.convert('RGB'), coords[0], coords[1])


def draw_rect(canvas, size, color, position):
    rect = Image.new("RGB", size=(size[0], size[1]))
    rect_draw = ImageDraw.Draw(rect)
    rect_draw.rectangle([(0, 0), (size[0], size[1])], fill=color)
    rect.thumbnail((canvas.width, canvas.height), Image.ANTIALIAS)

    canvas.SetImage(rect.convert('RGB'), position[0], position[1])


def draw_img(canvas, img, scale, position):
    img.thumbnail((canvas.width, canvas.height), Image.ANTIALIAS)
    img = img.resize([int(scale * dim) for dim in img.size])

    canvas.SetImage(img.convert('RGB'), position[0], position[1])


def convert(file):
    out = BytesIO()
    cairosvg.svg2png(file_obj=open(file, "rb"), write_to=out)
    img = Image.open(out)
    img = img.crop(img.getbbox())
    return img
