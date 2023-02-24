import cairosvg
import math
from io import BytesIO
from PIL import Image, ImageDraw


def push_to_board(matrix, canvas, board, module):
    if module == "NHL Scoreboard":
        board.nhl_cache = canvas
    elif module == "MLB Scoreboard":
        board.mlb_cache = canvas
    elif module == "Metro":
        board.metro_cache = canvas

    if canvas is None:
        if module == "NHL Scoreboard" and board.nhl_cache is not None:
            matrix.SwapOnVSync(board.nhl_cache)
        elif module == "MLB Scoreboard" and board.mlb_cache is not None:
            matrix.SwapOnVSync(board.mlb_cache)
        elif module == "Metro" and board.metro_cache is not None:
            matrix.SwapOnVSync(board.metro_cache)
        return
    elif board.name == module:
        canvas = matrix.SwapOnVSync(canvas)
    canvas.Clear()
    return canvas


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
    elif position == "mlb_score1":
        coords.append(math.floor((13 - img.width) / 2) + 16)
        coords.append(2)
    elif position == "mlb_score2":
        coords.append(math.floor((13 - img.width) / 2) + 16)
        coords.append(18)
    elif position == "mlb_inning":
        coords.append(canvas.width - 21)
        coords.append(1)

    canvas.SetImage(img.convert('RGB'), coords[0], coords[1])


def draw_rect(canvas, size, color, position):
    rect = Image.new("RGB", size=(size[0], size[1]))
    rect_draw = ImageDraw.Draw(rect)
    rect_draw.rectangle([(0, 0), (size[0], size[1])], fill=color)
    rect.thumbnail((canvas.width, canvas.height), Image.ANTIALIAS)

    canvas.SetImage(rect.convert('RGB'), position[0], position[1])

#20 -- 20 -- 20

def draw_img(canvas, img, scale, position):
    img.thumbnail((canvas.width, canvas.height))
    img = img.resize([int(scale * dim) for dim in img.size])

    coords = []

    if position == "mlb_team1":
        coords.append(math.floor((14 - img.width) / 2) + 1)
        coords.append(math.floor((14 - img.height) / 2) + 1)
        position = coords
    elif position == "mlb_team2":
        coords.append(math.floor((14 - img.width) / 2) + 1)
        coords.append(math.floor((14 - img.width) / 2) + 17)
        position = coords
    elif position == "mlb_out1":
        coords.append(canvas.width - 9)
        coords.append(2)
        position = coords
    elif position == "mlb_out2":
        coords.append(canvas.width - 9)
        coords.append((canvas.height / 2) - 4)
        position = coords
    elif position == "mlb_out3":
        coords.append(canvas.width - 9)
        coords.append(22)
        position = coords
    elif position == "mlb_bases":
        coords.append(canvas.width - 33)
        coords.append(12)
        position = coords
    elif position == "mlb_inning":
        coords.append(canvas.width - 29)
        coords.append(2)
        position = coords

    canvas.SetImage(img.convert('RGB'), position[0], position[1])


def convert(file):
    out = BytesIO()
    cairosvg.svg2png(file_obj=open(file, "rb"), write_to=out)
    img = Image.open(out)
    img = img.crop(img.getbbox())
    img = img.convert('RGB')
    return img


def png(file):
    file = Image.open(file)
    out = BytesIO()
    file.save(out, 'PNG')
    img = Image.open(out)
    img = img.crop(img.getbbox())
    return img
