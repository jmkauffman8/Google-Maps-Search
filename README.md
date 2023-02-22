# Google-Maps-Search
Using BFS, DFS, and A* Search Algorithms to create a Google Maps alternative that optimizes routes around Rice University campus

## Overview
This Capstone Project for Rice's Computational Thinking course uses Python to implement stacks and queues in order to use a variety of search algorithms to find routes near the Rice University campus. Note: because this project uses packages designed for the course, it is best run in the online IDE developed by the class' professor: https://py3.codeskulptor.org/

## Introduction

Graph search algorithms are fundamental tools in computer science and have numerous applications, from social networks to logistics and transportation systems. In this project, we explore and implement three different graph search algorithms: Breadth-First Search (BFS), Depth-First Search (DFS), and A* search.

BFS and DFS are classic graph search algorithms that have been widely studied and applied. They differ in their exploration strategy: BFS explores the graph by visiting all neighbors of a node before moving to the next level, while DFS explores the graph by visiting one of the neighbors of a node and continuing along that path until it reaches a dead-end before backtracking. A* search is an informed search algorithm that uses a heuristic function to guide its search towards the goal node.

In this project, we will start by modifying the BFS algorithm to implement both BFS and DFS. We will then implement a recursive version of DFS, followed by the A* search algorithm. For each algorithm, we will provide a clear and concise recipe that describes the steps involved in the algorithm, as well as the corresponding Python code.

The objective of this project is to gain a deeper understanding of graph search algorithms, and to demonstrate our ability to implement and apply these algorithms to real-world problems. By the end of this project, we will have a working implementation of three different graph search algorithms that can be used to solve a variety of problems, from finding the shortest path in a transportation network to optimizing a logistics route.

## Methodology

### Modified BFS

Breadth-First Search (BFS) is a graph traversal algorithm that explores all the vertices of a graph in breadth-first order. In a regular BFS algorithm, we start at the root node and visit all its neighbors before visiting any of their neighbors, and so on, until we have visited all nodes in the graph. However, in some cases, we might want to modify the BFS algorithm to meet specific requirements. For example, we might want to implement a BFS algorithm that terminates once it reaches a goal state, or we might want to implement a weighted BFS algorithm where the weight of each edge is taken into account. In general, we can modify the BFS algorithm to suit our needs by changing how we choose which node to visit next and how we update the visited set.

One way to modify the BFS algorithm is by using a priority queue to choose which node to visit next. Instead of visiting nodes in the order they were added to the queue, we can visit nodes in order of their priority. The priority of a node is determined by a heuristic function that estimates the distance between the current node and the goal node. This modification is known as the A* algorithm, which we will discuss in more detail in section C.

Pictured below is an implementation of BFS to navigate across campus

<img width="1022" alt="Screen Shot 2023-02-21 at 7 42 16 PM" src="https://user-images.githubusercontent.com/105028034/220499154-4eea7111-ff85-41f8-a922-64481bd85658.png">


### Implement Recursive DFS

Depth-First Search (DFS) is a graph traversal algorithm that explores all the vertices of a graph in depth-first order. In a regular DFS algorithm, we start at the root node and visit all its neighbors before backtracking and visiting the neighbors of its neighbors, and so on, until we have visited all nodes in the graph. However, like BFS, we might want to modify the DFS algorithm to meet specific requirements. For example, we might want to implement a DFS algorithm that terminates once it reaches a goal state, or we might want to implement an iterative DFS algorithm that uses a stack instead of recursion.

One way to modify the DFS algorithm is by implementing it recursively. Recursive DFS works by calling the DFS function recursively on each unvisited neighbor of the current node. This means that we will explore each branch of the graph to its deepest point before backtracking and exploring the next branch. Recursive DFS is easy to implement and is suitable for small graphs or graphs with a small depth. However, it can be memory-intensive for large graphs, as each recursive call adds a new layer to the call stack.

Pictured below is an implementation of DFS to navigate across campus

<img width="1029" alt="Screen Shot 2023-02-21 at 7 44 43 PM" src="https://user-images.githubusercontent.com/105028034/220499486-d051e215-a21d-4796-a46b-c3a7d837f641.png">


### A* Search

The A* algorithm is a graph traversal algorithm that is used to find the shortest path between two nodes in a graph. Like BFS, it explores all the vertices of a graph, but it uses a heuristic function to determine the priority of each node. The heuristic function estimates the distance between the current node and the goal node, and this estimate is used to prioritize which nodes to visit next.

The A* algorithm is a modification of the regular BFS algorithm, as it uses a priority queue to choose which node to visit next. However, unlike BFS, the priority of a node in A* is determined by the sum of the cost of the path from the start node to the current node and the estimated distance from the current node to the goal node. This sum is known as the f-value, and the node with the lowest f-value is visited next.

The A* algorithm is guaranteed to find the shortest path between the start node and the goal node if the heuristic function is admissible and consistent. An admissible heuristic function underestimates the distance between any two nodes in the graph, while a consistent heuristic function satisfies the triangle inequality. The A* algorithm is widely used in pathfinding and robotics, where finding the shortest path between two points is essential.

Pictured below is an implementation of A* to navigate across campus

<img width="1028" alt="Screen Shot 2023-02-21 at 7 42 31 PM" src="https://user-images.githubusercontent.com/105028034/220499192-72e591c4-470c-4836-94a2-696f46380e3f.png">

## Results and Discussion

The results of our experiments showed that A* algorithm performed the best among the three algorithms in terms of the number of nodes visited and the time taken to find the optimal solution. A* algorithm was able to find the optimal solution using the least number of nodes visited, followed by Recursive DFS and then BFS.

Furthermore, the results also revealed that the modified BFS algorithm performed better than the original BFS algorithm. By avoiding revisiting previously explored nodes, the modified BFS algorithm was able to reduce the time taken to find the optimal solution. However, it was not as effective as Recursive DFS and A* in terms of the number of nodes visited.

Our results show that the A* algorithm is the most efficient algorithm for finding the optimal solution among the three algorithms tested. This is because A* algorithm makes use of heuristic functions to guide the search towards the goal node, thus reducing the number of nodes visited and the time taken to find the optimal solution.

The modified BFS algorithm, which avoids revisiting previously explored nodes, also showed a significant improvement over the original BFS algorithm. This modification allowed BFS to perform better than Recursive DFS in terms of the number of nodes visited while still maintaining a reasonable time complexity.

In practice, the choice of algorithm depends on the specific problem being solved and the available computational resources. A* algorithm is generally preferred for problems that require finding the optimal solution quickly, while BFS and DFS may be more appropriate for problems with limited computational resources or where the optimal solution is not critical.

In conclusion, our experiments demonstrate the importance of selecting the appropriate algorithm for a given problem. By considering the characteristics of the problem and the available resources, we can select the most appropriate algorithm to achieve the desired outcome.

## Conclusion

In conclusion, this project involved modifying the BFS algorithm to implement both BFS and DFS, implementing a recursive version of DFS, and performing A* search. The modified algorithms and implementation of A* search were shown to be more efficient and accurate in solving search problems. These modifications and implementations can be further optimized and applied to a wide range of search problems

