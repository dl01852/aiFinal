import time
from board import State
from copy import deepcopy
from queue import PriorityQueue
from itertools import chain

# start off by reading the file
File = [line.strip().replace('\t', ' ').split(' ') for line in open('test2.txt')]
start_state = list(chain(*File[0:3])) # flatten the lists of lists to optimize and avoid
goal_state = File[4:]
goal_flat = list(chain(*File[4:]))


coordinates = {int(val): (row, goal_state[row].index(val)) for row, data in enumerate(goal_state) for val in data}

#closedSet = set()


start = time.time()
def algorithm():
    node = State(start_state)
    frontier = PriorityQueue()
    frontier.put(((node.manhattan_distance(coordinates) + node.pathCost), 0, node))
    setFrontier = set()
    setFrontier.add(node)
    explored = set()

    priorityCounter = 1

    while frontier.not_empty:
        node = frontier.get()[2]
        if node.flattened == goal_flat:
            end = time.time()
            print("done!")
            print(end - start)
            return
        else:
            explored.add(node)
            children = node.get_all_children()
            for child in children:
                #flattenChild = sum(child.current)
                if child not in explored:
                    if child not in setFrontier:#and child not in frontier.queue:
                        frontier.put(((child.manhattan_distance(coordinates) + child.pathCost), priorityCounter, child))
                        setFrontier.add(child)
                        priorityCounter +=1
                # elif child in frontier.queue:
                #     print('implement functionality!')

## OTHER MEANS OF CHECKING EXPLORED AND FRONTIER
algorithm()






























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

