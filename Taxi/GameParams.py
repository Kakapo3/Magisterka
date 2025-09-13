import random

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800
ROWS = 8
COLS = 8
BLOCK = WINDOW_WIDTH // ROWS

POSSIBLE_MOVES = [0, 1, 2, 3, 4, 5] # 0 up, 1 right, 2 down, 3 left , 4 pick up, 5 drop

startingPlayerX = 0
startingPlayerY = 0

startingPassengerX = 4
startingPassengerY = 4

startingDestinationX = 7
startingDestinationY = 7

move = 0

passengerPickedUp = False

passengerDelivered = False

board = [[[] for x in range(COLS)] for y in range(ROWS)]

board[startingPlayerY][startingPlayerX].append(1)
board[startingPassengerY][startingPassengerX].append(2)
board[startingDestinationY][startingDestinationX].append(3)

board[1][5].append(4)
board[2][4].append(4)
board[4][2].append(4)
board[7][6].append(4)
board[3][4].append(4)
board[2][4].append(4)
board[2][2].append(4)
board[3][2].append(4)
board[6][2].append(4)
board[3][3].append(4)