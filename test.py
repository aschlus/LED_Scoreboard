import requests
import json
import time
from datetime import date

# Capitals 15


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


live = True

while live:
    live = False
    response = requests.get("https://statsapi.web.nhl.com/api/v1/" +
                            "schedule?date=" +
                            date.today().strftime("%Y-%m-%d") +
                            "&expand=schedule.linescore")

    dates = response.json()['dates'][0]['games']

    for game in dates:

        if game['status']['abstractGameState'] != "Final":
            live = True

        team1 = game['teams']['home']['team']['name']
        team2 = game['teams']['away']['team']['name']
        score1 = game['teams']['home']['score']
        score2 = game['teams']['away']['score']
        period = game['linescore']['currentPeriodOrdinal']
        remaining = game['linescore']['currentPeriodTimeRemaining']

        print('{} {} - {} {} Period: {} Remaining: {}'
              .format(team1, score1, team2, score2, period, remaining))

    time.sleep(int(response.json()['wait']))
