import random

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
ROWS = 20
COLS = 20
BLOCK = WINDOW_WIDTH // ROWS

POSSIBLE_MOVES = [0, 1, 2, 3, 4, 5] # 0 up, 1 right, 2 down, 3 left , 4 pick up, 5 drop

moveCounter = 0
maxMoves = 1000000
#exploRateDiscount = 1/maxMoves
move = 0

#POSSIBLE_SPAWN_POINTS = [[0, 1], [2, 5], [0, 8], [4, 4], [6, 9], [9, 3], [4, 1], [9, 8], [12, 6]]
POSSIBLE_SPAWN_POINTS = [[0, 1], [13, 0], [7, 4], [13, 8], [19, 3], [9, 14], [13, 19], [2, 19], [3, 10], [15, 5], [17, 14], [19, 19]]
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


board[0][8].append(4)
board[7][5].append(4)
board[2][2].append(4)
board[3][5].append(4)
board[9][7].append(4)
board[1][5].append(4)
board[3][2].append(4)
board[6][4].append(4)
board[5][8].append(4)
board[3][9].append(4)
board[2][6].append(4)
board[8][4].append(4)
board[0][3].append(4)
board[1][1].append(4)
board[2][9].append(4)
board[4][8].append(4)
board[6][9].append(4)
board[8][3].append(4)
board[2][2].append(4)
board[3][1].append(4)
board[6][5].append(4)
board[7][7].append(4)
board[9][9].append(4)
board[0][0].append(4)
board[2][7].append(4)
board[1][4].append(4)
board[4][3].append(4)

board[12][6].append(4)
board[16][5].append(4)
board[17][3].append(4)
board[19][2].append(4)
board[17][3].append(4)
board[16][5].append(4)
board[14][8].append(4)
board[13][9].append(4)
board[12][4].append(4)
board[18][3].append(4)
board[10][2].append(4)
board[15][1].append(4)
board[13][7].append(4)
board[11][9].append(4)
board[12][3].append(4)
board[15][4].append(4)
board[17][7].append(4)
board[19][9].append(4)
board[17][3].append(4)
board[14][1].append(4)
board[13][2].append(4)
board[12][0].append(4)
board[13][2].append(4)
board[18][3].append(4)
board[10][6].append(4)
board[18][5].append(4)
board[12][3].append(4)

board[4][13].append(4)
board[6][14].append(4)
board[8][15].append(4)
#board[2][18].append(4)
board[5][12].append(4)
board[4][11].append(4)
#board[2][18].append(4)
board[1][19].append(4)
board[8][13].append(4)
board[9][12].append(4)
board[5][14].append(4)
board[3][15].append(4)
board[1][17].append(4)
board[4][18].append(4)
board[3][19].append(4)
board[2][10].append(4)
board[8][11].append(4)
board[9][12].append(4)
board[3][13].append(4)
board[2][14].append(4)
board[9][15].append(4)
#board[0][18].append(4)
board[2][15].append(4)
board[1][12].append(4)
board[6][11].append(4)
board[8][17].append(4)
board[9][19].append(4)

board[13][18].append(4)
board[16][15].append(4)
board[18][12].append(4)
board[14][13].append(4)
board[11][18].append(4)
#board[15][16].append(4)
board[19][13].append(4)
board[10][14].append(4)
board[15][18].append(4)
board[13][14].append(4)
board[11][12].append(4)
board[13][11].append(4)
board[16][14].append(4)
board[18][16].append(4)
board[14][18].append(4)
board[12][19].append(4)
board[18][15].append(4)
board[19][18].append(4)
board[14][13].append(4)
board[16][17].append(4)
board[13][13].append(4)
board[11][17].append(4)
board[17][15].append(4)
board[18][12].append(4)
board[19][13].append(4)
board[14][17].append(4)
board[11][18].append(4)

#board[0][0].append(4)
#board[3][1].append(4)
#board[4][2].append(4)
#board[5][2].append(4)
#board[7][1].append(4)
#board[8][4].append(4)
#board[3][5].append(4)
#board[5][5].append(4)
#board[3][5].append(4)
#board[0][4].append(4)
#board[0][2].append(4)
#board[8][8].append(4)
#board[3][2].append(4)
#board[0][5].append(4)
#board[8][5].append(4)
#board[9][1].append(4)
#board[9][4].append(4)
#board[9][2].append(4)
#board[5][4].append(4)
#board[4][3].append(4)
#board[5][9].append(4)
#board[5][8].append(4)
#board[5][7].append(4)
#board[2][7].append(4)
#board[2][8].append(4)
#board[3][7].append(4)
#board[3][8].append(4)