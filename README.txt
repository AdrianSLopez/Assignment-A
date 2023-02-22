Run code: 
    My code works fine with main.py, as long as you run main.py then you are able to run my code.


Which algorithm performed the fastest?
    A*H1 performs the fastest. For ex1.txt, BFS and A*H1 took 0ms to find a solution. With A*H2 at 0.99ms and DFS at 9840ms.
    For ex2.txt, A*H1 performed the fastest again clocking in at 0.49ms, BFS at 1.48ms, DFS at 21977ms, and A*H2 at 79ms.
    For ex3.txt, A*H1 found the solution in 0ms, BFS at 1.48ms, DFS at 34067ms, and A*H2 at 39ms. Using the time library I was
    able to store the time before and after the line of code that calls my algorithms, thus I was able to time my runs.


Which took up the most memory?
    All solutions are implemented similarly except for a few things like sorting the que for A* algorithms, add new paths to the end or start of the queue. 
    Depth First search would be the algorithm that takes the most memory because more nodes are explored in depth first search. And for every valid and possible move 0 can take,
    a node is created along with it's position, puzzle state, and list of Nodes that contain puzzles that have been explored. Which basically means the more valid and acceptable paths explored
    the more Nodes are created and added to the queue. Not only does Depth First Search take up the most memory but is also the slowest in finding the solution.

Which gave the best solution?
    BFS, A* H1 and H2 gave the same solution for all examples. Judging by the speed I say A* H1 gave the best solution since it was the quickest in all data examples provided.