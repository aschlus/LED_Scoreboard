import sys
import pygame
from pygame.locals import KEYDOWN, K_q
import numpy as np
import time
import grid_text
import team_logo
from threading import Thread
sys.path.insert(0, '.')
import test

PIXEL = 20
BORDER = PIXEL * 2
SCREENSIZE = WIDTH, HEIGHT = PIXEL * 64 + BORDER, PIXEL * 32 + BORDER
BLACK = (0, 0, 0)
GREY = (160, 160, 160)
WHITE = (255, 255, 255)

_VARS = {'surf': False, 'gridOrigin': (PIXEL, PIXEL)}

MAP = np.zeros((32, 64))

cellMap = np.zeros((32, 64), dtype=type(BLACK))

curtime = "20:00"

killThreads = False


def main():
    global killThreads
    global curtime

    guiThread = Thread(target=update)
    scheduleThread = Thread(target=test.schedule)
    guiThread.start()
    scheduleThread.start()


def update():
    pygame.init()
    pygame.display.set_caption('Scoreboard')
    _VARS['surf'] = pygame.display.set_mode(SCREENSIZE)
    _VARS['surf'].fill(GREY)

    while not killThreads:
        checkEvents()
        clear()
        if(test.timeleft is not None):
            drawLogo(team_logo.WPG, 0, -13)
            drawLogo(team_logo.ANA, 0, 45)
            pygame.draw.rect(_VARS['surf'], GREY, pygame.Rect(0, 0, WIDTH, HEIGHT), PIXEL)
            if not test.intermissiontime:
                if not test.pregame:
                    drawNum(split(test.curperiod), 14, ((64-4*len(split(test.curperiod)))/2))
                drawNum(split(test.timeleft), 20, ((64-4*len(split(test.timeleft)))/2))
            else:
                drawNum(split(test.curperiod), 14, ((64-4*len(split(test.curperiod)))/2))
                drawNum(split("INT"), 20, (((64-4*3)/2)))
            #drawNum(split(grid_text.teamDict[test.team1name]), 3, (64/4) - 7)
            #drawNum(split(grid_text.teamDict[test.team2name]), 3, (64/4 * 3) - 4)
            if not test.pregame:
                drawNum(split(str(test.team1score)), 5, (64/2) - 7)
                drawNum("-", 5, (64/2) - 2)
                drawNum(split(str(test.team2score)), 5, (64/2) + 3)
        drawGrid()
        pygame.display.update()
    pygame.quit()


def clear():
    pygame.draw.rect(_VARS['surf'], BLACK, pygame.Rect(PIXEL, PIXEL, WIDTH - BORDER, HEIGHT - BORDER))


def drawGrid():
    for y in range(0, 65):
        pygame.draw.line(_VARS['surf'], BLACK, (PIXEL + y * PIXEL, PIXEL), (PIXEL + y * PIXEL, HEIGHT - PIXEL), 2)
    for x in range(0, 33):
        pygame.draw.line(_VARS['surf'], BLACK, (PIXEL, PIXEL + x * PIXEL), (WIDTH - PIXEL, PIXEL + x * PIXEL), 2)


def drawCell(x, y, color):
    if x >= 0 and y >= 0 and x < WIDTH and y < HEIGHT:
        pygame.draw.rect(
            _VARS['surf'], color,
            (x, y, PIXEL, PIXEL)
        )


def placeCell():
    for row in range(cellMap.shape[0]):
        for col in range(cellMap.shape[1]):
            if(cellMap[row][col] != BLACK):
                drawCell(
                    _VARS['gridOrigin'][0] + (PIXEL*col),
                    _VARS['gridOrigin'][1] + (PIXEL*row),
                    cellMap[row][col]
                )


def drawNum(num, y, x):
    for digit in num:
        digit = grid_text.numDict[digit]
        for row in range(0, digit.shape[0]):
            for col in range(0, digit.shape[1]):
                if(tuple(digit[row][col]) != BLACK):
                    drawCell(
                        _VARS['gridOrigin'][0] + (PIXEL*col + PIXEL*x),
                        _VARS['gridOrigin'][1] + (PIXEL*row + PIXEL*y),
                        digit[row][col]
                    )
        x = x + 4


def drawLogo(logo, y, x):
    for row in range(0, logo.shape[0]):
        for col in range(0, logo.shape[1]):
            if(tuple(logo[row][col]) != BLACK):
                drawCell(
                    _VARS['gridOrigin'][0] + (PIXEL*col + PIXEL*x),
                    _VARS['gridOrigin'][1] + (PIXEL*row + PIXEL*y),
                    logo[row][col]
                )


def checkEvents():
    global killThreads
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            test.killThreads = True
            killThreads = True
        elif event.type == KEYDOWN and event.key == K_q:
            test.killThreads = True
            killThreads = True


def split(str):
    return [char for char in str]


if __name__ == '__main__':
    main()
