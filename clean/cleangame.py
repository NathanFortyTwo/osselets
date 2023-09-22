import random as rd
from numpy import transpose,array
from IPython.display import clear_output



def get_score_row(row):
    score = 0
    for index,value in enumerate(row):
        count = row.count(value)
        score+= value*count # if we have 5,5,3, the score is 5*2 + 5*2 +3 = 23
    return score


# game of osselets
class Player():
    def __init__(self):
        self.dice = 0
        self.board = [[0,0,0],[0,0,0],[0,0,0]]

    def get_valid_rows(self): 
        # row is valid if it contains at least one space, ie 0
        return [index for index,row in enumerate(self.board) if row.count(0)>0]
    
    def is_full(self):
        return not self.get_valid_rows()

    def place_dice(self,row_index):
        selected_row = self.board[row_index]
        try :
            place_index = selected_row.index(0) # find the first 0 in the column
        except IndexError:
            raise ValueError("Row is full")
        
        self.board[row_index][place_index] = self.dice


    def self_update_board(self,value,row_index):
        #to be done after the other player has placed a dice
        # if value is in the same column of the other player, replace it with 0
        row = self.board[row_index]

        # remove all occurences of value in row
        self.board[row_index] = [0 if x==value else x for x in row]


        
    def get_score(self):
        score = 0
        for row in self.board:
            score+= get_score_row(row)
        return score
    
    def roll_dice(self):
        self.dice = rd.randint(1,6)
        return self.dice
    


class Osselets():
    def __init__(self):
        self.players = [Player(),Player()]
        self.turn = 0
        self.done = False
    
    def is_done(self):
        return self.players[self.turn].is_full() or self.players[(self.turn+1)%2].is_full()
    
    def display_boards(self):
        clear_output()
        for player in self.players:
            #transpose the board to display it correctly
            board = transpose(array(player.board))
            print(f"Player {self.players.index(player)} board")
            for row in board:
                print(row)
            print("")

