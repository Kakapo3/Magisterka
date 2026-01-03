import GameParams

qTable = []
previousState = []
currentState = []

reward = 0
gamma = 0.99
learningRate = 0.0001
explorationRate = 1

RewardEnd = 50
RewardPickupPassenger = 20
RewardIllegalPickupOrDropoff = -10
RewardMoveIntoWall = -5
RewardEmptyMove = -1
RewardEmptyMoveGoodDir = 3
RewardEmptyMoveBadDir = -3