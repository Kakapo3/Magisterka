import sys
import time

import pygame

import GameplayLogic
from GameplayDisplay import *

print("Hello")

pygame.init()


spawnPlayer()
spawnPassengerAndDestination()

running = True
while running:

    updateBoard()
    updateWindow()
    #time.sleep(1)
    move = getRandomLegalMove()
    print(move)
    moveEffect(move)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()