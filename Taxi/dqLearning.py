import random

import torch
import torch.nn.functional as F

import GameParams
import GameplayLogic
import dqnParams
import qLearning
import qLearningParams


def getBestMove():
    with torch.no_grad():
        q_values = dqnParams.model(torch.FloatTensor(encode_state(qLearningParams.currentState)))
    return torch.argmax(q_values).item()

def chooseMove():
    print(torch.FloatTensor(encode_state(qLearningParams.currentState)))
    print(dqnParams.model(torch.FloatTensor(encode_state(qLearningParams.currentState))))
    roll = random.random()
    if roll < getExploRate(dqnParams.exploRateBase):
        return GameplayLogic.getRandomLegalMove()
    else:
        return getBestMove()


def encode_state(state):
    x = state[0]
    y = state[1]
    passenger = state[2]
    dest_id = state[3]
    # One-hot encode passenger flag and destination
    passenger_oh = F.one_hot(torch.tensor(passenger), num_classes=len(GameParams.POSSIBLE_SPAWNS)+1).float()
    dest_oh = F.one_hot(torch.tensor(dest_id), num_classes=len(GameParams.POSSIBLE_SPAWNS)+1).float()

    # Concatenate into one flat vector
    state_vector = torch.cat([
        torch.tensor([x, y]),
        passenger_oh,
        dest_oh
    ])
    return state_vector


def sample_minibatch(memory, batch_size, positive_fraction=0.1):
    # Split memory into positive and non-positive samples
    positive_samples = [m for m in memory if m[2] > 0]
    negative_samples = [m for m in memory if m[2] <= 0]

    # How many from each group
    num_positive = int(batch_size * positive_fraction)
    num_negative = batch_size - num_positive

    # Sample from each (handle cases where there aren’t enough)
    pos_batch = random.sample(positive_samples, min(num_positive, len(positive_samples))) if positive_samples else []
    neg_batch = random.sample(negative_samples, min(num_negative, len(negative_samples))) if negative_samples else []

    # Combine and fill up if needed
    minibatch = pos_batch + neg_batch
    if len(minibatch) < batch_size:
        minibatch += random.sample(memory, batch_size - len(minibatch))

    random.shuffle(minibatch)
    return minibatch


def learn():
    dqnParams.memory.append([encode_state(qLearningParams.previousState), GameParams.move, qLearningParams.reward, encode_state(qLearningParams.currentState)])
    if len(dqnParams.memory) < dqnParams.batchSize:
        return

    minibatch = sample_minibatch(dqnParams.memory, dqnParams.batchSize, positive_fraction=0.1)
    states = torch.stack([m[0] for m in minibatch])
    actions = torch.LongTensor([m[1] for m in minibatch])
    rewards = torch.FloatTensor([m[2] for m in minibatch])
    next_states = torch.stack([m[3] for m in minibatch])

    current_q = dqnParams.model(states).gather(1, actions.unsqueeze(1)).squeeze(1)
    max_next_q = dqnParams.model_target(next_states).max(1)[0] # Use target network
    target_q = rewards + qLearningParams.gamma * max_next_q

    loss = dqnParams.criterion(current_q, target_q.detach())
    dqnParams.optimizer.zero_grad()
    loss.backward()
    dqnParams.optimizer.step()

def getExploRate(base):
    return max(-(pow(base, GameParams.moveCounter/GameParams.maxMoves - 1)) + 1, dqnParams.minExploRate)

def updateTargetNetwork():
    dqnParams.model_target.load_state_dict(dqnParams.model.state_dict())
    print("Updated network")