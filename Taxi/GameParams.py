import random

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800
ROWS = 2
COLS = 2
BLOCK = WINDOW_WIDTH // ROWS


playerX = 1
playerY = 1

passengerX = random.randrange(0, COLS)
passengerY = random.randrange(0, ROWS)

destinationX = random.randrange(0, COLS)
destinationY = random.randrange(0, ROWS)

passengerPickedUp = False

board = [[0 for x in range(COLS)] for y in range(ROWS)]