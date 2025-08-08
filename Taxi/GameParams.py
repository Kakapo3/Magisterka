import random

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800
ROWS = 8
COLS = 8
BLOCK = WINDOW_WIDTH // ROWS


startingPlayerX = 1
startingPlayerY = 1

startingPassengerX = 2
startingPassengerY = 1

startingDestinationX = 6
startingDestinationY = 5

passengerPickedUp = False

board = [[[] for x in range(COLS)] for y in range(ROWS)]

board[startingPlayerY][startingPlayerX].append(1)
board[startingPassengerY][startingPassengerX].append(2)
board[startingDestinationY][startingDestinationX].append(3)

board[3][3].append(4)
board[3][4].append(4)
board[3][5].append(4)