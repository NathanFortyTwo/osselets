from cleangame import Osselets
import random

import gym
from gym import spaces
import numpy as np

#player 1 is the agent
#player 2 is a fake player playing randomly

class OsseletsEnv(gym.Env):
    def __init__(self):
        super(OsseletsEnv, self).__init__()

        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Box(low=-1, high=1, shape=(3,7), dtype=np.uint8)

        self.reset()

    def reset(self):
        #TODO ADD DICE VALUE TO STATE

        self.game = Osselets()
        self.state = self.game.getstate()
        return self.state

    def step(self, action):
        done = False
        # Actions contain the actions for player1 and player2 respectively
        player1_action = action
        valid_actions = self.game.players[0].get_valid_rows()

        if player1_action not in valid_actions:
            reward = -500
            done = True
            self.state = self.game.getstate()

            return self.state, reward, done, {}
        
        self.game.players[0].place_dice(player1_action)

        dice1 = self.game.players[1].roll_dice()
        valid_actions = self.game.players[1].get_valid_rows()
        random_action = random.choice(valid_actions)
        self.game.players[1].place_dice(random_action)
        
        dice0 = self.game.players[0].roll_dice()        

        score0 = self.game.players[0].get_score()
        score1 = self.game.players[1].get_score()

        reward = score0 - score1
        # Check for terminal conditions
        if self.game.is_done():
            done = True
            if score0 > score1:
                reward = 150
        self.state = self.game.getstate()
        return self.state, reward, done, {}

    def render(self, mode='human'):
        pass

    def close(self):
        pass


def main():
    env = OsseletsEnv()
    c=0
    for _ in range(1):
        env.reset()
        done = False
        global_reward = 0
        while not done:
            c+=1
            valid_actions = env.game.players[0].get_valid_rows()
            action = random.choice(valid_actions)

            state, reward, done, _ = env.step(action)
            global_reward += reward
            env.render()
            if done or c>100:
                print(f"Game Over! Rewards: {global_reward}\n")


if __name__ == "__main__":
    main()
