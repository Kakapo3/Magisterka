import matplotlib.pyplot as plt
import GameParams

scores = []
currScore = 0

def test():
    global currScore
    currScore += 1
    if GameParams.passengerDelivered:
        scores.append(currScore)
        currScore = 0

def generatePlot():
    print(scores)
    print(len(scores))
    plt.plot(scores)
    plt.show()
    plt.plot(scores)
    plt.yscale('log')
    plt.show()