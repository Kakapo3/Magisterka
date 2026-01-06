import random

import BFS
import GameParams
import GameplayLogic
import dqLearning
import dqnParams
import qLearningParams


# qTable = [[[[px, py, passenger_id, destination_id], action], reward], [[[px, py, passenger], action], reward], ...]

def stateActionInQtable(stateAction):
    for stateActionReward in qLearningParams.qTable:
        if stateActionReward[0] == stateAction:
            return True
    return False

def getQtableStateActions():
    stateActions = []
    for stateActionReward in qLearningParams.qTable:
        stateActions.append(stateActionReward[0])
    return stateActions

def getQtableBestMove(state):
    bestMoveId = -1
    bestMoveValue = -float('inf')
    for move in GameParams.POSSIBLE_MOVES: # 0 up, 1 right, 2 down, 3 left , 4 pick up, 5 drop
        if getQtableReward([state, move]) > bestMoveValue:
            bestMoveId = move
            bestMoveValue = getQtableReward([state, move])
    return [bestMoveId, bestMoveValue]

def getQtableReward(stateAction):
    if stateActionInQtable(stateAction):
        index = getQtableStateActions().index(stateAction)
        return qLearningParams.qTable[index][1]
    else:
        return 0

def getState(board):
    px, py = GameplayLogic.getEntityPos(board, 1)
    passenger = 0 if GameParams.passengerPickedUp else GameParams.passenger_id
    return [px, py, passenger, GameParams.destination_id]

def chooseMove():
    roll = random.random()
    #if roll < qLearningParams.explorationRate:
    if roll < dqLearning.getExploRate(dqnParams.exploRateBase):
        return GameplayLogic.getRandomLegalMove()
    else:
        return getQtableBestMove(qLearningParams.currentState)[0]

#def reduceExplorationRate():
#    qLearningParams.explorationRate -= GameParams.exploRateDiscount

def getReward():
    if GameParams.passengerDelivered: reward = qLearningParams.RewardEnd
    elif qLearningParams.currentState[2] == 0 and qLearningParams.previousState[2] != 0: reward = qLearningParams.RewardPickupPassenger
    elif GameParams.move == 4 or GameParams.move == 5: reward = qLearningParams.RewardIllegalPickupOrDropoff
    elif qLearningParams.currentState[0] == qLearningParams.previousState[0] and qLearningParams.currentState[1] == qLearningParams.previousState[1]: reward = qLearningParams.RewardMoveIntoWall
    #else: reward = qLearningParams.RewardEmptyMove
    else: reward = BFS.getBFSreward(qLearningParams.previousState, qLearningParams.currentState)
    #print(reward)
    qLearningParams.reward = reward

def learn():
    if not stateActionInQtable([qLearningParams.previousState, GameParams.move]):
        qLearningParams.qTable.append([[qLearningParams.previousState, GameParams.move], qLearningParams.reward])
    else:
        index = getQtableStateActions().index([qLearningParams.previousState, GameParams.move])
        currentValue = qLearningParams.qTable[index][1]
        newValue = qLearningParams.reward + qLearningParams.gamma * getQtableBestMove(qLearningParams.currentState)[1]
        qLearningParams.qTable[index][1] = (1-qLearningParams.learningRate) * currentValue + qLearningParams.learningRate * newValue