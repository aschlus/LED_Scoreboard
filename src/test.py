import requests
import time
import math
import sys
from datetime import date, datetime, timezone

# Capitals 15

live = True
pregame = False
firsttime = None
dayover = False
timeleft = None

team1score = None
team2score = None

team1name = None
team2name = None

curperiod = None
intermissiontime = None

killThreads = False


def schedule():
    global live
    global pregame
    global firsttime
    global dayover
    global timeleft
    global team1score
    global team2score
    global team1name
    global team2name
    global curperiod
    global intermissiontime

    today = date.today()
    # today = datetime(date.today().year, date.today().month, date.today().day - 1)
    todaystring = today.strftime("%Y-%m-%d")

    while live and not killThreads:
        live = False
        timeflag = None
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

                    if period == "SO":
                        print('{} {} - {} {} Period: {}'
                              .format(team1, score1, team2, score2, period))
                    elif not intermission:
                        print('{} {} - {} {} Period: {} Remaining: {}'
                              .format(team1, score1, team2, score2, period, remaining))
                    else:
                        print('{} {} - {} {} {} Intermission'
                              .format(team1, score1, team2, score2, period))

                    if timeflag is None:
                        timeflag = True
                        timeleft = remaining
                        team1score = score1
                        team2score = score2
                        team1name = team1
                        team2name = team2
                        curperiod = period
                        intermissiontime = intermission

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

                    if timeflag is None:
                        timeflag = True
                        timeleft = starttime
                        team1name = team1
                        team2name = team2

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
            else:
                print("else")


if __name__ == "__main__":
    try:
        schedule()
    except KeyboardInterrupt:
        print("Quit Received")
        sys.exit(0)
