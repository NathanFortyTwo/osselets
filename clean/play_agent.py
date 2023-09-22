from cleangame import Osselets
from stable_baselines3 import PPO
loaded_agent = PPO.load("agent")
import numpy as np

game=  Osselets()
#player 1 is the human player
#player 2 is the agent

while not game.is_done():
        
        # Actions contain the actions for player1 and player2 respectively
        dice0 = game.players[0].roll_dice()        

        player1_action = int(input(f"You rolled a {dice0}, Enter a row index: \n\n"))

        if player1_action not in game.players[0].get_valid_rows():
            break
        game.players[0].place_dice(player1_action) # human action

        if game.is_done():
              break
        
        # bot turn
        game.players[1].roll_dice()
        state = np.concatenate((game.players[0].board,game.players[1].board),axis=1)
        loaded_agent_action, _ = loaded_agent.predict(state)
        if loaded_agent_action not in game.players[1].get_valid_rows():
            break
        game.players[1].place_dice(loaded_agent_action)
        
        score0 = game.players[0].get_score()
        score1 = game.players[1].get_score()

        game.display_boards()

print(f"Player 0 score: {score0}")
print(f"Player 1 score: {score1}")

if score0>score1:
    print("Player 0 wins")
elif score0<score1:
    print("Player 1 wins")
else:
    print("Draw")
