import games
import copy
import itertools
import random
import time
from collections import namedtuple
import numpy as np
import sys
sys.setrecursionlimit(10000)
from games import Game
from games import GameState 



def my_eval_fn(state):
    '''This function can be used as the evaluation function for minimax cutoff decision/player
    and alpha beta cutoff decision/player. It intakes a state, and calculates the percentage of 
    the board that the relevant player has pieces over in comparison to the opponent.'''
    board = state.board
    calctotalX = 0
    calctotalO = 0
    for eachpiece in state.board:
        if board[eachpiece] == "X":
            calctotalX +=1
        if board[eachpiece] == "O":
            calctotalO +=1
    percent = round((calctotalX/calctotalO),3)
    if state.to_move == "X":
        return percent
    else:
        return 1-percent

def minmax_cutoff_decision(state, game, d, cutoff_test=None, eval_fn=None):
    """Given a state in a game, calculate the best move by searching
    forward all the way to the terminal states."""
    player = game.to_move(state)
    
    def max_value(state,depth):
        if cutoff_test(state,depth):
            return eval_fn(state)
        if game.terminal_test(state):
            return game.utility(state, player)
        v = -np.inf
        for a in game.actions(state):
            v = max(v, min_value(game.result(state, a), depth +1))
        return v

    def min_value(state,depth):
        if cutoff_test(state,depth):
            return eval_fn(state)
        if game.terminal_test(state):
            return game.utility(state, player)
        v = np.inf
        for a in game.actions(state):
            v = min(v, max_value(game.result(state, a), depth +1))
        return v
    cutoff_test = (cutoff_test or (lambda state, depth: depth > d or game.terminal_test(state)))
    return max(game.actions(state), key=lambda a: min_value(game.result(state, a),d))

def minmax_cutoff_player(depth,cutoff_test,eval_fn):
    '''This function can serve as a player of the Blobs game. It operates via the
    minmax_cutoff_decision function to select its moves.'''
    def fixedfunc(game,state):
        return minmax_cutoff_decision(state,game,depth,cutoff_test,eval_fn)
    return fixedfunc

def alpha_beta_cutoff_player(depth,cutoff_test,eval_fn):
    '''This function can serve as a player of the Blobs game. It operates via the
    alpha_beta_cutoff_decision function to select its moves.'''
    def fixedfunc(game,state):
        return games.alpha_beta_cutoff_search(state,game,depth,cutoff_test,eval_fn)
    return fixedfunc


class BLOBS(Game):
    def __init__(self, h=5, v=5) -> None:
        #Initialize your game here
        self.h = h
        self.v = v
        global passcount
        passcount = 0
        #Set the initial state for the game
        myboard={}
        myboard[1,1]="X"
        myboard[h,v]="X"
        myboard[h,1]="O"
        myboard[1,v]="O"
        
        moves = [(x, y) for x in range(1, h + 1)
                 for y in range(1, v + 1)]
        moves.remove((1,1))
        moves.remove((h,v))
        moves.remove((1,v))
        moves.remove((h,1))
        self.initial = GameState(to_move='X', utility=0.5, board=myboard, moves=moves)

    def actions(self, state: GameState) -> any:
        '''Intakes a state, returns a list of legal moves from that state. All actions will 
        appear as a list of tuples. Within the legalmoves list:
        If it is a "newpiece" action, you'll see [(xn, yn) , "new"].
        If it is a "move" action, you'll see [(xn, yn) , (xo,yo)]'''
        h = self.h
        v = self.v
        board = state.board
        legalmoves = []
        moves = state.moves
        
        for (x,y) in moves:
            if (x,y) not in board:#if there is no piece here, can place or move something here
                #implement "new" options- ensure it's one away from an existing piece
                canplacenew = False
                for each in board: #each is coords of an existing piece
                    if board[each]==state.to_move:#it's the correct type  
                        if each == (x+1,y) or (x-1,y) or (x,y+1) or (x,y-1):#if it's one away from current piece
                            canplacenew = True
                            break
                if canplacenew:
                    legalmoves.append([(x,y), "new"])
                    #add the action to legal moves
                
                #implement "move" options
                for each in board: #each is coords of an existing piece
                    if board[each]==state.to_move:#it's the correct type
                        if abs(each[0]-x)<3 and abs(each[1]-y)<3:#it's within 2 of x,y
                            legalmoves.append([(x,y),each])
        return legalmoves #will be a list of VALID moves at this state for the correct player

   
    def result (self, state: GameState, move:any) -> GameState:
        '''Intakes a state and a move, returns the resulting state from applying that move.'''
        global passcount
        
        if not move:#no possible moves-> increment the passcount
            passcount +=1
            return state
        if move[0] not in state.moves:#illegal move has no effect
            return state
        
        board = state.board.copy()
        moves=list(state.moves) 
        
        #if move is a new type:
        if move[1]=="new":
            board[move[0]] = state.to_move#just placing new item of type state.to_move
            
        #if move is a relocate type:
        else:
            del board[move[1]]
            board[move[0]] = state.to_move
            moves.append(move[1])#put the newly empty slot back in available moves list
            
        moves.remove(move[0])
        hold = GameState(to_move=('O' if state.to_move == 'X' else 'X'),
                         utility=self.compute_utility(board, move, state.to_move),
                         board=board, moves=moves) #new_state
        
        passcount = 0 #reset to 0 because no pass occurred this round
        return hold
    
    def terminal_test(self, state: GameState) -> bool:
        '''Tests if a state is terminal- that is, if it serves as the end of the game. Returns
        True if the board is an end state, False otherwise.'''
        global passcount
        if passcount == 2:
            return True
        return len(state.moves) == 0  #will return True if there are no empty squares
    
    def utility(self, state, player):
        """Intakes a state and a player, returns the utility value for that player; 
        1 for win, -1 for loss, 0 otherwise."""
        return state.utility if player == 'X' else -state.utility
    
    def compute_utility(self, board, move, player):#computes utility of X over O
        """Intakes a board, a move, and a player. If 'X' wins with this move, returns 1; 
        if 'O' wins returns -1; else returns 0."""
        h=self.h
        v=self.v
        board_size = h*v
        if board_size == len(board):#board is filled
            calctotalX = 0
            calctotalO = 0
            for each in board:
                if board[each] == "X":
                    calctotalX +=1
                if board[each] == "O":
                    calctotalO +=1
            if calctotalX>calctotalO:
                return 1
            elif calctotalX<calctotalO:
                return -1
            else:
                return 0
        else:
            return 0

    def display(self, state):
        '''This function will intake a state and display the board of that state. If the board is
        not the initial state, it will also display who wins at that state (as this is only called
        when the game is either initializing or finished).'''
        board = state.board
        Xcount = 0
        Ocount = 0
        if len(board)>4:#if not initial board, find winner, add winner to global resultaggregate
            for eachpiece in board:
                if board[eachpiece]=="X":
                    Xcount +=1
                elif board[eachpiece]=="O":
                    Ocount +=1
            global resultaggregate
            
            if Xcount > Ocount:
                print("X wins! Winning board:")
                resultaggregate.append("X")
            elif Xcount < Ocount:
                print("O wins! Winning board:")
                resultaggregate.append("O")
            else:
                print("MAJOR SEVERE ERROR OMG HELP AHHHH")
        
        for x in range(1, self.h + 1):
            for y in range(1, self.v + 1):
                print(board.get((x, y), '.'), end=' ')
            print()
        if Xcount !=0 and Ocount !=0:
            print("X placed", Xcount, "pieces.")
            print("O placed",Ocount,"pieces.")
        

def overall_winner(resultlist, playera, playerb):
    '''This function will take in a list of results from a matchup (5 games), as well as 
    the names of the players. It will print out: how many games each player won and who won overall,
    including the percent of games that it won.'''
    Xcount = 0
    Ocount = 0
    for each in resultlist:
        if each == "X":
            Xcount +=1
        elif each == "O":
            Ocount +=1
    print("In the 5 games between", playera, "and", playerb,":")
    print(playera,"(using piece X) won", Xcount, "games, and",playerb,"(using piece O) won", Ocount," games.")
    if Xcount>Ocount:
        percent = (Xcount/5)*100
        print(playera, "won overall!")
        print("It won", Xcount,"out of 5 rounds. That is", percent,  " percent!")
    else:
        percent = (Ocount/5)*100
        print(playerb, "won overall!")
        print("It won", Ocount,"out of 5 rounds. That is", percent,  " percent!")




def __main__():
    global resultaggregate
    mygame=BLOBS(5,5)
    print("Initial board for all rounds:")
    mygame.display(mygame.initial)
    print("")
    depth = 2


    #rand v rand
    print("#################################################")
    print("Matchup between 2 Random Players")
    resultaggregate = []
    roundstart = time.time()
    for i in range(5):
        start = time.time()
        print(" ")
        print("Round number:", i+1)
        mygame.play_game(games.random_player, games.random_player)
        end = time.time()
        print("")
        print("This round took", end-start, "seconds.")
    roundend = time.time()
    print("This matchup took", roundend-roundstart,"seconds total.")
    overall_winner(resultaggregate,"Random Player A", "Random Player B")

    print("")
    print("")
    print("")

    #rand v mincut
    resultaggregate = []
    print("#################################################")
    print("Matchup between a Random Player and a Minimax Cutoff Player")
    resultaggregate = []
    roundstart = time.time()
    for i in range(5):
        start = time.time()
        print(" ")
        print("Round number:", i+1)
        mygame.play_game(games.random_player, minmax_cutoff_player(depth,cutoff_test=None,eval_fn=my_eval_fn))
        end = time.time()
        print("This round took", end-start, "seconds.")
    roundend = time.time()
    print("This matchup took", roundend-roundstart,"seconds total.")
    overall_winner(resultaggregate,"Random Player", "Minimax Cutoff Player")

    print("")
    print("")
    print("")

    #mincut v abprune
    resultaggregate = []
    print("#################################################")
    print("Matchup between a Minimax Cutoff Player and an Alpha-Beta Cutoff Player")
    resultaggregate = []
    roundstart = time.time()
    for i in range(5):
        start = time.time()
        print(" ")
        print("Round number:", i+1)
        mygame.play_game(minmax_cutoff_player(depth,cutoff_test=None,eval_fn=my_eval_fn), alpha_beta_cutoff_player(depth,cutoff_test=None,eval_fn=my_eval_fn))
        end = time.time()
        print("This round took", end-start, "seconds.")
    roundend = time.time()
    print("This matchup took", roundend-roundstart,"seconds total.")
    overall_winner(resultaggregate,"Minimax Cutoff Player", "Alpha Beta Cutoff Player")


__main__()