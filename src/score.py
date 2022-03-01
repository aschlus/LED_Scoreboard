#!/usr/bin/env python3
import os

from helpers import render
from PIL import ImageFont


def run2(matrix):

    matrix.Clear()

    url1 = 'http://thecraftchop.com/files/images/washington-capitals2.svg'
    url2 = 'https://assets.nhle.com/logos/nhl/svg/ANA_dark.svg'
    url3 = 'https://assets.nhle.com/logos/nhl/svg/NYR_dark.svg'

    image1 = render.convert(url1)
    image2 = render.convert(url2)

    render.draw_img(matrix, image1, .85, [(-matrix.width / 4) + 1, 2])
    render.draw_img(matrix, image2, .80, [(matrix.width * 2 / 4) - 7, 3])

    render.draw_recta(matrix, [21, 32], "black", [21, 0])

    font = ImageFont.truetype(get_file("assets/fonts/04B_24__.TTF"), 8)
    font2 = ImageFont.truetype(get_file("assets/fonts/sonic_advance_2.ttf"), 16)

    render.draw_text(matrix, "TODAY", font, [22, 1])
    render.draw_text(matrix, "7:00", font, [25, 7])
    render.draw_text(matrix, "VS", font2, [25, 15])


def get_file(path):
    dir = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(dir, path)
