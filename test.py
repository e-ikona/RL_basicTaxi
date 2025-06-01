from taxi_env import TaxiEnv
from q_learning_agent import QLearningAgent
from pygame_visual import run_simulation_with_recorded_steps

obstacles = [(2, 2), (3, 1), (1, 3)]
env = TaxiEnv(obstacles=obstacles)
agent = QLearningAgent(actions=env.get_actions())
agent.load_q_table("model/qtable.pkl")

visualize_passenger_loc = 'B'
visualize_destination = 'D'

combinations = [(p, d) for p in env.passenger_locs for d in env.passenger_locs if p != d]
episodes_per_combination = 10
total_episodes = episodes_per_combination * len(combinations)

successful_episode_steps = None
successes = 0

for passenger_loc, destination in combinations:
    for ep in range(episodes_per_combination):
        state = env.reset(passenger_loc=passenger_loc, destination=destination)
        done = False
        step_count = 0
        max_steps = 100
        steps = []
        total_reward = 0

        while not done and step_count < max_steps:
            action_idx = agent.choose_action(state, training=False)
            action = env.get_actions()[action_idx]

            next_state, reward, done = env.step(action)

            # Simpan langkah tanpa done agar sesuai unpack di visual
            steps.append((env.taxi_pos, env.has_passenger, action))

            state = next_state
            total_reward += reward
            step_count += 1

        status = "BERHASIL" if done and reward == 20 else "GAGAL"
        print(f"Passenger: {passenger_loc} -> Destination: {destination} | Episode {ep+1}: Total Reward = {total_reward} | Steps = {step_count} | Status: {status}")

        if done and reward == 20:
            successes += 1
            if passenger_loc == visualize_passenger_loc and destination == visualize_destination:
                if successful_episode_steps is None:
                    successful_episode_steps = (env, steps, passenger_loc, destination, status)

print(f"\nTotal sukses: {successes}/{total_episodes}")
print(f"Akurasi: {successes / total_episodes * 100:.2f}%")

if successful_episode_steps:
    env, steps, passenger_loc, destination, status = successful_episode_steps
    print(f"\nVisualisasi episode berhasil untuk penjemputan {passenger_loc} dan tujuan {destination}")
    run_simulation_with_recorded_steps(env, steps, passenger_loc, destination, status)
else:
    print(f"\nTidak ada episode berhasil untuk visualisasi pada titik jemput {visualize_passenger_loc} dan tujuan {visualize_destination}.")
