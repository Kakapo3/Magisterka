import torch.nn as nn
import torch.optim as optim
import GameParams
from collections import deque

state_size = 2+2*(len(GameParams.POSSIBLE_SPAWNS)+1) # [px, py, passenger_id, destination_id]
action_size = 6 # 0 up, 1 right, 2 down, 3 left , 4 pick up, 5 drop

model = nn.Sequential(
            nn.Linear(state_size, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, action_size)
        )

optimizer = optim.Adam(model.parameters(), lr=0.01)
criterion = nn.MSELoss()

memory = deque(maxlen=50000)

batchSize = 100

exploRateBase = 10