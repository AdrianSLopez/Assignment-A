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

# TODO:
    # For every algorith switch goal state to perferct puzzle (1/4)
    # Apply BFS changes to rest of algorithms
def BFS(puzzle):
    puzzle = clean(puzzle)
    final_solution = []
    q = []

    if(matchGoalState(puzzle)): return final_solution

    # find location of zero, create initial node and append to q
    for r in range(3):
        for c in range(3):
            if puzzle[r][c].strip() == "0":
                startingNode = Node(r, c, puzzle=puzzle)
                q.append(startingNode)
    
    while not len(q) == 0:
        currentNode = q.pop(0)
        # print(str(currentNode.puzzle[0][0]) + " " + str(currentNode.puzzle[0][1]) + " " +  str(currentNode.puzzle[0][2]))
        # print(str(currentNode.puzzle[1][0]) + " " + str(currentNode.puzzle[1][1]) + " " +  str(currentNode.puzzle[1][2]))
        # print(str(currentNode.puzzle[2][0]) + " " + str(currentNode.puzzle[2][1]) + " " +  str(currentNode.puzzle[2][2]))
        # print()

        if matchGoalState(currentNode.puzzle):
            final_solution.append(currentNode)
            break
        else:
            next_moves = next_Move(currentNode)
            # print(str(len(next_moves)) + " possibles moves.")
            # print()
            for move in next_moves:
                move.puzzle = [[currentNode.puzzle[0][0], currentNode.puzzle[0][1], currentNode.puzzle[0][2]], [currentNode.puzzle[1][0], currentNode.puzzle[1][1], currentNode.puzzle[1][2]], [currentNode.puzzle[2][0], currentNode.puzzle[2][1], currentNode.puzzle[2][2]]]
                updatePuzzle(currentNode, move)
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

            for i in range(len(next_moves)):
                next_moves[i].puzzle = [[currentNode.puzzle[0][0], currentNode.puzzle[0][1], currentNode.puzzle[0][2]], [currentNode.puzzle[1][0], currentNode.puzzle[1][1], currentNode.puzzle[1][2]], [currentNode.puzzle[2][0], currentNode.puzzle[2][1], currentNode.puzzle[2][2]]]
                updatePuzzle(currentNode, next_moves[i])
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
                next_moves[i].puzzle = [[currentNode.puzzle[0][0], currentNode.puzzle[0][1], currentNode.puzzle[0][2]], [currentNode.puzzle[1][0], currentNode.puzzle[1][1], currentNode.puzzle[1][2]], [currentNode.puzzle[2][0], currentNode.puzzle[2][1], currentNode.puzzle[2][2]]]
                updatePuzzle(currentNode, next_moves[i])
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
        "9": [2,2]
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

# Helper method: removes any '\n' from puzzle data
def clean(puzzle):
    for r in range(3):
        for c in range(3):
            puzzle[r][c] = puzzle[r][c].strip()

    return puzzle

# Helper method: returns list of nodes that contains possible puzzle states where 0 can move based on currentNode's puzzle/zero's position
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
        nextNode = Node(prevNode=currentNode, g=1+currentNode.g)
        
        if(move == UP):
            nextNode.moveToPrevNode = DOWN
            nextNode.row = currentNode.row-1
            nextNode.col = currentNode.col
        elif(move == DOWN): 
            nextNode.moveToPrevNode = UP
            nextNode.row = currentNode.row+1
            nextNode.col = currentNode.col
        elif(move == LEFT): 
            nextNode.moveToPrevNode = RIGHT
            nextNode.row = currentNode.row
            nextNode.col = currentNode.col-1
        else:
            nextNode.moveToPrevNode = LEFT
            nextNode.row = currentNode.row
            nextNode.col = currentNode.col+1

        if(currentNode.prevNode == None):
            next_moves.append(nextNode)
            continue

        if(nextNode.row == currentNode.prevNode.row and nextNode.col == currentNode.prevNode.col):
            continue

        next_moves.append(nextNode)

    return next_moves

# Helper method : returns true or false if currentNodePuzzle mathes Goal state/puzzle
def matchGoalState(currentNodePuzzle):
    goalState = [[1,2,3], [4,5,6], [7,8,0]]

    for r in range(3):
        for c in range(3):
            if int(currentNodePuzzle[r][c]) != goalState[r][c]:
                return False
    
    return True