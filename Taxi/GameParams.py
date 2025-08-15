import random

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800
ROWS = 4
COLS = 4
BLOCK = WINDOW_WIDTH // ROWS


startingPlayerX = 3
startingPlayerY = 3

startingPassengerX = 0
startingPassengerY = 0

startingDestinationX = 0
startingDestinationY = 3

move = 0

passengerPickedUp = False

passengerDelivered = False

board = [[[] for x in range(COLS)] for y in range(ROWS)]

board[startingPlayerY][startingPlayerX].append(1)
board[startingPassengerY][startingPassengerX].append(2)
board[startingDestinationY][startingDestinationX].append(3)

board[1][0].append(4)
board[2][1].append(4)
board[1][2].append(4)