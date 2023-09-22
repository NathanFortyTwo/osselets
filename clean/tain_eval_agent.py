import gym
import matplotlib.pyplot as plt
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy
from cleangym import OsseletsEnv
# Load your custom gym environment
env = OsseletsEnv()
env = DummyVecEnv([lambda: env])  # Wrap the environment to vectorize it

# Initialize the agent
model = PPO("MlpPolicy", env, verbose=1)

# Training parameters
n_steps = 50_000
eval_freq = 1000

# Lists to store results
eval_rewards = []
steps_list = []

for step in range(0, n_steps, eval_freq):
    # Train the agent
    model.learn(total_timesteps=eval_freq)
    
    # Evaluate the agent's performance
    mean_reward, _ = evaluate_policy(model, env, n_eval_episodes=10)
    
    # Store the results
    eval_rewards.append(mean_reward)
    steps_list.append(step + eval_freq)  # Adjust to indicate the end of the current training segment

# Plotting the results
plt.plot(steps_list, eval_rewards)
plt.xlabel('Training Steps')
plt.ylabel('Mean Reward')
plt.title('Training Performance')
plt.grid()
plt.savefig("graph.png")