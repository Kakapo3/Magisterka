import sys
import time

import pygame

import GameplayLogic
import qLearning
import qLearningParams
from GameplayDisplay import *
from qLearning import getReward

print("Hello")

pygame.init()

qLearningParams.currentState = qLearning.getState(GameParams.board)
qLearningParams.previousState = qLearning.getState(GameParams.board)

running = True
while running:

    qLearningParams.previousState = qLearningParams.currentState
    updateWindow()
    #time.sleep(0.1)
    GameParams.move = getRandomLegalMove()
    moveEffect(GameParams.move)
    qLearningParams.currentState = qLearning.getState(GameParams.board)
    getReward()
    print(qLearningParams.reward)

    maybeRestart()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()