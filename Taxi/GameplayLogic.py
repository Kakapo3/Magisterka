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
    if playerX > 0:
        if 4 in GameParams.board[playerY][playerX-1]: moves.remove(3)
    if playerX < GameParams.COLS-1:
        if 4 in GameParams.board[playerY][playerX+1]: moves.remove(1)
    if playerY > 0:
        if 4 in GameParams.board[playerY-1][playerX]: moves.remove(0)
    if playerY < GameParams.ROWS-1:
        if 4 in GameParams.board[playerY+1][playerX]: moves.remove(2)

    return random.choice(moves)

def moveEffect(move):
    if move <= 3: movePlayer(move)
    if move == 4: pickUpPassenger()
    if move == 5: dropOffPassenger()

def movePlayer(move):
    playerX, playerY = getEntityPos(GameParams.board, 1)
    GameParams.board[playerY][playerX].remove(1)
    if move == 0:   GameParams.board[playerY-1][playerX].append(1)
    elif move == 1: GameParams.board[playerY][playerX+1].append(1)
    elif move == 2: GameParams.board[playerY+1][playerX].append(1)
    elif move == 3: GameParams.board[playerY][playerX-1].append(1)

def pickUpPassenger():
    if not GameParams.passengerPickedUp:
        playerX, playerY = getEntityPos(GameParams.board, 1)
        passengerX, passengerY = getEntityPos(GameParams.board, 2)
        if playerX == passengerX and playerY == passengerY:
            GameParams.passengerPickedUp = True
            GameParams.board[playerY][playerX].remove(2)

def dropOffPassenger():
    if GameParams.passengerPickedUp:
        playerX, playerY = getEntityPos(GameParams.board, 1)
        destinationX, destinationY = getEntityPos(GameParams.board, 3)
        if playerX == destinationX and playerY == destinationY:
            print("YIPEEE!")
            GameParams.passengerDelivered = True


def spawnPlayer():
    playerX, playerY = getEntityPos(GameParams.board, 1)
    GameParams.board[playerY][playerX].remove(1)
    GameParams.board[GameParams.startingPlayerY][GameParams.startingPlayerX].append(1)

def spawnPassenger():
    GameParams.board[GameParams.startingPassengerY][GameParams.startingPassengerX].append(2)

def maybeRestart():
    if GameParams.passengerDelivered:
        spawnPlayer()
        spawnPassenger()
        GameParams.passengerPickedUp = False
        GameParams.passengerDelivered = False

