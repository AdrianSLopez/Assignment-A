# ENUMS
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

# https://docs.google.com/presentation/d/18_xcUMHzkcqlAaxNcA-3bX4cMFL5vo5U/edit#slide=id.p1

class Node:
    def __init__(self, row, col, moveToPrevNode, prevNode):
        self.row = row
        self.col = col
        self.moveToPrevNode= moveToPrevNode
        self.prevNode = prevNode


def BFS(puzzle):
    final_solution = []
    q = []
    visited = [[0,0,0],[0,0,0],[0,0,0]] # 0 = unvisited, 1 = visited

    for r in range(3):
        for c in range(3):
            if puzzle[r][c].strip() == "0":
                startingNode = Node(r, c, None, None)
                q.append(startingNode)
                visited[r][c] = 1
    
    while not len(q) == 0:
        currentNode = q.pop(0)
        visited[currentNode.row][currentNode.col] = 1

        if currentNode.row == 2 and currentNode.col == 2:
            final_solution.append(currentNode)
            break
        else:
            next_moves = next_Move(currentNode, visited)

            for move in next_moves:
                q.append(move)

    currentNode = final_solution.pop(0)

    while(currentNode.prevNode != None):
        final_solution.insert(0, currentNode.moveToPrevNode)
        currentNode = currentNode.prevNode

    return final_solution


# BFS helper method: returns coordinates of next possible moves based on location and visited array
def next_Move(currentNode, visited):
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
        if(move == UP and visited[currentNode.row-1][currentNode.col] == 0):
            nextNode = Node(currentNode.row-1,currentNode.col, DOWN, currentNode)
            next_moves.append(nextNode)
            continue
        if(move == DOWN and visited[currentNode.row+1][currentNode.col] == 0):
            nextNode = Node(currentNode.row+1, currentNode.col, UP, currentNode)
            next_moves.append(nextNode)
            continue
        if(move == LEFT and visited[currentNode.row][currentNode.col-1] == 0):
            nextNode = Node(currentNode.row, currentNode.col-1, RIGHT, currentNode)
            next_moves.append(nextNode)
            continue
        if(move == RIGHT and visited[currentNode.row][currentNode.col+1] == 0):
            nextNode = Node(currentNode.row, currentNode.col+1, LEFT, currentNode)
            next_moves.append(nextNode)
            continue

    return next_moves




def DFS(puzzle):
    final_solution = []
    q = []
    visited = [[0,0,0],[0,0,0],[0,0,0]]

    for r in range(3):
        for c in range(3):
            if puzzle[r][c].strip() == "0":
                startingNode = Node(r, c, None, None)
                q.insert(0, startingNode)
                visited[r][c] = 1

    while not len(q) == 0:
        currentNode = q.pop(0)
        visited[currentNode.row][currentNode.col] = 1

        if currentNode.row == 2 and currentNode.col == 2:
            final_solution.append(currentNode)
            break
        else:
            next_moves = next_Move(currentNode, visited)

            for i in range(len(next_moves)):
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