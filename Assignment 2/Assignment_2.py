import search


###Question 1###
class WaterJug43(search.Problem):
    '''Implements Waterjug solution only for the situation of
    first jug being volume 4, second jug being volume 3.'''
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        possible_actions = ['jug4tojug3','jug3tojug4','filljug4','filljug3','emptyjug4','emptyjug3']
        if state[0] == 4:#jug4 is full
            possible_actions.remove('filljug4')
            possible_actions.remove('jug3tojug4')
        if state[1] == 3:#jug3 is full
            possible_actions.remove('filljug3')
            possible_actions.remove('jug4tojug3')

        if state[0] == 0:#jug4 is empty
            possible_actions.remove('emptyjug4')
            if 'jug4tojug3' in possible_actions:
                possible_actions.remove('jug4tojug3')
        if state[1] == 0:#jug4 is empty
            possible_actions.remove('emptyjug3')
            if 'jug3tojug4' in possible_actions:
                possible_actions.remove('jug3tojug4')
        return possible_actions

    def result(self, state, action):
        new_state = [state[0],state[1]]
        if action ==  "jug4tojug3":#will only happen if jug3 isn't full, jug4 isn't empty
            space = 3-new_state[1]
            if space > new_state[0]:#can add all jug4 without filling jug3
                new_state[1] += new_state[0]
                new_state[0]=0
            else:
                new_state[1] = 3
                new_state[0] -= space
        elif action == "jug3tojug4":#will only happen if jug4 isn't full, jug3 isn't empty
            space = 4-new_state[1]
            if space > new_state[1]:#can add all jug3 without filling jug4
                new_state[0] += new_state[1]
                new_state[1]=0
            else:
                new_state[0] = 4
                new_state[1] -= space
        elif action == "filljug4":
            new_state[0] = 4
        elif action == "filljug3":
            new_state[1] = 3
        elif action == "emptyjug4":
            new_state[0] = 0
        elif action == "emptyjug3":
            new_state[1] = 0
        return tuple(new_state)

    def goal_test(self, state):
        if state[0] == 2:
            print("Goal reached. Solution path in output file 'solution_waterjug.txt'")
            return True

def store_solution_Q1(initial, goal):
    '''Implements WaterJug problem, searching with breadth first search,
    and puts solutions in an output file.'''
    myprob = WaterJug43(initial,goal)
    solution = search.breadth_first_graph_search(myprob)
    
    solutionfile = open('solution_waterjug.txt','w')
    solutionfile.write("Path from "+str(initial)+" to "+str(goal)+" \n")
    solutionfile.write("Cost is "+str(solution.path_cost)+" \n")
    path = solution.path()
    for node in path:
        if not node.action:
            hold = "init_state: "+str(node.state)+ "\n"
            solutionfile.write(hold)
        else:
            hold = node.action+": "+str(node.state)+ "\n"
            solutionfile.write(hold)
    solutionfile.close()





###Question 2###
class n_max_swap(search.Problem):
    """Searches to find the max_swap heuristic """

    def __init__(self, initial, goal=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
        """ Define goal state and initialize a problem """
        super().__init__(initial, goal)

    def find_blank_square(self, state):
        """Return the index of the blank square in a given state"""
        return state.index(0)

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only 9 possible actions
        in any given state of the environment. Actions are swaps from index location
        to blank location"""

        possible_actions = ['0toblank','1toblank','2toblank','3toblank','4toblank','5toblank','6toblank','7toblank','8toblank']
        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        # blank_ind is the index of the blank square
        blank_ind = self.find_blank_square(state)
        new_state = list(state)
        oth_ind = int(action[0]) #index of the item to swap with blank
        new_state[blank_ind] = new_state[oth_ind]
        new_state[oth_ind] = 0
        return tuple(new_state)
    
    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is 
        h(n) = number of misplaced tiles """
        return sum(s != g for (s, g) in zip(node.state, self.goal))

class AltEightPuzzle(search.Problem):
    """ The problem of sliding tiles numbered from 1 to 8 on a 3x3 board, where one of the
    squares is a blank. A state is represented as a tuple of length 9, where  element at
    index i represents the tile number at index i (0 if it's an empty square) """

    def __init__(self, initial, goal=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
        """ Define goal state and initialize a problem """
        super().__init__(initial, goal)
        
    def __repr__(self):
        return "initial is"+str(self.initial)+" and goal is "+str(self.goal)+""

    def find_blank_square(self, state):
        """Return the index of the blank square in a given state"""
        return state.index(0)

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        index_blank_square = self.find_blank_square(state)

        if index_blank_square % 3 == 0:
            possible_actions.remove('LEFT')
        if index_blank_square < 3:
            possible_actions.remove('UP')
        if index_blank_square % 3 == 2:
            possible_actions.remove('RIGHT')
        if index_blank_square > 5:
            possible_actions.remove('DOWN')
        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """
        # blank is the index of the blank square
        blank = self.find_blank_square(state)
        new_state = list(state)
        delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        return tuple(new_state)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """
        return state == self.goal

    def check_solvability(self, state):
        """ Checks if the given state is solvable """
        inversion = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if (state[i] > state[j]) and state[i] != 0 and state[j] != 0:
                    inversion += 1
        return inversion % 2 == 0

    def misplaced_h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is 
        h(n) = number of misplaced tiles """
        return sum(s != g for (s, g) in zip(node.state, self.goal))
    
    def convert_to_grid_coord(self,index):
        '''takes index, returns as tuple x,y'''
        #x value
        mod = (index+1)%3
        if mod == 0:
            x = 3
        elif mod == 2:
            x = 2
        else:
            x=1
        #y value
        if index < 3:
            y=1
        elif index > 5:
            y=3
        else:
            y=2
        return (x,y)
    def manhattan_h(self, node):
        """ Return the heuristic value for a given state as 
        a total of manhattan distances."""
        i=0
        total=0
        for eachtile in node.state:
            if eachtile != 0:#don't calc. manhattan dist. for blank
                x1, y1 = self.convert_to_grid_coord(i)
                #find index of eachtile in goal
                ind = self.goal.index(eachtile)
                x2, y2 = self.convert_to_grid_coord(ind)
                adding = abs(x2 - x1) + abs(y2 - y1)
                total+=adding
                i+=1
        return total
    
    def n_max_swap_h(self,node):
        initial = node.state #uses node's state as initial for swap
        goal = self.goal
        thisprob = n_max_swap(initial,goal)
        solution = search.astar_search(thisprob,thisprob.h,False)
        solcost = solution.path_cost
        return solcost
    
    def followedbypropersuccessor(self,index,state,goal):
        if index <2:
                propersuccessor = goal[index+1]#look one right for who successor should be
                realsuccessor = state[index+1] #find the real successor
        elif index > 6:
                propersuccessor = goal[index-1]#look one left for who successor should be
                realsuccessor = state[index-1] #find the real successor
        elif index%3 == 0: #its 3 or 6
                propersuccessor = goal[index-3]#look one row up for who successor should be
                realsuccessor = state[index-3] #find the real successor
        else:
                propersuccessor = goal[index+3]#look one row down for who successor should be
                realsuccessor = state[index+3] #find the real successor

        if propersuccessor == realsuccessor:
                return True
        else:
                return False
    def nilssons_distance_h(self,node):
        #find s
        state = node.state
        goal = self.goal
        i=0
        s=0
        while i<len(state)-1:
            if i!=4: #it's not the central square
                if self.followedbypropersuccessor(i,state,goal):
                    s+=2
                else:
                    s+=0
            i+=1
        
        #find m
        m = self.manhattan_h(node)
        return m+s

def comparison_Q2(initial,goal): 
    '''Implements Eight Puzzle problem, searching with various heuristics as A# search:
    misplaced tiles, manhattan distance, n-max-swap, and nilsson's distance (inadmissible),
    and puts solutions in an output file.'''
    solutionfile = open('solutions_8P.txt','w')
    solutionfile.write("Paths from "+str(initial)+" to "+str(goal)+" \n")
    init = AltEightPuzzle(initial,goal)
    
    #misplaced tiles:
    print("Using misplaced tiles heuristic:")
    solutionfile.write("\n")
    misplacedsol = search.astar_search(init,init.misplaced_h,True)
    solutionfile.write("Using misplaced_h: \n")
    for node in misplacedsol.path():
        if not node.action:
            solutionfile.write("init_state: "+ str(node.state)+"\n")
        else:
            solutionfile.write(""+str(node.action)+" -> "+ str(node.state)+"\n")
    solutionfile.write("Path cost was: "+str(misplacedsol.path_cost)+"\n")
    print("")
    #manhattan:
    print("Using manhattan distance heuristic:")
    solutionfile.write("\n")
    manhattansol = search.astar_search(init,init.manhattan_h,True)
    solutionfile.write("Using manhattan_h: \n")
    for node in manhattansol.path():
        if not node.action:
            solutionfile.write("init_state: "+ str(node.state)+"\n")
        else:
            solutionfile.write(""+str(node.action)+" -> "+ str(node.state)+"\n")
    solutionfile.write("Path cost was: "+str(manhattansol.path_cost)+"\n")
    print("")
    #n_max_swap:
    print("Using n_max_swap heuristic:")
    solutionfile.write("\n")
    n_max_swapsol = search.astar_search(init,init.n_max_swap_h,True)
    solutionfile.write("Using n_max_swap: \n")
    for node in n_max_swapsol.path():
        if not node.action:
            solutionfile.write("init_state: "+ str(node.state)+"\n")
        else:
            solutionfile.write(""+str(node.action)+" -> "+ str(node.state)+"\n")
    solutionfile.write("Path cost was: "+str(n_max_swapsol.path_cost)+"\n")
    print("")
    #Nilsson's distance:
    print("Using nilsson's distance heuristic:")
    solutionfile.write("\n")
    nilssons_sol = search.astar_search(init,init.nilssons_distance_h,True)
    solutionfile.write("Using nilssons_distance_h: \n")
    for node in nilssons_sol.path():
        if not node.action:
            solutionfile.write("init_state: "+ str(node.state)+"\n")
        else:
            solutionfile.write(""+str(node.action)+" -> "+ str(node.state)+"\n")
    solutionfile.write("Path cost was: "+str(nilssons_sol.path_cost))
    solutionfile.close()
    
    print("Solutions in output file 'solutions_8P.txt'")








###Question 3###
class dating_game(search.Problem):
    '''Implements Dating Game solution. M has a value of 1, F has a value of 2, blank is 0.
    Initiate with initial state and goal state, both as tuples of length 7, comprised entirely
    of numeric values'''
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def find_blank_square(self, state):
        """Return the index of the blank square in a given state"""
        return state.index(0)
    
    def actions(self, state):
        '''all actions are based on moving the blank. For example, 1left moves the blank 
        1 spot left. This is identical to the person left of the blank moving right. Similarly, 
        3left is identical to a person jumping over 2 people to reach the blank seat.'''
        possible_actions = ['1left','1right','2left','2right','3left','3right']
        blank_ind = self.find_blank_square(state)
        
        if blank_ind < 3:#ind is 2,1,0
            possible_actions.remove('3left')
            if blank_ind < 2:#ind is 1,0
                possible_actions.remove('2left')
                if blank_ind <1:#ind is 0
                    possible_actions.remove('1left')
                    
        if blank_ind > 3:#ind is 4,5,6
            possible_actions.remove('3right')
            if blank_ind > 4:#ind is 5,6
                possible_actions.remove('2right')
                if blank_ind > 5:#ind is 6
                    possible_actions.remove('1right')
        return possible_actions

    def result(self, state, action):
        new_state = list(state)
        blank_ind = self.find_blank_square(state)
        
        move_dist = int(action[0])#find how far the first character says to move
        if "left" in action:
            new_ind = blank_ind - move_dist#subtracting to move left
        elif "right" in action:
            new_ind = blank_ind + move_dist#adding to move right
        else:
            print("CRITICAL ERROR WITH LEFT/RIGHT")
        new_state[blank_ind] = new_state[new_ind]
        new_state[new_ind]=0
        return tuple(new_state)

    def goal_test(self, state):
        if state == self.goal:
            return True

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2. If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        if "3" in action:
            return c + 2
        else:
            return c + 1

    def any_swap_h(self, node):
        """ Return the heuristic value for a given state. Assuming you can swap any locations, considers how many
        swaps must be made for each incorrect gendered chair. In other words, does nothing if a chair is M
        and should be M, but if chair is F and should be M, swaps with next incorrect placed M. If the next incorrect placed
        item is over 2 spots away, cost will increase by 2 instead of one to mimic the real game's rules. 
        This heuristic is admissible, since it will always underestimate how long to reach the goal state in comparison
        to the more limited game where only certain spots (instead of all spots) can move into the blank (instead of anywhere)
        and it is relevant since it is performing a simplified/relaxed version of the game."""
        state = list(node.state)
        goal = list(self.goal)
        c=0
        i=0
        while i<len(node.state):
            shouldbe = goal[i]
            if state[i] == 0 or state[i] == shouldbe:#do nothing if its 0 or if its m/f in the right spot
                i+=1
                continue
            elif state[i] != shouldbe:
                # what it should be = shouldbe
                k=0
                while k < len(state):#iterates through state to find a shouldbe in the wrong place
                    if state[k] == shouldbe: #if its the shouldbe
                        if state[k]!=goal[k]:#the shouldbe item is also in the wrong place
                            #switch state[i] and state[k]
                            hold = state[i]
                            state[i] = state[k]
                            state[k] = hold
                            #find cost
                            if abs(i-k) > 2:#moved more than 2 slots
                                c+=2
                            else:
                                c+=1
                            break# breaks the while loop, go to i+=1
                    k+=1
            i+=1#check next item in state
        return c

def num_to_let(num_state):
    '''Converts tuple of numbers to tuple of corresponding letters for easy viewing.'''
    let_state = list(num_state)
    i=0
    while i<len(let_state):
        if let_state[i] == 1:
            let_state[i] = "M"
        elif let_state[i] == 2:
            let_state[i] = "F"
        else: #its a 0
            let_state[i] = "_"
        i+=1
    return tuple(let_state)

def comparison_Q3(initial,goal): 
    '''Implements Dating Game problem, searching with A* and depth-limited searches,
    and puts solutions in an output file along with my analysis.'''
    solutionfile = open('solutions_dating.txt','w')
    solutionfile.write("Paths from "+str(initial)+" to "+str(goal)+" \n")
    init = dating_game(initial,goal)
    
    solutionfile.write("A* with any_swap heuristic took a path cost of only 6 to reach the result.\n")
    solutionfile.write("Depth limited search with a limit of 50 took a path cost of 51 to reach the result, which.\n")
    solutionfile.write("is much higher than A*. This is because the search heads in a downward direction first, and .\n")
    solutionfile.write("doesn't necessarily find the optimal solution. In comparison, A* uses a heuristic to ensure.\n")
    solutionfile.write("it is looking in a preferable direction first, which results in an optimal solution.\n")
    solutionfile.write(" \n")
    solutionfile.write("However, if you reduce the limit in depth limited search, it only is permitted to  \n")
    solutionfile.write("search shallower to find the solution. As a result, the path cost is lower. \n")
    solutionfile.write("As you can see below, implementing a limit of 10 results in a path cost of 11, much lower \n")
    solutionfile.write("than was reached by a limit of 50.\n")
    solutionfile.write(" \n")
    solutionfile.write("In sum, A* found an optimal solution, while depth limited search did not. \n")
    solutionfile.write("Depth limited search is not optimal if the depth is higher than the best solution.\n")
    
    #a* heuristic:
    solutionfile.write("\n")
    astar_sol = search.astar_search(init,init.any_swap_h,True)
    solutionfile.write("Using A* with any_swap heuristic: \n")
    for node in astar_sol.path():
        let_state = num_to_let(node.state)#convert to letter form for nicer viewing
        if not node.action:
            solutionfile.write("init_state: "+ str(let_state)+"\n")
        else:
            solutionfile.write(""+str(node.action)+" -> "+ str(let_state)+"\n")
    solutionfile.write("Path cost was: "+str(astar_sol.path_cost)+"\n")

    #depth-limited, limit 50:
    solutionfile.write("\n")
    depthlim_sol = search.depth_limited_search(init,50)
    solutionfile.write("Using depth_limited_search, limit 50: \n")
    for node in depthlim_sol.path():
        let_state = num_to_let(node.state)#convert to letter form for nicer viewing
        if not node.action:
            solutionfile.write("init_state: "+ str(let_state)+"\n")
        else:
            solutionfile.write(""+str(node.action)+" -> "+ str(let_state)+"\n")
    solutionfile.write("Path cost was: "+str(depthlim_sol.path_cost)+"\n")

   #depth-limited, limit 6:
    solutionfile.write("\n")
    depthlim_sol = search.depth_limited_search(init,10)
    solutionfile.write("Using depth_limited_search, limit 10: \n")
    for node in depthlim_sol.path():
        let_state = num_to_let(node.state)#convert to letter form for nicer viewing
        if not node.action:
            solutionfile.write("init_state: "+ str(let_state)+"\n")
        else:
            solutionfile.write(""+str(node.action)+" -> "+ str(let_state)+"\n")
    solutionfile.write("Path cost was: "+str(depthlim_sol.path_cost)+"\n") 
    print("Solutions in output file 'solutions_dating.txt'")





###Question 4###
def depth_limited_search_for_IDA(problem, limit=50):#only enters once for each depth (limit = depth)
    '''Implementation of Depth-limited search problem, adjusted for use with IDA* search'''

    def recursive_dls_for_IDA(node, problem, limit):
        print(node.action, "->", node.state)
        
        if problem.goal_test(node.state):
            return node
        elif limit == 0:
            return 0
        else:
            cutoff_occurred = False
            for child in node.expand(problem):
                result = recursive_dls_for_IDA(child, problem, limit - 1)
                if result == 0:
                    cutoff_occurred = True
                elif result is not None:
                    return result
            return 0 if cutoff_occurred else None
    return recursive_dls_for_IDA(search.Node(problem.initial), problem, limit)

def iterative_deepening_astar_search(problem):
    '''Implementation of IDA* search, where f is used as the initial depth, and subsequent iterations
    use the depth = the lowest f cost of the expanded nodes of the previous iteration.'''
    x1,y1 = problem.initial
    x2,y2 = problem.goal
    h =  abs(x2 - x1) + abs(y2 - y1)
    g = 0
    f = g+h
    depth = f #initial depth is f, essentially manhattan distance to goal
    global f_list
    f_list = []
    while depth < search.sys.maxsize:
        print("Depth = "+str(depth)+":")
        result = depth_limited_search_for_IDA(problem, depth)
        newlow = depth
        for each in f_list:
            if each<newlow:
                newlow = f_list
        depth = newlow
        
        if result != 0:
            return result
        f_list.clear()#clear f_list, resetting for next iterative depth

class GridWorld(search.Problem):
    """ The problem of an agent searching for a goal on a 3x3 board, where all other
    squares are blank. A state is represented as a tuple of length 2, (y, x), representing 
    the agent coordinates. The goal is also a tuple of length 2, (y, x), representing the
    goal coordinates."""

    def __init__(self, initial, goal=(3,2)):
        """ Define goal state and initialize a problem """
        super().__init__(initial, goal)
        
    def __repr__(self):
        return "initial is"+str(self.initial)+" and goal is "+str(self.goal)+""

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """
        possible_actions = ['move_up', 'move_down', 'move_left', 'move_right']
        if state[0] == 1:
            possible_actions.remove('move_down')
        if state[0] == 3:
            possible_actions.remove('move_up')
        if state[1] == 1:
            possible_actions.remove('move_left')
        if state[1] == 3:
            possible_actions.remove('move_right')
        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """
        # blank is the index of the blank square
        new_coords = list(state) #agent coords
        if action == "move_left": 
            new_coords[1] -= 1
        elif action == "move_right":
            new_coords[1] += 1
        elif action == "move_up":
            new_coords[0] += 1
        elif action == "move_down":
            new_coords[0] -= 1
        return tuple(new_coords)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """
        return state == self.goal

    def manhattan_h(self, node):
        """ Return the heuristic value from agent to goal."""
        y1,x1 = node.state
        y2,x2 = self.goal
        return abs(x2 - x1) + abs(y2 - y1)
    
    def check_f(self, node):
        g = node.path_cost
        h = self.manhattan_h(node)
        return g+h

















def main():
    # Example invocations of the functions:
    #Question1: initial=(0,0), goal=(2,0)
    print("Question 1:")
    store_solution_Q1((0,0), (2,0))
    
    print(" ")
    print(" ")
    print(" ")

    #Question2: initial=(1,2,3,4,5,0,6,7,8), goal=(1,2,3,4,5,6,7,8,0)
    print("Question 2:")
    comparison_Q2((1,2,3,4,5,0,6,7,8),(1,2,3,4,5,6,7,8,0))

    print(" ")
    print(" ")
    print(" ")

    #Question3: initial=(1,1,1,0,2,2,2), goal=(1,2,1,2,1,2,0)
    print("Question 3:")
    comparison_Q3((1,1,1,0,2,2,2), (1,2,1,2,1,2,0))

    print(" ")
    print(" ")
    print(" ")

    #Question4: initial=(1,1), goal=(3,2)
    print("Question 4:")
    prob4 = GridWorld((1,1),(3,2))
    result = iterative_deepening_astar_search(prob4)
    print("Path cost was:", result.path_cost)

main()