import cairosvg
from io import BytesIO
from PIL import Image, ImageDraw


def draw_text(canvas, text, font, position):
    img = Image.new("RGB", size=(canvas.width, canvas.height))
    img_draw = ImageDraw.Draw(img)
    img_draw.text((0, 0), text, font=font, fill="white")
    img = img.crop(img.getbbox())

    canvas.SetImage(img.convert('RGB'), position[0], position[1])


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


def convert(url):
    out = BytesIO()
    cairosvg.svg2png(url=url, write_to=out)
    img = Image.open(out)
    img = img.crop(img.getbbox())
    return img
