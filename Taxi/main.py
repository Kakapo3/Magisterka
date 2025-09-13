import sys
import time

import pygame

import GameplayLogic
import qLearning
import qLearningParams
from GameplayDisplay import *
from qLearning import *

print("Hello")

pygame.init()

qLearningParams.currentState = qLearning.getState(GameParams.board)
qLearningParams.previousState = qLearning.getState(GameParams.board)

running = True
moveCounter = 0
while running:
    qLearningParams.previousState = qLearningParams.currentState
    updateWindow()
    #time.sleep(0.2)
    GameParams.move = qLearning.chooseMove()
    moveEffect(GameParams.move)
    qLearningParams.currentState = qLearning.getState(GameParams.board)
    getReward()
    learn()
    reduceExplorationRate()
    print(qLearningParams.reward)
    print(qLearningParams.qTable)

    maybeRestart()
    moveCounter += 1

    if moveCounter >= 10000:
        time.sleep(0.2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()