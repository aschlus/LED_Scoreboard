#!/usr/bin/env python3
import os
import json
import time
import threading
import mlb_scoreboard_loop
from datetime import datetime
import datetime as dt

from helpers import render
from PIL import ImageFont

teamDict = {
    "Arizona Diamondbacks": 0,
    "Atlanta Braves": 1,
    "Baltimore Orioles": 2,
    "Boston Red Sox": 3,
    "Chicago Cubs": 4,
    "Cincinnati Reds": 5,
    "Cleveland Guardians": 6,
    "Colorado Rockies": 7,
    "Chicago White Sox": 8,
    "Detroit Tigers": 9,
    "Houston Astros": 10,
    "Kansas City Royals": 11,
    "Los Angeles Angels": 12,
    "Los Angeles Dodgers": 13,
    "Miami Marlins": 14,
    "Milwaukee Brewers": 15,
    "Minnesota Twins": 16,
    "New York Mets": 17,
    "New York Yankees": 18,
    "Oakland Athletics": 19,
    "Philadelphia Phillies": 20,
    "Pittsburgh Pirates": 21,
    "San Diego Padres": 22,
    "Seattle Mariners": 23,
    "San Francisco Giants": 24,
    "St. Louis Cardinals": 25,
    "Tampa Bay Rays": 26,
    "Texas Rangers": 27,
    "Toronto Blue Jays": 28,
    "Washington Nationals": 29,
}


def run2(matrix, board):

    canvas = matrix.CreateFrameCanvas()

    font = ImageFont.truetype(get_file("assets/fonts/Test_Font.ttf"), 8)
    font2 = ImageFont.truetype(get_file("assets/fonts/sonic_advance_2.ttf"), 16)

    data = json.load(open(get_file("config/mlb_config.json")))

    stop_time = None

    while True:

        print("Wake time: " + str(datetime.today()))
        stop_time = (datetime.today() + dt.timedelta(days=1)).replace(hour=1, minute=00, second=0, microsecond=0)
        print("Stop time: " + str(stop_time))

        games = []
        kill_flag = False

        loop = threading.Thread(target=mlb_scoreboard_loop.data_loop, args=[games, (lambda : kill_flag)])
        loop.setDaemon(True)
        loop.start()

        while True:
            all_final = True
            for game in games:
                if game.no_games:
                    render.draw_text(canvas, "NO GAMES TODAY", font, "white", "center_time")
                    canvas = matrix.SwapOnVSync(canvas)
                    canvas.Clear()
                    if (datetime.today() - stop_time).total_seconds() >= 0:
                        kill_flag = True
                        break
                    time.sleep(60)
                    break

                while game.team1 is None or game.team2 is None:
                    time.sleep(1)
                runonce = True
                while (game.priority) or runonce:
                    game.display_teams()
                    image1 = render.convert(get_file("assets/logos/MLB/" +
                                            data['teams'][teamDict[game.team1]]
                                            ['abbreviation'] +
                                            ".svg"))
                    image2 = render.convert(get_file("assets/logos/MLB/" +
                                            data['teams'][teamDict[game.team2]]
                                            ['abbreviation'] +
                                            ".svg"))

                    if game.live:
                        render.draw_rect(canvas, [16, 16], "gray", [0, 0])
                        render.draw_rect(canvas, [14, 14], "black", [1, 1])
                        render.draw_rect(canvas, [16, 16], "gray", [0, 16])
                        render.draw_rect(canvas, [14, 14], "black", [1, 17])
                        render.draw_img(canvas, image1, 0.45, [1, 1])
                        render.draw_img(canvas, image2, 0.45, [1, 17])

                    else:
                        render.draw_img(canvas, image1, data['teams'][teamDict[game.team1]]['position']['scale'],
                                        data['teams'][teamDict[game.team1]]['position']['home'])
                        render.draw_img(canvas, image2, data['teams'][teamDict[game.team2]]['position']['scale'],
                                        data['teams'][teamDict[game.team2]]['position']['away'])

                    render.draw_rect(canvas, [21, 32], "black", [21, 0])

                    if not game.final:
                        render.draw_text(canvas, game.status, font, "white", "center_status")
                        all_final = False
                    if game.live:
                        render.draw_text(canvas, str(game.outs) + " OUTS", font, "white", "center_time")
                        render.draw_text(canvas,
                                         str(game.score1) + "-" + str(game.score2),
                                         font2, "white", "center_score")
                    elif game.final:
                        render.draw_text(canvas, "FINAL", font, "white", "center_time")
                        render.draw_text(canvas,
                                         str(game.score1) + "-" + str(game.score2),
                                         font2, "white", "center_score")
                    else:
                        render.draw_text(canvas, game.starttime, font, "white", "center_time")
                        render.draw_text(canvas, "VS", font2, "white", "center_score")

                    canvas = matrix.SwapOnVSync(canvas)
                    canvas.Clear()
                    runonce = False
                    if game.priority:
                        time.sleep(5)

                    if (datetime.today() - stop_time).total_seconds() >= 0: # and all_final:
                        kill_flag = True
                        break

                if kill_flag:
                    break

                time.sleep(2)

            if kill_flag:
                print("KILLING")
                games = []
                matrix.Clear()
                time.sleep(15)
                print("READY TO RESET")
                break

        print("WAITING")
        now = datetime.today()
        later = stop_time.replace(hour=8)
        print("Wake time: " + str(later))
        # later = datetime(2022, 4, 28, 16, 49, 00)
        diff = (later - now).total_seconds()
        time.sleep(diff)
        print("RESTART")


def get_file(path):
    dir = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(dir, path)
