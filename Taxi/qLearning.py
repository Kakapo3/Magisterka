import GameParams
import GameplayLogic
import qLearningParams


def getState(board):
    px, py = GameplayLogic.getEntityPos(board, 1)
    passenger = 1 if GameParams.passengerPickedUp else 0
    return [px, py, passenger]

def getReward():
    print(qLearningParams.previousState, GameParams.move, qLearningParams.currentState)
    if GameParams.passengerDelivered: reward = 100
    elif qLearningParams.currentState[2] == 1 and qLearningParams.previousState[2] == 0: reward = 50
    elif GameParams.move == 4 or GameParams.move == 5: reward = -50
    else: reward = -1
    qLearningParams.reward = reward