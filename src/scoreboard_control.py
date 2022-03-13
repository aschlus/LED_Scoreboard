#!/usr/bin/env python3
import os
import json
import time
import threading
import scoreboard_loop

from helpers import render
from PIL import ImageFont

teamDict = {
    "New Jersey Devils": 0,
    "New York Islanders": 1,
    "New York Rangers": 2,
    "Philadelphia Flyers": 3,
    "Pittsburgh Penguins": 4,
    "Boston Bruins": 5,
    "Buffalo Sabres": 6,
    "Montréal Canadiens": 7,
    "Ottawa Senators": 8,
    "Toronto Maple Leafs": 9,
    "Carolina Hurricanes": 10,
    "Florida Panthers": 11,
    "Tampa Bay Lightning": 12,
    "Washington Capitals": 13,
    "Chicago Blackhawks": 14,
    "Detroit Red Wings": 15,
    "Nashville Predators": 16,
    "St. Louis Blues": 17,
    "Calgary Flames": 18,
    "Colorado Avalanche": 19,
    "Edmonton Oilers": 20,
    "Vancouver Canucks": 21,
    "Anaheim Ducks": 22,
    "Dallas Stars": 23,
    "Los Angeles Kings": 24,
    "San Jose Sharks": 25,
    "Columbus Blue Jackets": 26,
    "Minnesota Wild": 27,
    "Winnipeg Jets": 28,
    "Arizona Coyotes": 29,
    "Vegas Golden Knights": 30,
    "Seattle Kraken": 31,
}


def run2(matrix, board):

    canvas = matrix.CreateFrameCanvas()

    font = ImageFont.truetype(get_file("assets/fonts/Test_Font.ttf"), 8)
    font2 = ImageFont.truetype(get_file("assets/fonts/sonic_advance_2.ttf"), 16)

    data = json.load(open(get_file("config/scoreboard_config.json")))

    games = []
    loop = threading.Thread(target=scoreboard_loop.data_loop, args=[games])
    loop.setDaemon(True)
    loop.start()

    while True:
        g = None
        for game in games:
            while game.team1 is None or game.team2 is None:
                time.sleep(1)
            runonce = True
            while (game.priority and not game.intermission) or runonce:
                game.display_teams()
                image1 = render.convert(get_file("assets/logos/" +
                                        data['teams'][teamDict[game.team1]]
                                        ['abbreviation'] +
                                        ".svg"))
                image2 = render.convert(get_file("assets/logos/" +
                                        data['teams'][teamDict[game.team2]]
                                        ['abbreviation'] +
                                        ".svg"))

                render.draw_img(canvas, image1, data['teams'][teamDict[game.team1]]['position']['scale'],
                                data['teams'][teamDict[game.team1]]['position']['home'])
                render.draw_img(canvas, image2, data['teams'][teamDict[game.team2]]['position']['scale'],
                                data['teams'][teamDict[game.team2]]['position']['away'])

                render.draw_rect(canvas, [21, 32], "black", [21, 0])

                if not game.final:
                    render.draw_text(canvas, game.status, font, "center_status")
                if game.live:
                    if not game.intermission:
                        render.draw_text(canvas, game.remaining, font, "center_time")
                    else:
                        render.draw_text(canvas, "INT", font, "center_time")
                    render.draw_text(canvas,
                                     str(game.score1) + "-" + str(game.score2),
                                     font2, "center_score")
                elif game.final:
                    render.draw_text(canvas, "FINAL", font, "center_time")
                    render.draw_text(canvas,
                                     str(game.score1) + "-" + str(game.score2),
                                     font2, "center_score")
                else:
                    render.draw_text(canvas, game.starttime, font, "center_time")
                    render.draw_text(canvas, "VS", font2, "center_score")

                canvas = matrix.SwapOnVSync(canvas)
                canvas.Clear()
                runonce = False
                if game.priority and not game.intermission:
                    time.sleep(5)

            time.sleep(2)


def get_file(path):
    dir = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(dir, path)
