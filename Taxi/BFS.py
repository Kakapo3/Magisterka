import time
import GameParams
import GameplayLogic
import qLearningParams


def BFS(source):
    seenPoints = []
    currentPoints = [source]
    nextPoints = []
    currentDistance = 0

    #print(source)
    if not GameParams.passengerPickedUp and 2 in GameParams.board[source[0]][source[1]] or \
    GameParams.passengerPickedUp and 3 in GameParams.board[source[0]][source[1]]:
        return currentDistance + 1

    while currentPoints or nextPoints:
        for [y, x] in currentPoints:
            for neighbour in [[y+1, x], [y-1, x], [y, x+1], [y, x-1]]:

                if neighbour not in seenPoints and \
                neighbour not in currentPoints and \
                neighbour not in nextPoints and \
                0 <= neighbour[0] < GameParams.COLS and \
                0 <= neighbour[1] < GameParams.ROWS and \
                4 not in GameParams.board[neighbour[0]][neighbour[1]]:
                    if not GameParams.passengerPickedUp and 2 in GameParams.board[neighbour[0]][neighbour[1]] or \
                            GameParams.passengerPickedUp and 3 in GameParams.board[neighbour[0]][neighbour[1]]:
                        return currentDistance + 1
                    else:
                        nextPoints.append(neighbour)

        #print("Next points:", nextPoints)
        seenPoints = seenPoints + currentPoints
        currentPoints = nextPoints.copy()
        nextPoints = []
        currentDistance += 1
    print("TARGET NOT FOUND, SHUTTING DOWN")
    return None

def getBFSreward(prevState, currState):
    oldDistance = BFS([prevState[1], prevState[0]])
    newDistance = BFS([currState[1], currState[0]])
    #print("OldDistance:", oldDistance)
    #print("NewDistance:", newDistance)
    #print(oldDistance, "->", newDistance)
    if newDistance < oldDistance:
        return qLearningParams.RewardEmptyMoveGoodDir
    else:
        return qLearningParams.RewardEmptyMoveBadDir