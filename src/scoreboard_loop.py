import requests
import time
import game
from datetime import date, datetime


def data_loop(games, kill_flag):
    today = date.today()
    # today = datetime(date.today().year, date.today().month, date.today().day - 1)
    todaystring = today.strftime("%Y-%m-%d")

    priority = "Washington Capitals"

    response = None
    dates = None
    games_data = None

    while True:

        if kill_flag():
            print("KILLED")
            break

        try:
            session = requests.Session()
            session.mount('http://',
                          requests.adapters.HTTPAdapter(max_retries=100))
            response = session.get("https://statsapi.web.nhl.com/api/v1/" +
                                   "schedule?date=" +
                                   # "2022-02-08" +
                                   todaystring +
                                   "&expand=schedule.linescore")
        except requests.exceptions.RequestException:
            print("*************DNS ERROR**************")

        if response is not None:
            print("-----------------------------------------------------------------")
            dates = response.json()['dates']
            if dates == []:
                g = game.Game()
                g.no_games = True
                games.append(g)
            else:
                games_data = dates[0]['games']

        if games_data is not None:
            for game_data in games_data:
                if kill_flag():
                    break
                g = None
                if len(games) == 0:
                    g = game.Game()
                    g.id = game_data["gamePk"]
                    games.append(g)

                exists = False
                for x in games:
                    if x.id == game_data["gamePk"]:
                        exists = True
                        g = x
                        break
                if not exists:
                    g = game.Game()
                    g.id = game_data["gamePk"]
                    games.append(g)

                g.set_starttime(game_data['gameDate'])
                g.set_status(game_data['status']['abstractGameState'])

                g.team1 = game_data['teams']['home']['team']['name']
                g.team2 = game_data['teams']['away']['team']['name']
                if g.live:
                    if g.team1 == priority or g.team2 == priority:
                        g.priority = True
                    try:
                        g.period = game_data['linescore']['currentPeriodOrdinal']
                        g.remaining = game_data['linescore']['currentPeriodTimeRemaining']
                        g.intermission = game_data['linescore']['intermissionInfo']['inIntermission']
                    except KeyError:
                        g.period = g.period
                        g.remaining = g.remaining
                        g.intermission = g.intermission

                    g.update_status()
                if g.live or g.final:
                    g.score1 = game_data['teams']['home']['score']
                    g.score2 = game_data['teams']['away']['score']

        if not kill_flag():
            time.sleep(15)
