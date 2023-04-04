import gym
import numpy as np
import time


def gymActivation(grid):
    env = gym.make('FrozenLake-v1', desc=grid, map_name="4x4", is_slippery=False)
    # We re-initialize the Q-table
    qtable = np.zeros((env.observation_space.n, env.action_space.n))

    # Hyper parameters
    episodes = 9000  # Total number of episodes
    alpha = 0.5  # Learning rate
    gamma = 0.9  # Discount factor

    # List of outcomes to plot
    outcomes = []

    # Training
    for _ in range(episodes):

        state = env.reset()[0]

        done = False

        # By default, we consider our outcome to be a failure
        outcomes.append("Failure")

        # Until the agent gets stuck in a hole or reaches the goal, keep training it
        while not done:
            # Choose the action with the highest value in the current state

            if np.max(qtable[state]) > 0:
                action = np.argmax(qtable[state])

            # If there's no best action (only zeros), take a random one
            else:
                action = env.action_space.sample()

            # Implement this action and move the agent in the desired direction
            new_state, reward, done, info,_ = env.step(action)

            # Update Q(s,a)
            qtable[state, action] = qtable[state, action] + \
                                    alpha * (reward + gamma * np.max(qtable[new_state]) - qtable[state, action])

            # Update our current state
            state = new_state

            # If we have a reward, it means that our outcome is a success
            if reward:
                outcomes[-1] = "Success"

    return env, qtable


def seq(env, qtable):
    state = env.reset()[0]
    done = False
    sequence = []

    while not done:
    # Choose the action with the highest value in the current state
        if np.max(qtable[state]) > 0:
            action = np.argmax(qtable[state])

    # If there's no best action (only zeros), take a random one
        else:
            action = env.action_space.sample()

    # Add the action to the sequence
        sequence.append(action)

    # Implement this action and move the agent in the desired direction
        new_state, reward, done, info,_= env.step(action)

    # Update our current state
        state = new_state

        time.sleep(1)

    return sequence


def PathText(sequence):
    path = []
    for i in sequence:
        if i == 0:
            text = "Left"
            path.append(text)
            # print(text)
        elif i == 1:
            text = "Backward"
            path.append(text)
            # print(text)
        elif i == 2:
            text = "Right"
            path.append(text)
            # print(text)
        elif i == 3:
            text = "Forward"
            path.append(text)
            # print(text)
        else:
            print("error")
    print(path)
    return path
