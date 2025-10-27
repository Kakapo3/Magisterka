import random

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800
ROWS = 6
COLS = 6
BLOCK = WINDOW_WIDTH // ROWS

POSSIBLE_MOVES = [0, 1, 2, 3, 4, 5] # 0 up, 1 right, 2 down, 3 left , 4 pick up, 5 drop

moveCounter = 0
maxMoves = 250000
#exploRateDiscount = 1/maxMoves
move = 0

POSSIBLE_SPAWN_POINTS = [[0, 0], [0, 2], [3, 1], [4, 5], [5, 4]]
POSSIBLE_SPAWNS = list(range(1, len(POSSIBLE_SPAWN_POINTS) + 1))

startingPlayerX = POSSIBLE_SPAWN_POINTS[0][1]
startingPlayerY = POSSIBLE_SPAWN_POINTS[0][0]

startingPassengerX = POSSIBLE_SPAWN_POINTS[1][1]
startingPassengerY = POSSIBLE_SPAWN_POINTS[1][0]

startingDestinationX = POSSIBLE_SPAWN_POINTS[2][1]
startingDestinationY = POSSIBLE_SPAWN_POINTS[2][0]

passenger_id = 0
destination_id = 0

passengerPickedUp = False
passengerDelivered = False

board = [[[] for x in range(COLS)] for y in range(ROWS)]

board[startingPlayerY][startingPlayerX].append(1)
board[startingPassengerY][startingPassengerX].append(2)
board[startingDestinationY][startingDestinationX].append(3)

board[0][1].append(4)
board[2][1].append(4)
board[2][2].append(4)
board[4][2].append(4)
board[3][2].append(4)
board[3][4].append(4)
board[0][4].append(4)
board[1][4].append(4)
board[4][4].append(4)
board[5][5].append(4)
#board[3][6].append(4)
#board[6][7].append(4)
#board[7][2].append(4)
#board[6][5].append(4)
#board[7][5].append(4)