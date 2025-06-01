import numpy as np
import random

class TaxiEnv:
    def __init__(self, obstacles=None):
        self.grid_size = 7
        self.passenger_locs = {'A': (0, 0), 'B': (6, 1), 'C': (6, 6), 'D': (2, 6)}
        self.obstacles = obstacles if obstacles else []  
        self.reset()

    def reset(self, passenger_loc=None, destination=None):
        self.taxi_pos = (random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1))
        
        while self.taxi_pos in self.obstacles:
            self.taxi_pos = (random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1))

        if passenger_loc and passenger_loc in self.passenger_locs:
            self.passenger_loc = passenger_loc
        else:
            self.passenger_loc = random.choice(list(self.passenger_locs.keys()))
        
        if destination and destination in self.passenger_locs and destination != self.passenger_loc:
            self.destination = destination
        else:
            self.destination = random.choice([k for k in self.passenger_locs.keys() if k != self.passenger_loc])
        
        self.has_passenger = False
        return self.get_state()

    def get_state(self):
        return (self.taxi_pos[0], self.taxi_pos[1], self.passenger_loc, self.destination, self.has_passenger)

    def step(self, action):
        reward = -1
        row, col = self.taxi_pos

        if action == 'up':
            new_pos = (max(0, row - 1), col)
        elif action == 'down':
            new_pos = (min(self.grid_size - 1, row + 1), col)
        elif action == 'left':
            new_pos = (row, max(0, col - 1))
        elif action == 'right':
            new_pos = (row, min(self.grid_size - 1, col + 1))
        else:
            new_pos = (row, col)

        if action in ['up', 'down', 'left', 'right'] and new_pos in self.obstacles:
            reward = -5
            new_pos = self.taxi_pos
        else:
            self.taxi_pos = new_pos

        if action == 'pickup':
            if not self.has_passenger and self.taxi_pos == self.passenger_locs[self.passenger_loc]:
                self.has_passenger = True
                reward = 0
            else:
                reward = -10
        elif action == 'dropoff':
            if self.has_passenger and self.taxi_pos == self.passenger_locs[self.destination]:
                reward = 20
                return self.get_state(), reward, True  # Selesai episode
            else:
                reward = -10

        return self.get_state(), reward, False

    def get_actions(self):
        return ['up', 'down', 'left', 'right', 'pickup', 'dropoff']

    def render(self, ax):
        ax.clear()
        ax.set_xticks(np.arange(0, self.grid_size+1))
        ax.set_yticks(np.arange(0, self.grid_size+1))
        ax.grid(True)
        ax.set_xlim(-0.5, self.grid_size-0.5)
        ax.set_ylim(-0.5, self.grid_size-0.5)
        ax.invert_yaxis()

        for name, (r, c) in self.passenger_locs.items():
            ax.text(c, r, name, ha='center', va='center', fontsize=12,
                    bbox=dict(facecolor='white', edgecolor='black'))

        for (r, c) in self.obstacles:
            ax.plot(c, r, 's', markersize=30, color='red')

        taxi_color = 'blue' if not self.has_passenger else 'orange'
        ax.plot(self.taxi_pos[1], self.taxi_pos[0], 's', markersize=30, color=taxi_color)
