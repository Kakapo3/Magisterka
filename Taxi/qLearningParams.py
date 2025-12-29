import GameParams

qTable = []
previousState = []
currentState = []

reward = 0
gamma = 0.75
learningRate = 0.01
explorationRate = 1

RewardEnd = 100
RewardPickupPassenger = 50
RewardIllegalPickupOrDropoff = -50
RewardMoveIntoWall = -25
RewardEmptyMove = -5