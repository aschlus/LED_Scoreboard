#!/usr/bin/env python3
import os
import json
import time
import threading
import scoreboard_loop
from datetime import datetime
import datetime as dt

from helpers import render
from PIL import ImageFont

module = "NHL Scoreboard"

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

    stop_time = None

    while True:

        print("Wake time: " + str(datetime.today()))
        stop_time = (datetime.today() + dt.timedelta(days=1)).replace(hour=1, minute=00, second=0, microsecond=0)
        print("Stop time: " + str(stop_time))

        games = []
        kill_flag = False

        loop = threading.Thread(target=scoreboard_loop.data_loop, args=[games, (lambda : kill_flag)])
        loop.setDaemon(True)
        loop.start()

        while True:
            all_final = True
            for game in games:
                if game.no_games:
                    render.draw_text(canvas, "NO GAMES TODAY", font, "white", "center_time")
                    canvas = render.push_to_board(matrix, canvas, board, module)
                    canvas.Clear()
                    if (datetime.today() - stop_time).total_seconds() >= 0:
                        kill_flag = True
                        break
                    time.sleep(60)
                    break

                while game.team1 is None or game.team2 is None:
                    time.sleep(1)
                runonce = True
                while (game.priority and not game.intermission) or runonce:
                    game.display_teams()
                    image1 = render.convert(get_file("assets/logos/NHL/" +
                                            data['teams'][teamDict[game.team1]]
                                            ['abbreviation'] +
                                            ".svg"))
                    image2 = render.convert(get_file("assets/logos/NHL/" +
                                            data['teams'][teamDict[game.team2]]
                                            ['abbreviation'] +
                                            ".svg"))

                    render.draw_img(canvas, image1, data['teams'][teamDict[game.team1]]['position']['scale'],
                                    data['teams'][teamDict[game.team1]]['position']['home'])
                    render.draw_img(canvas, image2, data['teams'][teamDict[game.team2]]['position']['scale'],
                                    data['teams'][teamDict[game.team2]]['position']['away'])

                    render.draw_rect(canvas, [21, 32], "black", [21, 0])

                    if not game.final:
                        render.draw_text(canvas, game.status, font, "white", "center_status")
                        all_final = False
                    if game.live:
                        if not game.intermission:
                            render.draw_text(canvas, game.remaining, font, "white", "center_time")
                        else:
                            render.draw_text(canvas, "INT", font, "white", "center_time")
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

                    canvas = render.push_to_board(matrix, canvas, board, module)
                    canvas.Clear()
                    runonce = False
                    if game.priority and not game.intermission:
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
