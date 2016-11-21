import time
from board import State
from queue import PriorityQueue
from itertools import chain
from priorityDict import priority_dict

# start off by reading the file
File = [line.strip().replace('\t', ' ').split(' ') for line in open('testFile.txt')]
start_state = list(chain(*File[0:3])) # flatten the lists of lists to optimize and avoid
goal_state = File[4:]
goal_flat = list(chain(*File[4:]))


coordinates = {int(val): (row, goal_state[row].index(val)) for row, data in enumerate(goal_state) for val in data}

#closedSet = set()


start = time.time()
def algorithm():
    node = State(start_state)
    frontier = PriorityQueue() # openSet!
    frontier.put(((node.manhattan_distance(coordinates) + node.pathCost), 0, node)) #frontier for priority only!(queue)
    setFrontier = set() # a Set of the frontier for checking if value is exist as checking queue is VERY VERY EXPENSIVE. set is constant time
    dictFrontier = {} # dictionary of the frontier to retrive values to compare path cost and do updates if necessary!
    setFrontier.add(node)
    dictFrontier[tuple(node.flattened)] = node
    explored = set() # closed Set!

    priorityCounter = 1

    while frontier.not_empty:
        node = frontier.get()[2]
        if node.flattened == goal_flat:
            end = time.time()
            allPaths = reconstruct_path(node)
            print_path(allPaths)
            print(end - start)
            return
        else:
            explored.add(node)
            children = node.get_all_children()
            for child in children:
                #flattenChild = sum(child.current)
                if child in explored:
                    continue
                if child not in setFrontier: #and child not in frontier.queue:
                    frontier.put(((child.manhattan_distance(coordinates) + child.pathCost), priorityCounter, child))
                    setFrontier.add(child)
                    dictFrontier[tuple(child.flattened)] = child
                    priorityCounter +=1
                elif child in setFrontier and child != node:
                    test = dictFrontier[tuple(child.flattened)]
                    if child.pathCost < test.pathCost: # updating!
                        priority_num = del_n_replace(test,frontier.queue)
                        # frontier.queue = [element for element in frontier.queue if test not in element]
                        frontier.put(((child.manhattan_distance(coordinates) + child.pathCost), priority_num, child))
                        # priorityCounter+=1
                        setFrontier.remove(test)
                        setFrontier.add(child)
                        dictFrontier[tuple(child.flattened)] = child
                        #print("IMPLEMENT THIS FUNCTIONALITY!!")



            # elif child in frontier.queue:
            #     print('implement functionality!')

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

def del_n_replace(deleter,listQue):
    for index, tup in enumerate(listQue):
        if tup[2] == deleter:
            retainPriorityNum = tup[1]
            del listQue[index]
            return retainPriorityNum
algorithm()

# def algorithms2():
#     node = State(start_state)
#
#     frontier = priority_dict()  # openSet!
#     priority_dict[node] = node.manhattan_distance() + node.pathCost
#     frontier.put(
#         ((node.manhattan_distance(coordinates) + node.pathCost), 0, node))  # frontier for priority only!(queue)
#     setFrontier = set()  # a Set of the frontier for checking if value is exist as checking queue is VERY VERY EXPENSIVE. set is constant time
#     dictFrontier = {}  # dictionary of the frontier to retrive values to compare path cost and do updates if necessary!
#     setFrontier.add(node)
#     dictFrontier[tuple(node.flattened)] = node
#     explored = set()  # closed Set!
#
#     priorityCounter = 1
#
#     while frontier.not_empty:
#         node = frontier.get()[2]
#         if node.flattened == goal_flat:
#             end = time.time()
#             allPaths = reconstruct_path(node)
#             print_path(allPaths)
#             print(end - start)
#             return
#         else:
#             explored.add(node)
#             children = node.get_all_children()
#             for child in children:
#                 # flattenChild = sum(child.current)
#                 if child in explored:
#                     continue
#                 if child not in setFrontier:  # and child not in frontier.queue:
#                     frontier.put(((child.manhattan_distance(coordinates) + child.pathCost), priorityCounter, child))
#                     setFrontier.add(child)
#                     dictFrontier[tuple(child.flattened)] = child
#                     priorityCounter += 1
#                 elif child in setFrontier and child != node:
#                     test = dictFrontier[tuple(child.flattened)]
#                     if child.pathCost < test.pathCost:
#                         print("IMPLEMENT THIS FUNCTIONALITY!!")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#











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

