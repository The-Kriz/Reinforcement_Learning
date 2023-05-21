import numpy as np
import matplotlib.pyplot as plt


num_arms = 10
arms_mean = np.random.normal(0, 1, num_arms)
def epsilon_greedy(Q, epsilon):
    if np.random.uniform(0, 1) < epsilon:
        
        action = np.random.choice(num_arms)
    else:
      
        action = np.argmax(Q)
    return action


def run_bandit(epsilon):
    
    Q = np.zeros(num_arms)
    
    N = np.zeros(num_arms)
    
    total_reward = 0
    avg_reward = np.zeros(1000)
    
    for episode in range(1000):
        
        action = epsilon_greedy(Q, epsilon)
        
        reward = np.random.normal(arms_mean[action], 1)
        
        N[action] += 1
        Q[action] += (reward - Q[action]) / N[action]
        
        total_reward += reward
        avg_reward[episode] = total_reward / (episode + 1)
    return avg_reward


avg_reward_0 = run_bandit(0)
avg_reward_01 = run_bandit(0.1)
avg_reward_001 = run_bandit(0.01)


plt.plot(avg_reward_0, label='epsilon=0')
plt.plot(avg_reward_01, label='epsilon=0.1')
plt.plot(avg_reward_001, label='epsilon=0.01')
plt.xlabel('Episode')
plt.ylabel('Average Reward')
plt.legend()
plt.show()
