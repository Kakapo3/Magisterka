import random

import GameParams


def clearBoard():
    GameParams.board = [[0 for x in range(GameParams.COLS)] for y in range(GameParams.ROWS)]

def updateBoard():
    clearBoard()
    GameParams.board[GameParams.playerY][GameParams.playerX] = 1

def getRandomLegalMove():
    moves = [0, 1, 2, 3, 4, 5] # 0 up, 1 right, 2 down, 3 left , 4 pick up, 5 drop
    if GameParams.playerX == 0:
        moves.remove(3) # Can't go left
    if GameParams.playerX == GameParams.COLS-1:
        moves.remove(1) # Can't go right
    if GameParams.playerY == 0:
        moves.remove(0) # Can't go left
    if GameParams.playerY == GameParams.ROWS-1:
        moves.remove(2) # Can't go right

    return random.choice(moves)

def moveEffect(move):
    if move <= 3: movePlayer(move)
    if move == 4: pickUpPassenger()
    if move == 5: dropOffPassenger()

def movePlayer(move):
    if move == 0: GameParams.playerY -= 1
    elif move == 1: GameParams.playerX += 1
    elif move == 2: GameParams.playerY += 1
    elif move == 3: GameParams.playerX -= 1

def pickUpPassenger():
    if GameParams.playerX == GameParams.passengerX and GameParams.playerY == GameParams.passengerY:
        GameParams.passengerPickedUp = True

def dropOffPassenger():
    if GameParams.passengerPickedUp and GameParams.playerX == GameParams.destinationX and GameParams.playerY == GameParams.destinationY:
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