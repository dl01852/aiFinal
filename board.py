import copy
from itertools import chain


class State:
    def __init__(self, current_state, parent=None):

        self.parent = parent
        self.flattened = current_state
        if parent is None:
            self.pathCost = 0
        else:
            self.pathCost = parent.pathCost + 1

    def manhattan_distance(self, goal_state_coords):
        tv2 = 0
        for index, val in enumerate(self.flattened):
            a,b = goal_state_coords[index]
            c,d = goal_state_coords[int(val)]
            tv2 += abs(a-c) + abs(b-d)
        return tv2

    def __hash__(self):
        return hash(tuple(self.flattened)) # switched it to tuple here because you can only hash immutable objects.

    def __eq__(self, other):
        if isinstance(other, State):
            return self.flattened == other.flattened

    def get_all_children(self):

        zero_index = self.flattened.index(0)
        states = set()

        # i can move down!
        if zero_index > 2:
            swap = zero_index - 3
            temp_state = self.flattened[:]
            temp_state[zero_index], temp_state[swap] = temp_state[swap], temp_state[zero_index]
            states.add(State(temp_state, self))

        # i can move up!
        if zero_index < 6:
            swap = zero_index + 3
            temp_state = self.flattened[:]
            temp_state[zero_index], temp_state[swap] = temp_state[swap], temp_state[zero_index]
            states.add(State(temp_state, self))

        if zero_index % 3 > 0:
            swap = zero_index - 1
            temp_state = self.flattened[:]
            temp_state[zero_index], temp_state[swap] = temp_state[swap], temp_state[zero_index]
            states.add(State(temp_state, self))

        # if your're in the 0th or 1st column Move left!
        if zero_index % 3 < 2:
            swap = zero_index + 1
            temp_state = self.flattened[:]
            temp_state[zero_index], temp_state[swap] = temp_state[swap], temp_state[zero_index]
            states.add(State(temp_state, self))

        return states