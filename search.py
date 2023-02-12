# ENUMS
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

class Node:
    def __init__(self, row, col, moveToPrevNode=None, prevNode=None, g=0, h=None, f=None, visited = None):
        self.row = row
        self.col = col
        self.moveToPrevNode= moveToPrevNode
        self.prevNode = prevNode
        self.g = g
        self.h = h
        self.f = f
        self.visited = visited
        # Each node should have a visited 2d array? 


def BFS(puzzle):
    final_solution = []
    q = []

    for r in range(3):
        for c in range(3):
            if puzzle[r][c].strip() == "0":
                startingNode = Node(r, c, visited=[[0,0,0],[0,0,0],[0,0,0]])
                q.append(startingNode)
    
    while not len(q) == 0:
        currentNode = q.pop(0)
        currentNode.visited[currentNode.row][currentNode.col] = 1
        print("Current Node: [" + str(currentNode.row) + "," + str(currentNode.col) + "]")

        if currentNode.row == 2 and currentNode.col == 2:
            final_solution.append(currentNode)
            break
        else:
            next_moves = next_Move(currentNode)

            for move in next_moves:
                print("Can move to [" + str(move.row) + "," + str(move.col) + "]")
                q.append(move)

    currentNode = final_solution.pop(0)

    while(currentNode.prevNode != None):
        final_solution.insert(0, currentNode.moveToPrevNode)
        currentNode = currentNode.prevNode

    return final_solution


# BFS/DFS helper method: returns coordinates of next possible moves based on location and visited array
def next_Move(currentNode):
    possible_moves = [UP, DOWN, LEFT, RIGHT]
    next_moves = []

    if(currentNode.row==0):
        possible_moves.remove(UP)
    
    if(currentNode.col==0):
        possible_moves.remove(LEFT)
    
    if(currentNode.row==2):
        possible_moves.remove(DOWN)

    if(currentNode.col==2):
        possible_moves.remove(RIGHT)
    
    for move in possible_moves:
        if(move == UP and currentNode.visited[currentNode.row-1][currentNode.col] == 0):
            nextNode = Node(currentNode.row-1,currentNode.col, DOWN, currentNode, visited=currentNode.visited)
            next_moves.append(nextNode)
            continue
        if(move == DOWN and currentNode.visited[currentNode.row+1][currentNode.col] == 0):
            nextNode = Node(currentNode.row+1, currentNode.col, UP, currentNode, visited=currentNode.visited)
            next_moves.append(nextNode)
            continue
        if(move == LEFT and currentNode.visited[currentNode.row][currentNode.col-1] == 0):
            nextNode = Node(currentNode.row, currentNode.col-1, RIGHT, currentNode, visited=currentNode.visited)
            next_moves.append(nextNode)
            continue
        if(move == RIGHT and currentNode.visited[currentNode.row][currentNode.col+1] == 0):
            nextNode = Node(currentNode.row, currentNode.col+1, LEFT, currentNode, visited=currentNode.visited)
            next_moves.append(nextNode)
            continue

    return next_moves




def DFS(puzzle):
    final_solution = []
    q = []

    for r in range(3):
        for c in range(3):
            if puzzle[r][c].strip() == "0":
                startingNode = Node(r, c, visited=[[0,0,0],[0,0,0],[0,0,0]])
                q.insert(0, startingNode)

    while not len(q) == 0:
        currentNode = q.pop(0)
        currentNode.visited[currentNode.row][currentNode.col] = 1
        print("Current Node: [" + str(currentNode.row) + "," + str(currentNode.col) + "]")
        if currentNode.row == 2 and currentNode.col == 2:
            final_solution.append(currentNode)
            break
        else:
            next_moves = next_Move(currentNode)

            for i in range(len(next_moves)):
                print("Can move to [" + str(next_moves[i].row) + "," + str(next_moves[i].col) + "]")
                q.insert(i, next_moves[i])
    
    currentNode = final_solution.pop(0)
    
    while(currentNode.prevNode != None):
        final_solution.insert(0, currentNode.moveToPrevNode)
        currentNode = currentNode.prevNode

    return final_solution


def A_Star_H1(puzzle):
    """
    A-Star with Heuristic 1

    Arguments:
    - puzzle: Node object representing initial state of the puzzle

    Return:
    final_solution: An ordered list of moves representing the final solution.
    """

    final_solution = []

    # TODO: WRITE CODE

    return final_solution


def A_Star_H2(puzzle):
    """
    A-Star with Heauristic 2

    Arguments:
    - puzzle: Node object representing initial state of the puzzle

    Return:
    final_solution: An ordered list of moves representing the final solution.
    """

    final_solution = []

    # TODO: WRITE CODE

    return final_solution