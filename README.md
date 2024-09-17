
1
Aim:To write a python program to solve 8 queens problem
Algorithm:
1.	Initialize an empty chessboard of size 8x8.
2.	Start placing queens column by column, beginning with the first column.
3.	For each column, try placing a queen in each row and check if it's safe.
4.	If it's safe, place the queen and move to the next column.
5.	If placing a queen leads to no solution, backtrack by removing the last placed queen.
6.	Repeat steps 3-5 until all queens are placed or all possibilities are exhausted.


2
Aim:To write a python program to  water jug problem
Algorithm:
1.	Initialize two jugs with capacities X and Y and a target amount Z.
2.	Start with both jugs empty.
3.	Fill one jug or pour water from one jug to another.
4.	Check if either jug contains exactly the target amount.
5.	If not, repeat step 3 until a solution is found or no more valid moves are possible.
6.	If a solution is found, stop; otherwise, backtrack and try a different sequence of actions.
3
Aim:To write a python program to crypt arthemetic problem
Algorithm:
1.	Define the words in the equation as variables, treating each letter as a digit.
2.	Create all possible digit assignments for the letters.
3.	Check for uniqueness in the digit assignment (no repeating digits).
4.	Substitute the digit values into the equation and evaluate the result.
5.	If the equation holds true, print the valid assignment.
6.	Repeat until all valid assignments are checked or a solution is found.
4
Aim:To write a python program to implement breadth first search  algorithm
Algorithm:
1.	Initialize a queue and enqueue the starting node.
2.	Mark the starting node as visited.
3.	Dequeue a node from the queue and process it.
4.	Enqueue all its unvisited neighbors and mark them as visited.
5.	Repeat steps 3-4 until the queue is empty.
6.	End when all nodes have been visited.
5
Aim:To write a python program to solve depth first search algorithm 
Algorithm:
1.	Start at the initial node and mark it as visited.
2.	Explore as far as possible along each branch before backtracking.
3.	Push unvisited neighbors of the current node onto a stack.
4.	Pop the next node from the stack and mark it as visited.
5.	Repeat steps 3-4 until the stack is empty.
6.	End when all nodes have been visited.
6
Aim:To write a python program to  A* search algorithm
Algorithm:
1.	Initialize the open list with the starting node and the closed list as empty.
2.	While the open list is not empty, get the node with the lowest f score (where f = g + h).
3.	If the current node is the goal, reconstruct the path and return the solution.
4.	For each neighbor of the current node, calculate its g, h, and f values.
5.	If the neighbor is not in the open list, add it; if it is, check if the new path is shorter.
6.	Move the current node to the closed list and repeat until the goal is found or the open list is empty.
7
Aim:To write a python program to map colouring to attain CSP 
Algorithm:
1.	Define the map as a graph where nodes represent regions and edges represent adjacent regions.
2.	Define a list of colors to be used for coloring the map.
3.	Create a function to check if the current coloring assignment is valid (i.e., no two adjacent regions have the same color).
4.	Use a backtracking algorithm to assign colors to each region, ensuring that the coloring remains valid.
5.	If a valid coloring is found, return the solution.
6.	If no valid coloring can be found for a region, backtrack and try a different color for the previous regions.# CSA1751-AI-LABPROGRAMS
