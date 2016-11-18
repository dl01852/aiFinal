import time
from board import State
import pprint
# start off by reading the file
File = [line.strip().replace('\t', ' ').split(' ') for line in open('board_config.txt')]
current_state = File[0:3]
goal_state = File[4:]
# print(current_state)
# print(goal_state)


coordinates = {int(val): (row, goal_state[row].index(val)) for row, data in enumerate(goal_state) for val in data}


initial = State(current_state)
children = initial.get_all_children()
for child in children:
    print(child)




# print(s.manhattan_distance2())


# a,b = 2,1
# c,d = coordinates[3]
# mhd = abs(a-c) + abs(b-d)
# print(mhd)


## dictionary comp above is this code below.
# simply grabbing the position for each value in the goal state.
# coordinates = {}.fromkeys(range(9)) #
# for row,val in enumerate(goal_state): enumerate function turns val into a list for each row.
#     for v in val:
#         coordinates[int(v)] = (row, goal_state[row].index(v)) # store

