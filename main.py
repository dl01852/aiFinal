import time
from board import State
from queue import PriorityQueue
from itertools import chain



# start off by reading the file
File = [line.strip().replace('\t', ' ').split(' ') for line in open('test2.txt')]
start_state = [int(x) for x in chain(*File[0:3])] ##list(chain(*File[0:3])) # flatten the lists of lists to optimize and avoid
goal_state = File[4:]
goal_flat = [int(x) for x in chain(*File[4:])] #list(chain(*File[4:]))


coordinates = {int(val): (row, goal_state[row].index(val)) for row, data in enumerate(goal_state) for val in data}




def algorithm():
    start = time.time()
    node = State(start_state)
    unexplored_queue = PriorityQueue() # openSet!
    unexplored_queue.put(((node.manhattan_distance(coordinates) + node.pathCost), 0, node)) #frontier for priority only!(queue)
    explored = set() # closed Set!

    priorityCounter = 1

    while unexplored_queue.not_empty:
        node = unexplored_queue.get()[2]
        if node.flattened == goal_flat:
            end = time.time()
            allPaths = reconstruct_path(node)
            print_path(allPaths)
            print(end - start)
            return
        else:
            explored.add(node)
            children = node.get_all_children()
            #for child in children:
            for child in children - explored:
                unexplored_queue.put(((child.manhattan_distance(coordinates) + child.pathCost), priorityCounter, child))
                priorityCounter += 1



## OTHER MEANS OF CHECKING EXPLORED AND FRONTIER
def reconstruct_path(node):
    end = node
    totalPath = {}
    while end != None:
        totalPath[end.pathCost] = end.flattened
        end = end.parent
    return totalPath

def print_path(allPaths): # pass in a dictionary
    for key, value in allPaths.items():
        print("Move %s" % key)
        print(value[0:3],value[3:6],value[6:],sep='\n')
    print("Optimal Moves: %s" % (len(allPaths) -1))


algorithm()
