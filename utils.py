import matplotlib.pyplot as plt
import time

def plot_rewards(rewards):
    plt.figure(figsize=(10, 5))
    plt.plot(rewards)
    plt.xlabel('Episode')
    plt.ylabel('Total Reward')
    plt.title('Learning Progress')
    plt.grid(True)
    plt.show()