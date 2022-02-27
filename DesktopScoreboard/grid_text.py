import numpy as np

BLACK = (0, 0, 0)
GREY = (160, 160, 160)
WHITE = (255, 255, 255)

space = np.asanyarray(([BLACK, BLACK, BLACK],
                       [BLACK, BLACK, BLACK],
                       [BLACK, BLACK, BLACK],
                       [BLACK, BLACK, BLACK],
                       [BLACK, BLACK, BLACK]))

colon = np.asanyarray(([BLACK, BLACK, BLACK],
                       [BLACK, WHITE, BLACK],
                       [BLACK, BLACK, BLACK],
                       [BLACK, WHITE, BLACK],
                       [BLACK, BLACK, BLACK]))

dash = np.asanyarray(([BLACK, BLACK, BLACK],
                      [BLACK, BLACK, BLACK],
                      [WHITE, WHITE, WHITE],
                      [BLACK, BLACK, BLACK],
                      [BLACK, BLACK, BLACK]))

zero = np.asanyarray(([WHITE, WHITE, WHITE],
                      [WHITE, BLACK, WHITE],
                      [WHITE, BLACK, WHITE],
                      [WHITE, BLACK, WHITE],
                      [WHITE, WHITE, WHITE]))

one = np.asanyarray(([BLACK, WHITE, BLACK],
                     [WHITE, WHITE, BLACK],
                     [BLACK, WHITE, BLACK],
                     [BLACK, WHITE, BLACK],
                     [WHITE, WHITE, WHITE]))

two = np.asanyarray(([WHITE, WHITE, WHITE],
                     [BLACK, BLACK, WHITE],
                     [WHITE, WHITE, WHITE],
                     [WHITE, BLACK, BLACK],
                     [WHITE, WHITE, WHITE]))

three = np.asanyarray(([WHITE, WHITE, WHITE],
                       [BLACK, BLACK, WHITE],
                       [WHITE, WHITE, WHITE],
                       [BLACK, BLACK, WHITE],
                       [WHITE, WHITE, WHITE]))

four = np.asanyarray(([WHITE, BLACK, WHITE],
                      [WHITE, BLACK, WHITE],
                      [WHITE, WHITE, WHITE],
                      [BLACK, BLACK, WHITE],
                      [BLACK, BLACK, WHITE]))

five = np.asanyarray(([WHITE, WHITE, WHITE],
                      [WHITE, BLACK, BLACK],
                      [WHITE, WHITE, WHITE],
                      [BLACK, BLACK, WHITE],
                      [WHITE, WHITE, WHITE]))

six = np.asanyarray(([WHITE, WHITE, WHITE],
                     [WHITE, BLACK, BLACK],
                     [WHITE, WHITE, WHITE],
                     [WHITE, BLACK, WHITE],
                     [WHITE, WHITE, WHITE]))

seven = np.asanyarray(([WHITE, WHITE, WHITE],
                       [WHITE, BLACK, WHITE],
                       [BLACK, BLACK, WHITE],
                       [BLACK, BLACK, WHITE],
                       [BLACK, BLACK, WHITE]))

eight = np.asanyarray(([WHITE, WHITE, WHITE],
                       [WHITE, BLACK, WHITE],
                       [WHITE, WHITE, WHITE],
                       [WHITE, BLACK, WHITE],
                       [WHITE, WHITE, WHITE]))

nine = np.asanyarray(([WHITE, WHITE, WHITE],
                      [WHITE, BLACK, WHITE],
                      [WHITE, WHITE, WHITE],
                      [BLACK, BLACK, WHITE],
                      [BLACK, BLACK, WHITE]))

letter_e = np.asanyarray(([WHITE, WHITE, WHITE],
                          [WHITE, BLACK, BLACK],
                          [WHITE, WHITE, WHITE],
                          [WHITE, BLACK, BLACK],
                          [WHITE, WHITE, WHITE]))

letter_n = np.asanyarray(([WHITE, WHITE, WHITE],
                          [WHITE, BLACK, WHITE],
                          [WHITE, BLACK, WHITE],
                          [WHITE, BLACK, WHITE],
                          [WHITE, BLACK, WHITE]))

letter_d = np.asanyarray(([WHITE, WHITE, BLACK],
                          [WHITE, BLACK, WHITE],
                          [WHITE, BLACK, WHITE],
                          [WHITE, BLACK, WHITE],
                          [WHITE, WHITE, BLACK]))

letter_w = np.asanyarray(([WHITE, BLACK, WHITE],
                          [WHITE, BLACK, WHITE],
                          [WHITE, BLACK, WHITE],
                          [WHITE, WHITE, WHITE],
                          [WHITE, BLACK, WHITE]))

letter_s = np.asanyarray(([WHITE, WHITE, WHITE],
                          [WHITE, BLACK, BLACK],
                          [WHITE, WHITE, WHITE],
                          [BLACK, BLACK, WHITE],
                          [WHITE, WHITE, WHITE]))

letter_h = np.asanyarray(([WHITE, BLACK, WHITE],
                          [WHITE, BLACK, WHITE],
                          [WHITE, WHITE, WHITE],
                          [WHITE, BLACK, WHITE],
                          [WHITE, BLACK, WHITE]))

letter_t = np.asanyarray(([WHITE, WHITE, WHITE],
                          [BLACK, WHITE, BLACK],
                          [BLACK, WHITE, BLACK],
                          [BLACK, WHITE, BLACK],
                          [BLACK, WHITE, BLACK]))

letter_r = np.asanyarray(([WHITE, WHITE, WHITE],
                          [WHITE, BLACK, WHITE],
                          [WHITE, BLACK, WHITE],
                          [WHITE, WHITE, BLACK],
                          [WHITE, BLACK, WHITE]))
letter_a = np.asanyarray(([WHITE, WHITE, WHITE],
                          [WHITE, BLACK, WHITE],
                          [WHITE, WHITE, WHITE],
                          [WHITE, BLACK, WHITE],
                          [WHITE, BLACK, WHITE]))

letter_l = np.asanyarray(([WHITE, BLACK, BLACK],
                          [WHITE, BLACK, BLACK],
                          [WHITE, BLACK, BLACK],
                          [WHITE, BLACK, BLACK],
                          [WHITE, WHITE, WHITE]))

letter_m = np.asanyarray(([WHITE, BLACK, WHITE],
                          [WHITE, WHITE, WHITE],
                          [WHITE, BLACK, WHITE],
                          [WHITE, BLACK, WHITE],
                          [WHITE, BLACK, WHITE]))

letter_o = np.asanyarray(([WHITE, WHITE, WHITE],
                          [WHITE, BLACK, WHITE],
                          [WHITE, BLACK, WHITE],
                          [WHITE, BLACK, WHITE],
                          [WHITE, WHITE, WHITE]))

letter_c = np.asanyarray(([WHITE, WHITE, WHITE],
                          [WHITE, BLACK, BLACK],
                          [WHITE, BLACK, BLACK],
                          [WHITE, BLACK, BLACK],
                          [WHITE, WHITE, WHITE]))

letter_k = np.asanyarray(([WHITE, BLACK, WHITE],
                          [WHITE, BLACK, WHITE],
                          [WHITE, WHITE, BLACK],
                          [WHITE, BLACK, WHITE],
                          [WHITE, BLACK, WHITE]))

letter_i = np.asanyarray(([WHITE, WHITE, WHITE],
                          [BLACK, WHITE, BLACK],
                          [BLACK, WHITE, BLACK],
                          [BLACK, WHITE, BLACK],
                          [WHITE, WHITE, WHITE]))

letter_p = np.asanyarray(([WHITE, WHITE, WHITE],
                          [WHITE, BLACK, WHITE],
                          [WHITE, WHITE, WHITE],
                          [WHITE, BLACK, BLACK],
                          [WHITE, BLACK, BLACK]))

letter_g = np.asanyarray(([WHITE, WHITE, WHITE],
                          [WHITE, BLACK, BLACK],
                          [WHITE, BLACK, WHITE],
                          [WHITE, BLACK, WHITE],
                          [WHITE, WHITE, WHITE]))


numDict = {
    " ": space,
    ":": colon,
    "-": dash,
    "0": zero,
    "1": one,
    "2": two,
    "3": three,
    "4": four,
    "5": five,
    "6": six,
    "7": seven,
    "8": eight,
    "9": nine,
    "E": letter_e,
    "N": letter_n,
    "n": letter_n,
    "D": letter_d,
    "d": letter_d,
    "W": letter_w,
    "S": letter_s,
    "s": letter_s,
    "H": letter_h,
    "T": letter_t,
    "t": letter_t,
    "R": letter_r,
    "r": letter_r,
    "A": letter_a,
    "L": letter_l,
    "M": letter_m,
    "O": letter_o,
    "C": letter_c,
    "K": letter_k,
    "I": letter_i,
    "P": letter_p,
    "G": letter_g
}

teamDict = {
    "Edmonton Oilers": "EDM",
    "Dallas Stars": "DAL",
    "Colorado Avalanche": "COL",
    "Los Angeles Kings": "LAK",
    "Washington Capitals": "WSH",
    "Nashville Predators": "NSH",
    "Anaheim Ducks": "ANA",
    "Carolina Hurricanes": "CAR",
    "Detroit Red Wings": "DET",
    "Montreal Canadiens": "MTL",
    "Ottawa Senators": "OTT",
    "Seattle Kraken": "SEA",
    "St. Louis Blues": "STL",
    "Toronto Maple Leafs": "TOR",
    "Winnipeg Jets": "WPG",
    "Minnesota Wild": "MIN"
}
