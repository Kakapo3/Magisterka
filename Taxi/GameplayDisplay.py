import pygame

import GameParams
from GameplayLogic import *

screen = pygame.display.set_mode((GameParams.WINDOW_HEIGHT, GameParams.WINDOW_WIDTH))
pygame.display.set_caption("Taxi")

def updateWindow():
    clearScreen()
    drawDestination()
    drawPassenger()
    drawPlayer()
    pygame.display.update()

def clearScreen():
    screen.fill('Black')

def drawPlayer():
    pygame.draw.rect(screen, 'Green', pygame.Rect(GameParams.playerX * GameParams.BLOCK,
                                                  GameParams.playerY * GameParams.BLOCK,
                                                  GameParams.BLOCK,
                                                  GameParams.BLOCK))
    if GameParams.passengerPickedUp:
        pygame.draw.circle(screen, 'Blue', ((GameParams.playerX + 0.5)*GameParams.BLOCK, (GameParams.playerY+0.5)*GameParams.BLOCK), GameParams.BLOCK/2, 0)

def drawPassenger():
    if not GameParams.passengerPickedUp:
        pygame.draw.circle(screen, 'Blue', ((GameParams.passengerX + 0.5)*GameParams.BLOCK, (GameParams.passengerY+0.5)*GameParams.BLOCK), GameParams.BLOCK/2, 0)

def drawDestination():
    pygame.draw.rect(screen, 'Yellow', pygame.Rect(GameParams.destinationX * GameParams.BLOCK,
                                                 GameParams.destinationY * GameParams.BLOCK,
                                                 GameParams.BLOCK,
                                                 GameParams.BLOCK))