
# Recursive Version of Floyd-Warshall Algorithm

This project aims to enhance the Floyd-Warshall algorithm by implementing a recursive method. The deliverables include a recursive implementation of the algorithm, an iterative implementation sourced from geeksforgeeks, unit tests validating the correctness of the recursive implementation, a performance comparison analysis highlighting the differences in running time and complexity, as well as a detailed report outlining the project's methodology and findings.


## What is Floyd-Warshall Algorithm?

The Floyd-Warshall algorithm is an algorithm used to find the shortest path between all pairs of nodes in a weighted graph. The matrix is initially filled with the weights of the edges connecting the nodes, and the algorithm updates the matrix by considering all possible intermediate nodes that could make a shorter path between each pair of nodes. For each intermediate node, it computes the distance between each pair of nodes as the minimum of the distance between start node and end node using an intermediate node or the current distance between start node and end node. The process repeats until all possible intermediate nodes have been considered.

![Initial Graph (1)](https://github.com/tolgatosunn/Floyd-Warshall_Recursion/blob/main/Images/Initial%20Graph.PNG)

![Initial Matrix](https://github.com/tolgatosunn/Floyd-Warshall_Recursion/blob/main/Images/Initial%20Matrix.PNG)

## References

(1) https://www.programiz.com/dsa/floyd-warshall-algorithm