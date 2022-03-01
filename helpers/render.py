import cairosvg
from io import BytesIO
from PIL import Image, ImageDraw


def draw_text(matrix, text, font, position):
    img = Image.new("RGB", size=(matrix.width, matrix.height))
    img_draw = ImageDraw.Draw(img)
    img_draw.text((0, 0), text, font=font, fill="white")
    img = img.crop(img.getbbox())

    matrix.SetImage(img.convert('RGB'), position[0], position[1])


def draw_recta(matrix, size, color, position):
    rect = Image.new("RGB", size=(size[0], size[1]))
    rect_draw = ImageDraw.Draw(rect)
    rect_draw.rectangle([(0, 0), (size[0], size[1])], fill=color)
    rect.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)

    matrix.SetImage(rect.convert('RGB'), position[0], position[1])


def draw_img(matrix, img, scale, position):
    img.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
    img = img.resize([int(scale * dim) for dim in img.size])

    matrix.SetImage(img.convert('RGB'), position[0], position[1])


def convert(url):
    out = BytesIO()
    cairosvg.svg2png(url=url, write_to=out)
    img = Image.open(out)
    img = img.crop(img.getbbox())
    return img
