
class Train:

    def __init__(self):
        self.time = None
        self.line = None
        self.dest = None
        self.color = None

    def set_line(self, line):
        if line == "OR":
            self.line = "ORANGE"
            self.color = "orange"
        elif line == "SV":
            self.line = "SILVER"
            self.color = "silver"

    def display_train(self):
        if (self.time is not None and self.line is not None and self.dest is not None):
            print("Next Train: " + self.time + " on " + self.line + " to " + self.dest)
