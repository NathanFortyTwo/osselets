from cleangame import Osselets
from stable_baselines3 import PPO
import numpy as np

MAX_AGENT_TRIES = 15

loaded_agent = PPO.load("agent")
game=  Osselets()

#player 0 is the human player
#player 1 is the agent

while not game.is_done():
        
        # Actions contain the actions for player1 and player2 respectively
        dice0 = game.players[0].roll_dice()        

        player0_action = int(input(f"You rolled a {dice0}, Enter a row index: \n\n"))

        while player0_action not in game.players[0].get_valid_rows():
            player0_action = int(input(f"Invalid row, Enter a row index:\n"))
            
        game.players[0].place_dice(player0_action) # human action
        game.players[1].self_update_board(dice0,player0_action) # agent action

        if game.is_done():
              break
        
        # bot turn
        dice1 = game.players[1].roll_dice()
        state = np.concatenate((game.players[0].board,game.players[1].board),axis=1)
        loaded_agent_action, _ = loaded_agent.predict(state)
        c=0
        while loaded_agent_action not in game.players[1].get_valid_rows():
            c+=1
            loaded_agent_action = loaded_agent.predict(state)  

            if c>MAX_AGENT_TRIES:
                print("Agent failed to make a valid move, random move is made")
                loaded_agent_action = np.random.choice(game.players[1].get_valid_rows())

        game.players[1].place_dice(loaded_agent_action)
        game.players[0].self_update_board(dice1,loaded_agent_action) # agent action

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
