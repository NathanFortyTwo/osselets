from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3 import PPO
from cleangym import OsseletsEnv

env = OsseletsEnv()
env = DummyVecEnv([lambda: env])
# Create the agent
#agent = PPO("MlpPolicy", env, verbose=1)
agent = PPO.load("agent", env=env, verbose=1)
agent.learn(total_timesteps=200_000)

# Save the agent
agent.save("../agent")

# Load the agent
#loaded_agent = PPO.load("path_to_save")
