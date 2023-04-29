
# Recursive Version of Floyd-Warshall Algorithm

This project aims to enhance the Floyd-Warshall algorithm by implementing a recursive method. The deliverables include a recursive implementation of the algorithm, an iterative implementation, unit tests validating the correctness of the recursive implementation, a performance comparison analysis highlighting the differences in running time and complexity, as well as a detailed report outlining the project's methodology and findings.


## What is Floyd-Warshall Algorithm?

The Floyd-Warshall algorithm is an algorithm used to find the shortest path between all pairs of nodes in a weighted graph. The matrix is initially filled with the weights of the edges connecting the nodes, and the algorithm updates the matrix by considering all possible intermediate nodes that could make a shorter path between each pair of nodes. For each intermediate node, it computes the distance between each pair of nodes as the minimum of the distance between start node and end node using an intermediate node or the current distance between start node and end node. The process repeats until all possible intermediate nodes have been considered.

![Initial Graph](https://github.com/tolgatosunn/Floyd-Warshall_Recursion/blob/main/Images/Initial%20Graph.PNG)
[Initial graph which displays distances between the nodes](https://www.programiz.com/dsa/floyd-warshall-algorithm)

![Initial Matrix](https://github.com/tolgatosunn/Floyd-Warshall_Recursion/blob/main/Images/Initial%20Matrix.PNG)
[Initial matrix which includes all the distances between the nodes.](https://www.programiz.com/dsa/floyd-warshall-algorithm)

![Final Matrix](https://github.com/tolgatosunn/Floyd-Warshall_Recursion/blob/main/Images/Final%20Matrix.PNG)
[Final matrix which includes all the shortest distances between the nodes.](https://www.programiz.com/dsa/floyd-warshall-algorithm)

## Recursive Version

Module Name: floyd_recursion.py

Firstly, the system prompts the user to enter a positive integer representing the desired range of the graph. The input is validated to ensure it is indeed a positive integer. If the input does not meet this requirement, appropriate warnings are raised, and the system exits. A graph is then generated based on the provided range using randomly generated values.

The "floyd" function determines the shortest path between nodes. The function requires a previously generated graph, graph_range and an intermediate node number as input.

The function then checks if intermediate_node is less than the graph_range. If so, the function iterates through the for loops for each start node and end node. It updates the distance matrix by comparing the distance from each start_node to each end_node with the distance through the intermediate_node. If the latter is shorter, the distance matrix is updated accordingly.

The function then recursively calls itself with the updated distance matrix and the intermediate_node incremented by 1. This process continues until intermediate_node is equal to or greater than the graph_range.

Once all possible shortest paths have been found, the function prints the final distance matrix using the print_graph function.




## Iterative Version

Module Name: floyd_iteration.py

This module is an iterative version of the Floyd-Warshall algorithm to be compared with the recursive version of the algorithm.

## Unit Test of Recursive Floyd-Warshall Algorithm

Module Name: test_floyd_recursion.py

This piece of code performs unit tests of get_user_input, graph_creator, floyd and print_graph functions from floyd_recursion module.
## Time Performance Comparision

Module Name: time_performance.py

This piece of code is designed to compare the required execution time of recursive and iterative versions of the Floyd-Warshall algorithm. 

The module generates 10,000 graphs with random variables. The shortest distances between the nodes in each graph is calculated by recursive and iterative version of the algorithm.The difference in ratio is then printed as the output.

As a result, iterative version is about 10% faster than recursive version.
## Complexity Comparision

Module Name: time_complexity_comparison.ipynb

This module is designed to compare the complexity of the recursive and iterative versions of the Floyd-Warshall algorithm. The finding is that there is no significant difference between the versions. 
## The Report

The report explains how the application is built alongside its unit tests. Also, the performance of the recursive and the iterative versions of the Floyd-Warshall algorithm is discussed.