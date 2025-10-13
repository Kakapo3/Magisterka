import sys
import time

import pygame

import GameParams
import GameplayLogic
import dqLearning
import dqnParams
import qLearning
import qLearningParams
from GameplayDisplay import *
from qLearning import *

print("Hello")

def runGameQLearning():
    pygame.init()

    qLearningParams.currentState = qLearning.getState(GameParams.board)
    qLearningParams.previousState = qLearning.getState(GameParams.board)

    running = True
    moveCounter = 0

    respawnPassenger()
    respawnDestination()

    while running:
        qLearningParams.previousState = qLearningParams.currentState
        updateWindow()
        #time.sleep(0.2)
        GameParams.move = qLearning.chooseMove()
        moveEffect(GameParams.move)
        qLearningParams.currentState = qLearning.getState(GameParams.board)
        qLearning.getReward()
        qLearning.learn()
        qLearning.reduceExplorationRate()

        maybeRestart()
        moveCounter += 1



        if moveCounter >= 500000:
            time.sleep(0.2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


    pygame.quit()


def runGameDeepQLearning():
    pygame.init()

    qLearningParams.currentState = qLearning.getState(GameParams.board)
    qLearningParams.previousState = qLearning.getState(GameParams.board)

    running = True

    respawnPassenger()
    respawnDestination()

    while running:
        qLearningParams.previousState = qLearningParams.currentState
        updateWindow()
        #time.sleep(0.2)
        GameParams.move = dqLearning.chooseMove()
        moveEffect(GameParams.move)
        qLearningParams.currentState = qLearning.getState(GameParams.board)
        qLearning.getReward()
        dqLearning.learn()
        #qLearning.reduceExplorationRate()

        print(GameParams.moveCounter/GameParams.maxMoves)
        print(dqLearning.getExploRate(dqnParams.exploRateBase))

        maybeRestart()
        GameParams.moveCounter += 1

        if GameParams.moveCounter >= GameParams.maxMoves:
            time.sleep(0.2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


    pygame.quit()


#runGameQLearning()
runGameDeepQLearning()