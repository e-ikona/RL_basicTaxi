import numpy as np
import random
import pickle

class QLearningAgent:
    def __init__(self, actions, learning_rate=0.1, discount_factor=0.99, epsilon=1.0, epsilon_decay=0.9995, epsilon_min=0.01):
        self.actions = actions
        self.lr = learning_rate
        self.gamma = discount_factor
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
        self.q_table = {} 

    def get_q_values(self, state):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(len(self.actions))
        return self.q_table[state]

    def choose_action(self, state, training=True):
        q_values = self.get_q_values(state)
        if training and random.random() < self.epsilon:
            return random.randint(0, len(self.actions) - 1)
        else:
            return int(np.argmax(q_values))

    def learn(self, state, action, reward, next_state):
        q_values = self.get_q_values(state)
        q_next = self.get_q_values(next_state)
        td_target = reward + self.gamma * np.max(q_next)
        td_error = td_target - q_values[action]
        q_values[action] += self.lr * td_error

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def save_q_table(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.q_table, f)
        print(f"Q-table saved to {filename}")

    def load_q_table(self, filename):
        try:
            with open(filename, 'rb') as f:
                self.q_table = pickle.load(f)
            print(f"Q-table loaded from {filename}")
        except FileNotFoundError:
            print(f"No saved Q-table found at {filename}, starting fresh.")
