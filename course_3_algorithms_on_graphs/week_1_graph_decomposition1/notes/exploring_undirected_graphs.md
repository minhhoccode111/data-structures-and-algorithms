## Exploring Graphs

- Problem Context:

  - Explore which vertices in a graph are reachable from a given starting vertex
  - Examples of applications:
    - Video Games: Ensure you have explored all rooms (vertices) in a level connected by passageways (edges)
    - Maps: Find paths between locations or verify connectivity in a road system
    - Mazes and Puzzles: Solve them by determining reachability and valid configurations

- Reachability in Graphs:

  - A vertex is reachable from a starting vertex `s` if there exists a path of edges leading to it
  - Problem: Given a graph `G` and a starting vertex `s`, find all vertices reachable from `s`

- Algorithm: Explore(v):

  - Tracks reachable vertices using a recursive approach:
    1. Mark the starting vertex `v` as visited
    2. For each neighbor `w` of `v`, if `w` has not been visited, recursively explore `w`
  - Uses an adjacency list for efficiency in finding neighbors
  - Builds a set of reachable vertices during the process

- Depth-First Search (DFS):
  - Extends `Explore` to find all vertices in a graph, not just those reachable from one starting point
  - Algorithm:
    1. Mark all vertices as unvisited
    2. For each unvisited vertex in the graph, perform `Explore` starting from it
  - Key characteristic: Traverses as far as possible along one path before backtracking
- DFS Example:

  - Start from an unvisited vertex, explore its neighbors recursively
  - Backtrack when no further neighbors exist, then move to the next unvisited vertex
  - Continue until all vertices are visited

- Correctness of DFS:

  - DFS explores all vertices reachable from a given starting vertex, ensuring no vertex is skipped
  - It also ensures no vertex is visited more than once, maintaining efficiency

- Runtime Analysis:

  - Each vertex is explored exactly once: O(V)
  - Each edge is checked exactly twice (once per vertex it connects): O(E)
  - Total runtime: O(V + E), which is linear relative to the size of the graph

- Applications of DFS:
  - Connectivity analysis (e.g., verifying connected components)
  - Maze solving
  - Pathfinding in games and navigation systems
  - Graph puzzles and other combinatorial problems

## Connectivity

- Concept of Connected Components:

  - In an undirected graph, vertices can be grouped into connected components:
    - Two vertices are in the same connected component if and only if they are reachable from each other
    - A connected component is like an "island," where any vertex within it can reach any other vertex, but there are no connections to vertices in other components

- Equivalence Relation of Reachability:

  - Reachability satisfies the properties of an equivalence relation:
    1. Reflexivity: A vertex `v` is reachable from itself
    2. Symmetry: If `v` is reachable from `w`, then `w` is reachable from `v`
    3. Transitivity: If `u` is reachable from `v` and `v` is reachable from `w`, then `u` is reachable from `w`

- Algorithm to Compute Connected Components:

  - Build on Depth-First Search (DFS):
    - Use `Explore(v)` to find all vertices in the connected component containing `v`
    - Repeat for all unvisited vertices to identify other components

- Component Labeling:

  - Instead of returning vertex sets, assign a unique Connected Component (CC) number to each vertex:
    - Start with `CC = 1`
    - For each unvisited vertex `v`:
      - Run `Explore(v)` and assign `CC` to all reachable vertices
      - Increment `CC` after completing exploration of a component

- Example:

  - On a graph with multiple disconnected components:
    1. Start from an unvisited vertex in one component, explore it, and assign it `CC = 1`
    2. Move to another unvisited vertex in a different component, explore it, and assign it `CC = 2`
    3. Repeat until all vertices are labeled

- Correctness:

  - Each `Explore` finds a complete connected component
  - Every vertex is eventually visited because the outer loop of the DFS ensures all vertices are checked

- Runtime:
  - The algorithm is a modified DFS, so its runtime remains O(V + E), where:
    - `V` is the number of vertices
    - `E` is the number of edges

## Previsit and Postvisit Orderings

- Introduction to Previsit and Postvisit:

  - Previsit and postvisit numbers capture the order in which vertices are visited during a DFS
  - These numbers are useful for analyzing the execution of DFS and will be key for later algorithms

- Augmenting DFS with Previsit and Postvisit:

  - Previsit: A function run when a vertex is first discovered
  - Postvisit: A function run right before finishing the exploration of a vertex
  - A clock is introduced to assign timestamps during DFS:
    - Increment the clock during each previsit and postvisit
    - Record timestamps for each vertex

- Example of Previsit and Postvisit:

  - A clock starts at 1
  - Previsit numbers are assigned when a vertex is first visited
  - Postvisit numbers are assigned after all neighbors of a vertex have been explored
  - Example workflow:
    1. Visit vertex `A`: Previsit = 1
    2. Explore neighbor `B`: Previsit = 2
    3. Complete exploration of `B`: Postvisit = 3
    4. Return to `A` and continue: Postvisit = 4

- Key Property of Previsit and Postvisit:

  - The intervals defined by `[pre(u), post(u)]` for vertices `u` and `v` are either:
    - Nested: One interval is completely contained within the other
    - Disjoint: The intervals do not overlap at all
  - Interleaved intervals are not possible in a valid DFS execution

- Proof of the Interval Property:

  - Case 1: `v` is discovered while exploring `u`:
    - `v` is a descendant of `u` in the DFS tree
    - The interval for `v` is nested within the interval for `u`
  - Case 2: `v` is discovered after `u` is fully explored:
    - `u` and `v` are in different branches of the DFS tree
    - The intervals for `u` and `v` are disjoint

- Practical Use of Previsit and Postvisit:

  - The relationship between intervals provides information about the structure of the graph and the DFS execution order
  - Useful for determining ancestor/descendant relationships in the DFS tree

- Validation of Previsit and Postvisit Numbers:
  - A valid set of previsit and postvisit numbers ensures no interleaved intervals
  - Example:
    - `[pre(A), post(A)]` and `[pre(B), post(B)]` cannot overlap partially; they must be nested or disjoint
