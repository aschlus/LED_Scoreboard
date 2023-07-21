import requests
import time
import mlb_game
from datetime import date, datetime


def data_loop(games, kill_flag):
    today = date.today()
    # today = datetime(date.today().year, date.today().month, date.today().day - 1)
    todaystring = today.strftime("%Y-%m-%d")

    priority = "New York Yankees"

    response = None
    dates = None
    games_data = None
    linescore = None
    linescore_data = None

    while True:

        if kill_flag():
            print("KILLED")
            break

        print("REACHES")
        try:
            print("GAMES OUT")
            session = requests.Session()
            adapter = requests.adapters.HTTPAdapter(max_retries=0)
            adapter.max_retries.respect_retry_after_header = False
            session.mount('http://', adapter)
            response = session.get("https://statsapi.mlb.com/api/v1/" +
                                   "schedule?sportId=1&date=" + todaystring, timeout=2.5)
            #response = session.get("https://statsapi.mlb.com/api/v1/" +
            #                       "schedule?sportId=1&date=2023-02-25", timeout=2.5)
            print("GAMES IN")
        except requests.exceptions.Timeout:
            print("*************TIMEOUT**************")
        except requests.exceptions.RequestException:
            print("*************DNS ERROR**************")

        if response is not None:
            print("-----------------------------------------------------------------")
            try:
                dates = response.json()['dates']
                if dates == []:
                    g = mlb_game.Game()
                    g.no_games = True
                    games.append(g)
                else:
                    games_data = dates[0]['games']
            except KeyError:
                g = mlb_game.Game()
                g.no_games = True
                games.append(g)

        if games_data is not None:
            for game_data in games_data:
                if kill_flag():
                    break
                g = None
                if len(games) == 0:
                    g = mlb_game.Game()
                    g.id = game_data["gamePk"]
                    games.append(g)

                exists = False
                for x in games:
                    if x.id == game_data["gamePk"]:
                        exists = True
                        g = x
                        break
                if not exists:
                    g = mlb_game.Game()
                    g.id = game_data["gamePk"]
                    games.append(g)

                try:
                    print("SCORE OUT")
                    session = requests.Session()
                    session.mount('http://', adapter)
                    linescore = session.get("https://statsapi.mlb.com/api/v1/" +
                                            "game/" + str(g.id) + "/linescore", timeout=2.5)
                    print("SCORE IN")
                except requests.exceptions.Timeout:
                    print("*************TIMEOUT**************")
                except requests.exceptions.RequestException:
                    print("*************DNS ERROR**************")

                if linescore is not None:
                    print("-----------------------------------------------------------------")
                    linescore_data = linescore.json()

                g.set_starttime(game_data['gameDate'])
                g.set_status(game_data['status']['abstractGameState'])

                g.team1 = game_data['teams']['home']['team']['name']
                g.team2 = game_data['teams']['away']['team']['name']
                if g.live:
                    print("IS LIVE")
                    if g.team1 == priority or g.team2 == priority:
                        g.priority = True
                    try:
                        g.inning = linescore_data['currentInning']
                        g.inning_state = linescore_data['inningState']
                        g.outs = linescore_data['outs']
                    except KeyError:
                        print("Inning keyerror")
                        g.inning = g.inning
                        g.inning_state = g.inning_state
                        g.outs = g.outs
                    try:
                        g.first = linescore_data['offense']['first']
                        g.first = True
                    except KeyError:
                        g.first = False
                    try:
                        g.second = linescore_data['offense']['second']
                        g.second = True
                    except KeyError:
                        g.second = False
                    try:
                        g.third = linescore_data['offense']['third']
                        g.third = True
                    except KeyError:
                        g.third = False

                    g.update_status()
                if g.live or g.final:
                    try:
                        g.score1 = game_data['teams']['home']['score']
                        g.score2 = game_data['teams']['away']['score']
                    except KeyError:
                        print("Score keyerror")
                        g.score1 = g.score1
                        g.score2 = g.score2

        if not kill_flag():
            print("SLEEP")
            time.sleep(15)
