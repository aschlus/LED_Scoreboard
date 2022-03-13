from datetime import datetime, timezone


class Game:

    def __init__(self):
        self.id = None
        self.team1 = None
        self.team2 = None
        self.starttime = None
        self.status = None
        self.period = None
        self.live = None
        self.remaining = None
        self.score1 = None
        self.score2 = None
        self.intermission = None
        self.final = None
        self.priority = False

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
        if self.period == "1st":
            self.status = "1ST"
        elif self.period == "2nd":
            self.status = "2ND"
        elif self.period == "3rd":
            self.status = "3RD"
        elif self.period == "OT" or self.period == "SO":
            self.status = self.period

    def display_teams(self):
        print(self.team1 + " vs " + self.team2)
