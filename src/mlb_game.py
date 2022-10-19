from datetime import datetime, timezone


class Game:

    def __init__(self):
        self.id = None
        self.team1 = None
        self.team2 = None
        self.starttime = None
        self.status = None
        self.inning = None
        self.inning_state = None
        self.outs = None
        self.live = None
        self.score1 = None
        self.score2 = None
        self.final = None
        self.priority = False
        self.no_games = False
        self.first = False
        self.second = False
        self.third = False

    def set_starttime(self, date):
        utc = datetime.fromisoformat(date.replace("Z", "+00:00"))
        local = utc.replace(tzinfo=timezone.utc).astimezone(tz=None)
        starttime = local.strftime("%I:%M").lstrip('0')
        self.starttime = starttime

    def set_status(self, status):
        if status == "Preview":
            self.status = "TODAY"
        elif status == "Live":
            self.live = True
            self.status = "LIVE"
        elif status == "Final":
            self.live = False
            self.final = True
            self.priority = False
            self.status = "FINAL"
        else:
            self.status = status

    def update_status(self):
        half = None
        if self.inning_state == "Top":
            half = "T"
        elif self.inning_state == "Bottom":
            half = "B"
        elif self.inning_state == "Start":
            half = "S"
            self.outs = 0
        elif self.inning_state == "Middle":
            half = "M"
            self.outs = 0
        elif self.inning_state == "End":
            half = "E"
        else:
            half = " "
        self.status = half + " " + str(self.inning)

    def display_teams(self):
        print(self.team1 + " vs " + self.team2)
