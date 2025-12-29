import pygame

import GameParams
from GameplayLogic import *

screen = pygame.display.set_mode((GameParams.WINDOW_HEIGHT, GameParams.WINDOW_WIDTH))
pygame.display.set_caption("Taxi")

def updateWindow():
    clearScreen()
    drawBoardEntities(GameParams.board)
    pygame.display.update()

def clearScreen():
    screen.fill('Black')

def drawPlayer(x, y):
    pygame.draw.rect(screen, 'Gold', pygame.Rect(x * GameParams.BLOCK,
                                                  y * GameParams.BLOCK,
                                                  GameParams.BLOCK,
                                                  GameParams.BLOCK))
    if GameParams.passengerPickedUp:
        pygame.draw.circle(screen, 'Blue', ((x + 0.5)*GameParams.BLOCK, (y+0.5)*GameParams.BLOCK), GameParams.BLOCK/2, 0)

def drawPassenger(x, y):
    pygame.draw.circle(screen, 'Blue', ((x + 0.5)*GameParams.BLOCK, (y+0.5)*GameParams.BLOCK), GameParams.BLOCK/2, 0)

def drawDestination(x, y):
    pygame.draw.rect(screen, 'Green', pygame.Rect(x * GameParams.BLOCK,
                                                 y * GameParams.BLOCK,
                                                 GameParams.BLOCK,
                                                 GameParams.BLOCK))

def drawWall(x, y):
    pygame.draw.rect(screen, 'Gray', pygame.Rect(x * GameParams.BLOCK,
                                                 y * GameParams.BLOCK,
                                                 GameParams.BLOCK,
                                                 GameParams.BLOCK))

def drawRespawns(x, y):
    if [x, y] in GameParams.POSSIBLE_SPAWN_POINTS:
        pygame.draw.rect(screen, 'Purple', pygame.Rect(y * GameParams.BLOCK,
                                                 x * GameParams.BLOCK,
                                                 GameParams.BLOCK,
                                                 GameParams.BLOCK))

def drawBoardEntities(board):
    for col in range(len(board)):
        for row in range(len(board[col])):
            #continue
            drawRespawns(row, col)

    for col in range(len(board)):
        for row in range(len(board[col])):
            for entity in board[col][row]:
                match entity:
                    case 1: drawPlayer(row, col)
                    case 2: drawPassenger(row, col)
                    case 3: drawDestination(row, col)
                    case 4: drawWall(row, col)