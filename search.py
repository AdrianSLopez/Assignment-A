# ENUMS
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

class Node:
    def __init__(self, row=None, col=None, moveToPrevNode=None, prevNode=None, g=0, h=None, f=None, visited = None, puzzle = None):
        self.row = row
        self.col = col
        self.moveToPrevNode= moveToPrevNode
        self.prevNode = prevNode
        self.g = g
        self.h = h
        self.f = f
        self.visited = visited
        self.puzzle = puzzle


def BFS(puzzle):
    final_solution = []
    if(puzzle[2][2].strip() == "0"):
        return final_solution

    q = []

    for r in range(3):
        for c in range(3):
            if puzzle[r][c].strip() == "0":
                startingNode = Node(r, c, visited=[[0,0,0],[0,0,0],[0,0,0]])
                q.append(startingNode)
    
    while not len(q) == 0:
        currentNode = q.pop(0)
        currentNode.visited[currentNode.row][currentNode.col] = 1

        if currentNode.row == 2 and currentNode.col == 2:
            final_solution.append(currentNode)
            break
        else:
            next_moves = next_Move(currentNode)

            for move in next_moves:
                q.append(move)

    currentNode = final_solution.pop(0)

    while(currentNode.prevNode != None):
        final_solution.insert(0, currentNode.moveToPrevNode)
        currentNode = currentNode.prevNode

    return final_solution

def DFS(puzzle):
    final_solution = []
    if(puzzle[2][2].strip() == "0"):
        return final_solution
    q = []

    for r in range(3):
        for c in range(3):
            if puzzle[r][c].strip() == "0":
                startingNode = Node(r, c, visited=[[0,0,0],[0,0,0],[0,0,0]])
                q.insert(0, startingNode)

    while not len(q) == 0:
        currentNode = q.pop(0)
        currentNode.visited[currentNode.row][currentNode.col] = 1
        if currentNode.row == 2 and currentNode.col == 2:
            final_solution.append(currentNode)
            break
        else:
            next_moves = next_Move(currentNode)

            for i in range(len(next_moves)):
                q.insert(i, next_moves[i])
    
    currentNode = final_solution.pop(0)
    
    while(currentNode.prevNode != None):
        final_solution.insert(0, currentNode.moveToPrevNode)
        currentNode = currentNode.prevNode

    return final_solution


def A_Star_H1(puzzle):
    final_solution = []
    if(puzzle[2][2].strip() == "0"):
        return final_solution
    q = []

    for r in range(3):
        for c in range(3):
            if puzzle[r][c].strip() == "0":
                startingNode = Node(r, c, visited=[[0,0,0],[0,0,0],[0,0,0]], puzzle=puzzle)
                q.insert(0, startingNode)

    while not len(q) == 0:
        currentNode = q.pop(0)
        currentNode.visited[currentNode.row][currentNode.col] = 1

        if currentNode.row == 2 and currentNode.col == 2:
            final_solution.append(currentNode)
            break
        else:
            next_moves = next_Move(currentNode)

            for move in next_moves:
                move.puzzle = [[currentNode.puzzle[0][0], currentNode.puzzle[0][1], currentNode.puzzle[0][2]], [currentNode.puzzle[1][0], currentNode.puzzle[1][1], currentNode.puzzle[1][2]], [currentNode.puzzle[2][0], currentNode.puzzle[2][1], currentNode.puzzle[2][2]]]
                move.h = h1(move.puzzle)
                move.f = move.g + move.h
                updatePuzzle(currentNode, move)
                q.append(move)

            sort(q)
                
    currentNode = final_solution.pop(0)

    while(currentNode.prevNode != None):
        final_solution.insert(0, currentNode.moveToPrevNode)
        currentNode = currentNode.prevNode

    return final_solution

# A_Star_H1 helper method: Update node's puzzle based on 0's new position
def updatePuzzle(currentNode, nextNode):
    temp = nextNode.puzzle[nextNode.row][nextNode.col]
    nextNode.puzzle[nextNode.row][nextNode.col] = nextNode.puzzle[currentNode.row][currentNode.col]
    nextNode.puzzle[currentNode.row][currentNode.col] = temp

# A_Star_H1 helper method: Calculate # of misplaced tiles based on puzzle's state
def h1(puzzle):
    misplacedTiles = 0
    perfectState = {
        "1": [0,0],
        "2": [0,1],
        "3": [0,2],
        "4": [1,0],
        "5": [1,1],
        "6": [1,2],
        "7": [2,0],
        "8": [2,1],
        "0": [2,2]
    }
    for row in range(3):
        for col in range(3):
            if(perfectState[puzzle[row][col].strip()][0] != row or perfectState[puzzle[row][col].strip()][1] != col):
                misplacedTiles+=1

    return misplacedTiles


def A_Star_H2(puzzle):
    final_solution = []
    if(puzzle[2][2].strip() == "0"):
        return final_solution
    q = []

    for r in range(3):
        for c in range(3):
            if puzzle[r][c].strip() == "0":
                startingNode = Node(r, c, visited=[[0,0,0],[0,0,0],[0,0,0]])
                q.insert(0, startingNode)

    while not len(q) == 0:
        currentNode = q.pop(0)
        currentNode.visited[currentNode.row][currentNode.col] = 1

        if currentNode.row == 2 and currentNode.col == 2:
            final_solution.append(currentNode)
            break
        else:
            next_moves = next_Move(currentNode)

            for move in next_moves:
                move.h = h2(puzzle[move.row][move.col].strip(), move.row, move.col)
                move.f = move.g + move.h
                q.append(move)

            sort(q)
    
    currentNode = final_solution.pop(0)

    while(currentNode.prevNode != None):
        final_solution.insert(0, currentNode.moveToPrevNode)
        currentNode = currentNode.prevNode

    return final_solution

def h2(number, row, col):
    perfectState = {
        "1": [0,0],
        "2": [0,1],
        "3": [0,2],
        "4": [1,0],
        "5": [1,1],
        "6": [1,2],
        "7": [2,0],
        "8": [2,1],
        "0": [2,2]
    }

    if(perfectState[number][0] == row and perfectState[number][1] == col):
        return 0
    else:
        rowDist = abs(perfectState[number][0] - row)
        colDist = abs(perfectState[number][1] - col)

        return rowDist + colDist

def sort(q):
    for i in range(1, len(q)):
        j = i
        while j>0 and q[j-1].f >= q[j].f:
            if(q[j-1].f == q[j].f and q[j-1].moveToPrevNode % 2 == 0 and q[j].moveToPrevNode % 2 != 0) or (q[j-1].f == q[j].f and q[j-1].moveToPrevNode == 0 and q[j].moveToPrevNode == 2)  or (q[j-1].f == q[j].f and q[j-1].moveToPrevNode == 1 and q[j].moveToPrevNode == 3):
                break
            temp = q[j-1]
            q[j-1] = q[j]
            q[j] = temp
            j -= 1
           
    return q

# Helper method: returns coordinates of next possible moves based on location and visited array
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
        nextNode = Node(prevNode=currentNode, g=1+currentNode.g, visited=currentNode.visited)

        # Update 0's new position and move to previous Node
        if(move == UP and currentNode.visited[currentNode.row-1][currentNode.col] == 0):
            nextNode.moveToPrevNode = DOWN
            nextNode.row = currentNode.row-1
            nextNode.col = currentNode.col
            next_moves.append(nextNode)
            continue
        if(move == DOWN and currentNode.visited[currentNode.row+1][currentNode.col] == 0):
            nextNode.moveToPrevNode = UP
            nextNode.row = currentNode.row+1
            nextNode.col = currentNode.col
            next_moves.append(nextNode)
            continue
        if(move == LEFT and currentNode.visited[currentNode.row][currentNode.col-1] == 0):
            nextNode.moveToPrevNode = RIGHT
            nextNode.row = currentNode.row
            nextNode.col = currentNode.col-1
            next_moves.append(nextNode)
            continue
        if(move == RIGHT and currentNode.visited[currentNode.row][currentNode.col+1] == 0):
            nextNode.moveToPrevNode = LEFT
            nextNode.row = currentNode.row
            nextNode.col = currentNode.col+1
            next_moves.append(nextNode)
            continue       

    return next_moves