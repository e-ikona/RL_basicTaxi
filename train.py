from taxi_env import TaxiEnv
from q_learning_agent import QLearningAgent
import matplotlib.pyplot as plt

env = TaxiEnv(obstacles=[(1, 1), (2, 2), (3, 3)])
actions = env.get_actions()
agent = QLearningAgent(actions)

episodes_per_combination = 1000
combinations = [(p, d) for p in env.passenger_locs for d in env.passenger_locs if p != d]
total_episodes = episodes_per_combination * len(combinations)

max_steps = 200  # batas maksimal step per episode untuk menghindari freeze

print(f"Mulai training {total_episodes} episode...")

for episode_num, (passenger_loc, destination) in enumerate(combinations * episodes_per_combination):
    state = env.reset(passenger_loc=passenger_loc, destination=destination)
    done = False
    step_count = 0
    
    while not done and step_count < max_steps:
        action_index = agent.choose_action(state)
        action = actions[action_index]
        next_state, reward, done = env.step(action)
        agent.learn(state, action_index, reward, next_state)
        state = next_state
        step_count += 1

        if step_count % 50 == 0:
            print(f"Episode {episode_num + 1}, Step {step_count}")

    if step_count >= max_steps:
        print(f"Episode {episode_num + 1} berhenti karena mencapai batas maksimal step ({max_steps})")

    if (episode_num + 1) % 500 == 0:
        print(f"Episode {episode_num + 1}/{total_episodes} selesai")

agent.save_q_table("model/qtable.pkl")
