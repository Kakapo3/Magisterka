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
    print("First 100 average:", sum(scores[:100])/len(scores[:100]))
    print("Total average:", sum(scores) / len(scores))
    print("Last 100 average:", sum(scores[-100:]) / len(scores[-100:]))
    plt.plot(scores)
    plt.xlabel('Epizod')
    plt.ylabel('Liczba ruchów')
    plt.show()
    plt.plot(scores)
    plt.yscale('log')
    plt.xlabel('Epizod')
    plt.ylabel('Liczba ruchów')
    plt.show()