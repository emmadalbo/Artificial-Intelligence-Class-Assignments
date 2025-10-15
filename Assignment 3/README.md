# Assignment 3

## Libraries
"games.py" and "utils.py" are used from the AIMA code repository on Github: https://github.com/aimacode/aima-python
BLOBS.py also imports copy, itertools, random, time, namedtuple (from collections), nympy, and sys.


## Python version
This program runs on version 3.9.1.


## Usage
All problems will print automatically following the main function running. 

### Purpose:
This code "BLOBS" implements a game called BLOBS/Ataxx, which is similar to Othello. 
There are two players: one X, one O. The game is won by having more pieces at the end of the game. This can be achieved either when there are two passes in a row (pass= no move can be made), or when the board fills up.
There are two options for a player's turn: 1) Place a new piece in an empty slot next to another piece of the same color. 2) Move the player's own existing piece to a location that is within a 2-square radius of the original location (providing the new location is empty).
The main function will automatically run 3 matchups:
1) 5 rounds between Random Player A and Random Player B
2) 5 rounds between a Random Player and a Minimax Cutoff Player
3) 5 rounds between a Minimax Cutoff Player and an Alpha-Beta Cutoff Player.
These functions will run automatically on a 5x5 game board with a depth of 2 for the cutoff depths. Results will be printed.

### Game Class:
I implement a class "BLOBS", which formulates the problem of the game Blobs. This class intakes an h and a v, being the height and width of the game board. The Board is represented as a dictionary, containing keys which are occupied locations and values which are the corresponding piece of the player who placed it. The Game State is a named tuple, which includes the data of the utility of a board, the player to move from that state, and the empty slots
The game initializes as a board with "X" in the top left and bottom right, and "O" in the remaining corners. 
Actions returns a list of valid legal moves from each state.
Result returns the resulting GameState after intaking an action.
Terminal_test returns True if the state is the termination of the game (by full board or 2 passes).
Utility returns 1 if the state is a win for the player, -1 if it is a loss, 0 otherwise.
Compute_utility computes the utility of the board from the perspective of X.
Display prints out the board of the state it intakes.

To call to formulate outside of main():
    mygame = Blobs(h, v)

### Eval Function:
The function "my_eval_fn" intakes a state, and returns an evaluation that is the percentage of board pieces held by the relevant player.

### Alpha-Beta Function:
The function "alpha_beta_cutoff_player" takes depth, cutoff_test, and eval_fn as parameters. It then is used to play the Blobs game with the alpha_beta_cutoff_search algorithm from games.py.

### Minimax Cutoff Functions:
There are two relevant functions for this.
The function "minmax_cutoff_player" takes depth, cutoff_test, and eval_fn as parameters. It then is used to play the Blobs game with the minmax_cutoff_decision function.
The function "minmax_cutoff_decision" takes state, game, depth, cutoff_test, and eval_fn. It is not necessary to pass a cutoff_test, as there is an inherent cutoff test built into the function. 

### Overall Winner Function:
The overall_winner function works alongside __main__. It runs at the end of each matchup, printing a summary of the 5 rounds for the most recent matchup. It will print:
-the total time that the matchup took
-how many games each player won
-who won overall
-what percentage of games the winner won.

### __main__ Function:
The main function will run 3 matchups as described in the Purpose section above. It will record the time that each round took, display the final board, and calculate who won along with how many pieces each player placed. This function will also run the overall_winner function at the end of each matchup.

To call to play a game outside of main():
    firstplayer = algorithmname_player(depth,cutoff_test=None,eval_fn=my_eval_fn)
    secondplayer = algorithmname_player(depth,cutoff_test=None,eval_fn=my_eval_fn)
    mygame.play_game(firstplayer, secondplayer)
    
    #if player is random, remove parameters from the random player


### My results/ Analysis of Winners:
Of course, due to the randomness of random players, there will be different results on each run for the first and second matchup. The results I received will be at the bottom of this README.

We can see that in the matchup between 2 random players, there is no consistent winner. B ended up winning more rounds this time, but previous iterations had A winning more games. This is as expected for players who simply select any legal move without reason, planning, or calculation.

In the matchup between Minimax Cutoff Player and a random player, the Minimax Cutoff Player won decisively, taking about 2.09 seconds over the entire matchup to win all 5 rounds. This is as expected, since minimax searches the entire tree to our cutoff point and selects the path that maximizes its ability to win (even if the opponent had been playing perfectly, the player selected the path to minimize its chance of loss and maximize its chance of a win).

In the matchup between Minimax Cutoff Player and Alpha Beta Cutoff Player, the Minimax player won. Theoretically, both players should play equally well, since both are working to maximize winning potential for themselves. The only difference is only that Alpha Beta player prunes unnecessary branches in the search tree, working more quickly while achieving identical results to if it was a Minmax player. 
However, the Minimax Cutoff Player won all 5 rounds. This is because it was player X, and got to place a piece first, which is an advantage in this game. When I switch the order of this matchup so that Alpha Beta Cutoff Player goes first, it wins, also with 22 pieces placed compared to the opponent's 3. 
This matchup took about 4.83 seconds total, which is longer than the previous round since there are two competent players "thinking ahead" to make a rational decision for their own benefit.



### My achieved printout:

Initial board for all rounds:
X . . . O 
. . . . . 
. . . . . 
. . . . . 
O . . . X 

#################################################
Matchup between 2 Random Players
 
Round number: 1
X wins! Winning board:
O X X O X 
X X X O X 
O O X O O 
X X O X O 
O O O X X 
X placed 13 pieces.
O placed 12 pieces.

This round took 0.017329931259155273 seconds.
 
Round number: 2
O wins! Winning board:
X X X X O 
X O X O X 
O X X X O 
O O O O O 
O O X O O 
X placed 11 pieces.
O placed 14 pieces.

This round took 0.009458780288696289 seconds.
 
Round number: 3
O wins! Winning board:
X X X O O 
X O X O X 
X X O X O 
O O X X O 
X O O O O 
X placed 12 pieces.
O placed 13 pieces.

This round took 0.011670827865600586 seconds.
 
Round number: 4
O wins! Winning board:
X O O X O 
O O X X X 
O O X O O 
O O X O X 
O O X X X 
X placed 11 pieces.
O placed 14 pieces.

This round took 0.010951042175292969 seconds.
 
Round number: 5
O wins! Winning board:
X O X X O 
X O O O O 
X X X X O 
O O X X O 
O X X O O 
X placed 12 pieces.
O placed 13 pieces.

This round took 0.017446279525756836 seconds.
This matchup took 0.06691694259643555 seconds total.
In the 5 games between Random Player A and Random Player B :
Random Player A (using piece X) won 1 games, and Random Player B (using piece O) won 4  games.
Random Player B won overall!
It won 4 out of 5 rounds. That is 80.0  percent!



#################################################
Matchup between a Random Player and a Minimax Cutoff Player
 
Round number: 1
O wins! Winning board:
X O O O X 
O X O O O 
O O O O O 
X O X X O 
X O O X O 
X placed 8 pieces.
O placed 17 pieces.
This round took 0.44292593002319336 seconds.
 
Round number: 2
O wins! Winning board:
O O O O X 
O X O O O 
O X O O O 
O X O X X 
O O X O O 
X placed 7 pieces.
O placed 18 pieces.
This round took 0.4038116931915283 seconds.
 
Round number: 3
O wins! Winning board:
X X O O X 
O O O O O 
O O O O O 
X X X X O 
O O O X O 
X placed 8 pieces.
O placed 17 pieces.
This round took 0.34900498390197754 seconds.
 
Round number: 4
O wins! Winning board:
O O O O X 
O O O O O 
O O O O O 
O X X X O 
O O O O X 
X placed 5 pieces.
O placed 20 pieces.
This round took 0.4901580810546875 seconds.
 
Round number: 5
O wins! Winning board:
O O O X O 
O X O O O 
X O O O O 
O O O O O 
X X O X O 
X placed 6 pieces.
O placed 19 pieces.
This round took 0.4095191955566406 seconds.
This matchup took 2.095444917678833 seconds total.
In the 5 games between Random Player and Minimax Cutoff Player :
Random Player (using piece X) won 0 games, and Minimax Cutoff Player (using piece O) won 5  games.
Minimax Cutoff Player won overall!
It won 5 out of 5 rounds. That is 100.0  percent!



#################################################
Matchup between a Minimax Cutoff Player and an Alpha-Beta Cutoff Player
 
Round number: 1
X wins! Winning board:
X X X X X 
X X X X X 
X O X X X 
X X X X O 
O X X X X 
X placed 22 pieces.
O placed 3 pieces.
This round took 0.9626691341400146 seconds.
 
Round number: 2
X wins! Winning board:
X X X X X 
X X X X X 
X O X X X 
X X X X O 
O X X X X 
X placed 22 pieces.
O placed 3 pieces.
This round took 0.9662590026855469 seconds.
 
Round number: 3
X wins! Winning board:
X X X X X 
X X X X X 
X O X X X 
X X X X O 
O X X X X 
X placed 22 pieces.
O placed 3 pieces.
This round took 0.9636120796203613 seconds.
 
Round number: 4
X wins! Winning board:
X X X X X 
X X X X X 
X O X X X 
X X X X O 
O X X X X 
X placed 22 pieces.
O placed 3 pieces.
This round took 0.9731729030609131 seconds.
 
Round number: 5
X wins! Winning board:
X X X X X 
X X X X X 
X O X X X 
X X X X O 
O X X X X 
X placed 22 pieces.
O placed 3 pieces.
This round took 0.9666569232940674 seconds.
This matchup took 4.832398176193237 seconds total.
In the 5 games between Minimax Cutoff Player and Alpha Beta Cutoff Player :
Minimax Cutoff Player (using piece X) won 5 games, and Alpha Beta Cutoff Player (using piece O) won 0  games.
Minimax Cutoff Player won overall!
It won 5 out of 5 rounds. That is 100.0  percent!