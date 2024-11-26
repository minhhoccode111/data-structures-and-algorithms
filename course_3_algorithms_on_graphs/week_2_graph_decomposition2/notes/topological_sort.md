# Topological Sort Algorithm

## Motivation

- Goal: Linearly order the vertices of a Directed Acyclic Graph (DAG) such that for every directed edge \( u to v \), vertex \( u \) comes before vertex \( v \) in the ordering
- Requirement: The graph must be a DAG (no cycles)

## Key Concepts

- Source: A vertex with no incoming edges (can have outgoing edges)
- Sink: A vertex with no outgoing edges (can have incoming edges)

## Basic Algorithm Idea

1. Find a Sink:

   - A sink is a vertex with no outgoing edges. This vertex will be placed last in the linear ordering

2. Remove Sink:

   - After adding a sink to the ordering, remove it from the graph

3. Repeat:
   - Continue finding sinks, removing them, and adding them to the ordering until all vertices are ordered

## Finding a Sink in a DAG

- Path-based approach:
  - Start from any vertex and follow a directed path
  - If you hit a vertex with no outgoing edges, you've found a sink
  - If you encounter a cycle (path repeats), the graph isn't a DAG

## Algorithm Walkthrough

1. Start: Begin with any vertex and follow directed edges
2. Identify Sink: Once you hit a vertex with no outgoing edges, remove it from the graph and add it to the ordering
3. Repeat the process with the remaining graph

## Example

- In a graph with vertices \( A, B, C, D, E \), follow paths to identify sinks:
  - Example path: \( A to B to C to D \) → D is a sink, remove it
  - Repeat with the remaining graph until all vertices are ordered

## Time Complexity

- Initial Algorithm:
  - The naive approach could take \( O(V^2) \) time (traversing long paths repeatedly for each vertex)
- Optimization: Instead of retracing the entire path, backtrack one step and continue from there, reducing redundant work

## Optimized Algorithm (Using DFS)

- DFS-based Approach:
  - Perform a Depth-First Search (DFS) on the graph
  - Reverse Post-order: The vertices are ordered by the reverse post-order from DFS, which naturally satisfies the requirement that \( u \) comes before \( v \) if there's an edge \( u to v \)
- Efficiency:
  - The optimized algorithm runs in \( O(V + E) \) time, which is much better than the naive \( O(V^2) \)

## Correctness Proof

- Key Idea: If there's an edge \( u to v \), then \( u \) must come before \( v \) in the topological order
- Proof:
  - Case 1: If we explore \( u \) before \( v \), then \( u \)'s post-order will be greater than \( v \)'s
  - Case 2: If \( v \) is explored before \( u \), this would imply a cycle (impossible in a DAG)
  - Case 3: If \( u \) and \( v \) are explored at the same time, the DFS guarantees that \( u \) will finish before \( v \), ensuring \( u \) comes before \( v \)

## Conclusion and Next Steps

- Topological Sort Algorithm:
  - The algorithm sorts the vertices of a DAG in linear order based on the reverse post-order of a DFS traversal
  - Time Complexity: The final time complexity is \( O(V + E) \), which is optimal
- Next Lecture: We will discuss connectivity in directed graphs (digraphs)
