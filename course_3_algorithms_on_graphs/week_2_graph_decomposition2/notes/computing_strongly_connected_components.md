# Computing Strongly Connected Components (SCCs)

## Motivation

- Goal: Find an efficient algorithm to compute the strongly connected components (SCCs) of a directed graph
- Recap from the Previous Lecture:
  - A directed graph can be divided into strongly connected components, where within a component, every vertex is reachable from every other vertex, but vertices outside the component cannot reach it
  - Metagraph: The SCCs of a graph are connected to each other in a Directed Acyclic Graph (DAG)

## Problem Overview

- Given: A directed graph \( G \), we need to find the strongly connected components (SCCs) of \( G \)
- Naive Approach:
  - For each vertex \( v \), run a depth-first search (DFS) to find all vertices reachable from \( v \)
  - After that, look for vertices that can both reach and be reached by \( v \), which will form the SCC
  - Time Complexity: \( O(V^2 + V \times E) \), which is a bit slow

## Improved Approach: Reverse DFS

- Key Insight: If we run DFS from a vertex \( v \), we explore all reachable vertices, but if \( v \) is in a sink SCC (an SCC with no outgoing edges), we will exactly discover the SCC that contains \( v \)
- Problem: How to find a vertex in a sink component efficiently?

### Theorem for Postorder Numbers

- Theorem: If two SCCs \( C \) and \( C' \) are connected by an edge from \( C \) to \( C' \), the largest postorder number in \( C \) is greater than the largest postorder number in \( C' \)
- Proof:

  - When running DFS, if we visit a vertex in \( C \) before \( C' \), we will finish exploring \( C \) before \( C' \), making the postorder number in \( C \) larger
  - If we visit \( C' \) first, we can't reach \( C \), and so \( C \)’s postorder number will be larger

  This means that the vertex with the largest postorder number is always in the sink component of the graph

## Using Reverse Graph to Find Sink SCC

- Reverse Graph: Reverse the direction of all edges in the graph. The strongly connected components in the reverse graph are the same as in the original graph, but the edges in the metagraph are reversed
- Goal: Find the sink component of the original graph by looking at the reverse graph
- Method:
  1. Run DFS on the reverse graph
  2. The vertex with the largest postorder number in the reverse graph must belong to a sink SCC in the original graph
  3. Once we find this vertex, we can explore it to get the SCC
  4. After finding one SCC, we remove it from the graph and repeat the process until all SCCs are found

## Step-by-Step Algorithm

1. Reverse the Graph: Reverse the direction of all edges in the graph
2. DFS on Reverse Graph: Run DFS on the reverse graph and record the postorder numbers of all vertices
3. Find Sink SCC: The vertex with the largest postorder number belongs to the sink component
4. Explore and Mark SCC: Explore the vertices reachable from the sink component and mark them as part of the same SCC
5. Remove and Repeat: Remove the explored SCC from the graph and repeat the process until all SCCs are found

## Optimized Algorithm

- Instead of running DFS repeatedly, we can optimize the process:
  - Run DFS once on the reverse graph to obtain the postorder numbers of all vertices
  - Then, look for the vertex with the largest postorder number that hasn't been visited yet in the original graph
  - Explore that vertex and mark the SCC
  - Time Complexity: \( O(V + E) \), which is linear in the size of the graph, making it much more efficient than the previous approach

## Example Walkthrough

- Graph Example:
  - Reverse the graph and run DFS to get the postorder numbers
  - The vertex with the largest postorder number in the reverse graph is explored first, which gives the first SCC
  - After removing this SCC, repeat the process for the remaining graph until all SCCs are discovered

## Conclusion

- Efficient Algorithm: By using reverse DFS and postorder numbers, we can efficiently compute the strongly connected components of a graph in \( O(V + E) \) time
- Applications: This algorithm is fundamental for various graph-based problems, including decomposition and pathfinding
