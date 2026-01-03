import torch.nn as nn
import torch.optim as optim
import GameParams
from collections import deque

import qLearningParams

state_size = 2+2*(len(GameParams.POSSIBLE_SPAWNS)+1) # [px, py, passenger_id, destination_id]
print("STATE SIZE", state_size)
action_size = 6 # 0 up, 1 right, 2 down, 3 left , 4 pick up, 5 drop

model = nn.Sequential(
    nn.Linear(state_size, 64),
    nn.ReLU(),
    nn.Linear(64, 64),
    nn.ReLU(),
    nn.Linear(64, action_size)
)

model_target = nn.Sequential(
    nn.Linear(state_size, 64),
    nn.ReLU(),
    nn.Linear(64, 64),
    nn.ReLU(),
    nn.Linear(64, action_size)
)

model_target.load_state_dict(model.state_dict())

optimizer = optim.Adam(model.parameters(), lr=qLearningParams.learningRate)
criterion = nn.MSELoss()

memory = deque(maxlen=50000)

batchSize = 64
positive_fraction = 0.5

exploRateBase = 100
minExploRate = 0.1

target_update_freq = 1000