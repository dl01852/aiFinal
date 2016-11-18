import copy
class State:

    def __init__(self, current_state, parent = None):
        self.parent = parent
        #self.goal_state_coords = goal_state_coords # coordinates of the goal state
        self.current = current_state # always a list of list
        self.current_coords = self.get_current_coords()


    def manhattan_distance(self, goal_state_coords):
       # current_coords = {int(val):(row,self.current[row].index(val)) for row,row_data in enumerate(self.current) for val in row_data}
       tv = 0
       for k,v in self.current_coords.items():
           a,b = v
           c,d = goal_state_coords[k]
           tv += abs(a-c) + abs(b-d)
       return tv

    def get_current_coords(self):
       return  {int(val): (row, self.current[row].index(val)) for row, row_data in enumerate(self.current) for
                          val in row_data}


    def get_all_children(self):
        zero = self.current_coords[0]
        zero_row, zero_col = zero
        states = []
        # blank spot is not on top row(middle or bottom) so we move up!
        if zero_row > 0:
            swapRow = zero_row - 1
            tempState = copy.copy(self.current) # a list of list of strings
            tempState[zero_row][zero_col], tempState[swapRow][zero_col] = tempState[swapRow][zero_col], tempState[zero_row][zero_col]
            s = State(tempState)
            states.append(s)
        ##  blank spot is not on the bottom row(middle or top) so we move down!
        if zero_row < 2:
            swapRow = zero_row + 1
            tempState = copy.copy(self.current)
            tempState[zero_row][zero_col], tempState[swapRow][zero_col] = tempState[swapRow][zero_col], tempState[zero_row][zero_col]
            s = State(tempState)
            states.append(s)

        ## handle left right now(using columns).

        # if you're in the 0th or 1st column, Move right!
        if 0 <= zero_col < 2:
            swapCol = zero_col + 1
            tempState = copy.copy(self.current)
            tempState[zero_row][zero_col], tempState[zero_row][swapCol] = tempState[zero_row][swapCol], tempState[zero_row][zero_col]
            s = State(tempState)
            states.append(s)

        # if your're in the 1st or 2nd column Move left!
        if  0 < zero_col <= 2:
            swapCol = zero_col - 1
            tempState = copy.copy(self.current)
            tempState[zero_row][zero_col], tempState[zero_row][swapCol] = tempState[zero_row][swapCol], tempState[zero_row][zero_col]
            s = State(tempState)
            states.append(s)


        return states

    # def __str__(self):
    #     for l in self.current:
    #         print(*l)
       # Not fast enough!
       # def manhattan_distance2(self):
       #     current_coords = {int(val): (row, self.current[row].index(val)) for row, row_data in enumerate(self.current) for
       #                       val in row_data}
       #     return sum([abs(v[0] - self.goal_state_coords[k][0]) + abs(v[1] - self.goal_state_coords[k][1]) for k, v in
       #                 current_coords.items()])


