import copy
from itertools import chain


class State:
    def __init__(self, current_state, parent=None):
        # self.current = current_state  # list of list is only used to generate MHD!
        # self.current_coords = self.get_current_coords()
        # self.flattened = self.flatten_list() # a flattened version of current for optimization
        if parent is None:
            self.parent = None
            self.flattened = current_state
            self.pathCost = 0
            #self.path = copy.deepcopy(self.current)
            #self.current = current_state

           # self.current_coords = self.get_current_coords()
           # self.path = self.flattened[:]

        else:
            self.parent = parent
            self.flattened = current_state
            self.pathCost = parent.pathCost + 1
            #self.path = self.parent.path[:]

            #self.current = self.unflatten_list()
          #  self.current_coords = self.get_current_coords()
            #  self.path.append(self.flattened)



    def manhattan_distance(self, goal_state_coords):
        # current_coords = {int(val):(row,self.current[row].index(val)) for row,row_data in enumerate(self.current) for val in row_data}

        tv2 = 0
        for val in self.flattened:
            a,b = goal_state_coords[self.flattened.index(val)]
            c,d = goal_state_coords[int(val)]
            tv2 += abs(a-c) + abs(b-d)
        return tv2

        # for k, v in self.current_coords.items():
        #     a, b = v
        #     c, d = goal_state_coords[k]
        #     tv += abs(a - c) + abs(b - d)
        # return tv

    # def flatten_list(self):
    #     return list(chain(*self.current))

    # def unflatten_list(self):
    #
    #     return [self.flattened[x:x+3] for x in range(0, len(self.flattened), 3)]

    def __hash__(self):
        return hash(tuple(self.flattened)) # switched it to tuple here because you can only has unmutable objects.

    def __eq__(self, other):
        if isinstance(other, State):
            return self.flattened == other.flattened

    # def get_current_coords(self):
    #     return {int(val): (row, self.current[row].index(val)) for row, row_data in enumerate(self.current) for
    #             val in row_data}

    def get_all_children(self):

        zero_update = self.flattened.index('0')

        states = []
        # blank spot is not on top row(middle or bottom) so we move up!

        if zero_update > 2:
            swap = zero_update - 3
            temp_state = self.flattened[:]
            temp_state[zero_update], temp_state[swap] = temp_state[swap], temp_state[zero_update]
            s = State(temp_state, self)
            states.append(s)
        # if zero_row > 0:
        #     swap_row = zero_row - 1
        #     temp_state = copy.deepcopy(self.current)  # a list of list of strings
        #     temp_state[zero_row][zero_col], temp_state[swap_row][zero_col] = temp_state[swap_row][zero_col], \
        #                                                                      temp_state[zero_row][zero_col]

        # blank spot is not on the bottom row(middle or top) so we move down!

        if zero_update < 6:
            swap = zero_update + 3
            temp_state = self.flattened[:]
            temp_state[zero_update], temp_state[swap] = temp_state[swap], temp_state[zero_update]
            s = State(temp_state, self)
            states.append(s)
        # if zero_row < 2:
        #     swap_row = zero_row + 1
        #     temp_state = copy.deepcopy(self.current)
        #     temp_state[zero_row][zero_col], temp_state[swap_row][zero_col] = temp_state[swap_row][zero_col], \
        #                                                                      temp_state[zero_row][zero_col]

        # handle left right now(using columns).

        # if you're in the 1st or 2nd column, Move Left!
        if zero_update % 3 > 0:
            swap = zero_update - 1
            temp_state = self.flattened[:]
            temp_state[zero_update], temp_state[swap] = temp_state[swap], temp_state[zero_update]
            s = State(temp_state, self)
            states.append(s)

        # if 0 <= zero_col < 2:
        #     swap_col = zero_col + 1
        #     temp_state = copy.deepcopy(self.current)
        #     temp_state[zero_row][zero_col], temp_state[zero_row][swap_col] = temp_state[zero_row][swap_col], \
        #                                                                      temp_state[zero_row][zero_col]

        # if your're in the 0th or 1st column Move left!
        if zero_update % 3 < 2:
            swap = zero_update + 1
            temp_state = self.flattened[:]
            temp_state[zero_update], temp_state[swap] = temp_state[swap], temp_state[zero_update]
            s = State(temp_state, self)
            states.append(s)
        # if 0 < zero_col <= 2:
        #     swap_col = zero_col - 1
        #     temp_state = copy.deepcopy(self.current)
        #     temp_state[zero_row][zero_col], temp_state[zero_row][swap_col] = temp_state[zero_row][swap_col], \
        #                                                                      temp_state[zero_row][zero_col]

        return states

    # def print(self):
    #     for l in self.path:
    #         print(*l)
    #     print()

        # Not fast enough!
        # def manhattan_distance2(self):
        #     current_coords = {int(val): (row, self.current[row].index(val)) for row, row_data in enumerate(self.current) for
        #                       val in row_data}
        #     return sum([abs(v[0] - self.goal_state_coords[k][0]) + abs(v[1] - self.goal_state_coords[k][1]) for k, v in
        #                 current_coords.items()])
