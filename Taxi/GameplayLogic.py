import random

import GameParams

def getEntityPos(board, id):
    for col in range(len(board)):
        for row in range(len(board[col])):
            if id in board[col][row]:
                return row, col

def getRandomLegalMove():
    playerX, playerY = getEntityPos(GameParams.board, 1)
    moves = [0, 1, 2, 3, 4, 5] # 0 up, 1 right, 2 down, 3 left , 4 pick up, 5 drop
    if playerX == 0:
        moves.remove(3) # Can't go left
    if playerX == GameParams.COLS-1:
        moves.remove(1) # Can't go right
    if playerY == 0:
        moves.remove(0) # Can't go left
    if playerY == GameParams.ROWS-1:
        moves.remove(2) # Can't go right

    return random.choice(moves)

def moveEffect(move):
    if move <= 3: movePlayer(move)
    if move == 4: pickUpPassenger()
    if move == 5: dropOffPassenger()

def movePlayer(move):
    playerX, playerY = getEntityPos(GameParams.board, 1)
    GameParams.board[playerY][playerX] = 0
    if move == 0:   GameParams.board[playerY+1][playerX].append(1)
    elif move == 1: GameParams.board[playerY][playerX+1].append(1)
    elif move == 2: GameParams.board[playerY-1][playerX].append(1)
    elif move == 3: GameParams.board[playerY][playerX-1].append(1)

def pickUpPassenger():
    playerX, playerY = getEntityPos(GameParams.board, 1)
    passengerX, passengerY = getEntityPos(GameParams.board, 2)
    if playerX == passengerX and playerY == passengerY:
        GameParams.passengerPickedUp = True

def dropOffPassenger():
    playerX, playerY = getEntityPos(GameParams.board, 1)
    destinationX, destinationY = getEntityPos(GameParams.board, 2)
    if GameParams.passengerPickedUp and playerX == destinationX and playerY == destinationY:
        print("YIPEEE!")
        GameParams.passengerPickedUp = False
        spawnPassengerAndDestination()


def spawnPlayer():
    GameParams.playerX = random.randrange(GameParams.COLS)
    GameParams.playerY = random.randrange(GameParams.ROWS)

def spawnPassengerAndDestination():
    GameParams.passengerX = random.randrange(0, GameParams.COLS)
    GameParams.passengerY = random.randrange(0, GameParams.ROWS)

    GameParams.destinationX = random.randrange(0, GameParams.COLS)
    GameParams.destinationY = random.randrange(0, GameParams.ROWS)
    while GameParams.passengerX == GameParams.destinationX and GameParams.passengerY == GameParams.destinationY:
        GameParams.destinationX = random.randrange(0, GameParams.COLS)
        GameParams.destinationY = random.randrange(0, GameParams.ROWS)