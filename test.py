import requests
import json
import time
import math
from datetime import date, datetime, timezone

# Capitals 15


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


live = True
pregame = False
firsttime = None
dayover = False

today = date.today()
todaystring = today.strftime("%Y-%m-%d")

while live:
    live = False
    response = requests.get("https://statsapi.web.nhl.com/api/v1/" +
                            "schedule?date=" +
                            # "2022-02-08" +
                            todaystring +
                            "&expand=schedule.linescore")

    dates = response.json()['dates']

    if dates[0]['games'][0]['status']['abstractGameState'] == "Preview":
        pregame = True

    if len(dates) == 0:
        print("No games today")
    else:
        games = dates[0]['games']

        for game in games:

            status = game['status']['abstractGameState']

            team1 = game['teams']['home']['team']['name']
            team2 = game['teams']['away']['team']['name']

            if status == "Live":
                live = True

                score1 = game['teams']['home']['score']
                score2 = game['teams']['away']['score']
                period = game['linescore']['currentPeriodOrdinal']
                remaining = game['linescore']['currentPeriodTimeRemaining']
                intermission = game['linescore']['intermissionInfo']['inIntermission']

                if not intermission:
                    print('{} {} - {} {} Period: {} Remaining: {}'
                          .format(team1, score1, team2, score2, period, remaining))
                else:
                    print('{} {} - {} {} {} Intermission'
                          .format(team1, score1, team2, score2, period))

            elif status == "Final":
                score1 = game['teams']['home']['score']
                score2 = game['teams']['away']['score']

                print('{} {} - {} {} Final'
                      .format(team1, score1, team2, score2))

                if not dayover:
                    dayover = True

            elif status == "Preview":
                utc = datetime.fromisoformat(game['gameDate']
                                             .replace("Z", "+00:00"))
                local = utc.replace(tzinfo=timezone.utc).astimezone(tz=None)
                starttime = local.strftime("%I:%M %p").lstrip('0')

                if firsttime is None:
                    firsttime = local
                    firsttime = firsttime.replace(tzinfo=None)

                print('{} - {} Start Time: {}'.format(team1, team2, starttime))

        if live:
            print("")
            time.sleep(int(response.json()['wait']))
        elif pregame:
            print("")
            delay = math.ceil((firsttime-datetime.today()).total_seconds())

            if delay >= 0:
                time.sleep(delay)
            else:
                time.sleep(int(response.json()['wait']))

            pregame = False
            firsttime = None
            live = True

        elif dayover:
            print("")
            tomorrow = datetime(today.year, today.month, today.day + 1)
            delay = math.ceil((tomorrow-datetime.today()).total_seconds())

            if delay >= 0:
                time.sleep(delay)

            today = tomorrow
            todaystring = tomorrow.strftime("%Y-%m-%d")

            dayover = False
            live = True
