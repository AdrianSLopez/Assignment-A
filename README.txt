Run code: 
    My code works fine with main.py, as long as you run main.py then you are able to run my code.


Which algorithm performed the fastest?
    Using the time library, I was able to time each algorithm for each example data files 3 times.
    For ex1.txt, Depth first search was the fastest at an average of 3.4 seconds, BFS at 5.8 secs, A*H2 at 7.44 secs, and at A*H1 at 8.32 secs
    For ex2.txt, Depth First search was the fastest at an average of 1.52 seconds, BFS at 1.86 seconds, A*H1 at 3.19 secs, and A*H2 at 4.01 secs.
    For ex3.txt, A*H1 was the fastest at 0.07 secs, DFS at 0.08 secs, A*H2 at 0.083 secs, and BFS at 0.09.

Which took up the most memory?
    A*H1 took the most memory. The node to keep trach of each state of the puzzle unlike the other algorithms also inclues a 2d array or basically a version of the puzzle based on the new path. The other solutions don't have this.
    The puzzle in the node is basically there to keep track and help calculate how many misplaced tiles are there in the puzzle, since a move can either misplace more tiles or put some in the correct place.

Which gave the best solution?
    For data in ex2.txt and ex3.txt, my algorithms gave the same answer. Based on ex1.txt, I say Breadth-first search gave the best solution,
    because not only did it reach the goal state, but also all numbers were in the correct position.
