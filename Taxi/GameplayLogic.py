import random

import GameParams
import testing


def getEntityPos(board, elem_id):
    for col in range(len(board)):
        for row in range(len(board[col])):
            if elem_id in board[col][row]:
                return row, col
    return False


def getRandomLegalMove():
    return random.choice(GameParams.POSSIBLE_MOVES) # 0 up, 1 right, 2 down, 3 left , 4 pick up, 5 drop

def moveEffect(move):
    if move <= 3: movePlayer(move)
    if move == 4: pickUpPassenger()
    if move == 5: dropOffPassenger()

def movePlayer(move):
    playerX, playerY = getEntityPos(GameParams.board, 1)
    GameParams.board[playerY][playerX].remove(1)
    if move == 0 and playerY != 0 and 4 not in GameParams.board[playerY-1][playerX]:   GameParams.board[playerY-1][playerX].append(1)
    elif move == 1 and playerX != GameParams.COLS-1 and 4 not in GameParams.board[playerY][playerX+1]: GameParams.board[playerY][playerX+1].append(1)
    elif move == 2 and playerY != GameParams.ROWS-1 and 4 not in GameParams.board[playerY+1][playerX] : GameParams.board[playerY+1][playerX].append(1)
    elif move == 3 and playerX != 0 and 4 not in GameParams.board[playerY][playerX-1]: GameParams.board[playerY][playerX-1].append(1)
    else: GameParams.board[playerY][playerX].append(1)

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

def respawnPassenger():
    while getEntityPos(GameParams.board, 2):
        GameParams.board[getEntityPos(GameParams.board, 2)[1]][getEntityPos(GameParams.board, 2)[0]].remove(2)
    GameParams.passenger_id = random.choice(GameParams.POSSIBLE_SPAWNS)
    passenger_coords = GameParams.POSSIBLE_SPAWN_POINTS[GameParams.passenger_id - 1]
    GameParams.board[passenger_coords[0]][passenger_coords[1]].append(2)

def respawnDestination():
    while getEntityPos(GameParams.board, 3):
        GameParams.board[getEntityPos(GameParams.board, 3)[1]][getEntityPos(GameParams.board, 3)[0]].remove(3)
    GameParams.destination_id = random.choice(GameParams.POSSIBLE_SPAWNS)
    while GameParams.destination_id == GameParams.passenger_id:
        GameParams.destination_id = random.choice(GameParams.POSSIBLE_SPAWNS)
    destination_coords = GameParams.POSSIBLE_SPAWN_POINTS[GameParams.destination_id - 1]
    GameParams.board[destination_coords[0]][destination_coords[1]].append(3)

def maybeRestart():
    if GameParams.passengerDelivered:
        #spawnPlayer()
        respawnPassenger()
        respawnDestination()
        GameParams.passengerPickedUp = False
        GameParams.passengerDelivered = False

