import GameParams

qTable = []
previousState = []
currentState = []

reward = 0
gamma = 0.99
learningRate = 0.001
explorationRate = 1

RewardEnd = 100
RewardPickupPassenger = 50
RewardIllegalPickupOrDropoff = -50
RewardMoveIntoWall = -25
RewardEmptyMove = -1
RewardEmptyMoveGoodDir = 1
RewardEmptyMoveBadDir = -1