# Strongly Connected Components

## Motivation

- Goal: Understand the different notions of connectivity in directed graphs and how they differ from the undirected case. The main focus will be on strongly connected components

## Key Concepts

1. Undirected Connectivity:

   - In undirected graphs, connected components are straightforward. Two vertices are in the same component if there is a path connecting them

2. Directed Graph Connectivity:
   - In directed graphs, connectivity is more complicated because edges have directions
   - There are several notions of connectivity:
     - Basic Connectivity: Vertices can be reached from each other in some direction, but not necessarily following edge directions
     - Reachable via Directed Edges: One vertex can reach the other following the edge direction
     - Strong Connectivity: Both vertices can reach each other following the edge directions, forming a strongly connected component (SCC)

## Strongly Connected Components (SCC)

- Definition: A strongly connected component is a maximal subset of vertices such that for any two vertices \( u \) and \( v \) in the component, \( u \) is reachable from \( v \), and \( v \) is reachable from \( u \)

- Graph Example:

  - The graph in the lecture contains five SCCs:
    1. A, B, E, F, G, H: All these vertices can reach each other, but not beyond this component
    2. D: It is its own SCC
    3. C and I: These vertices form separate components that can’t reach others

- SCCs create a partition of the graph where vertices in each SCC are strongly connected

## Example Analysis

- Strongly Connected Component of A:
  - The component containing A includes the vertices A, B, E, F, G, H
  - These vertices can reach each other, but once you leave the component, there’s no way to return
  - Vertices like C and I are not part of this component, as they can’t reach any of the other vertices

## Theorem on Strongly Connected Components

- A directed graph can always be partitioned into SCCs where:
  - Vertices \( u \) and \( v \) are connected (i.e., they are in the same SCC) if and only if you can reach \( u \) from \( v \) and vice versa

## Equivalence Relation Proof

- Connectivity in SCCs is an equivalence relation, meaning:

  1. Reflexive: Any vertex is connected to itself
  2. Symmetric: If \( u \) is connected to \( v \), then \( v \) is connected to \( u \)
  3. Transitive: If \( u \) is connected to \( v \), and \( v \) is connected to \( w \), then \( u \) is connected to \( w \)

- Proof:
  - Paths from \( u \to v \) and \( v \to w \) imply there is a path from \( u \to w \) and vice versa, ensuring the equivalence relation holds

## Metagraph of Strongly Connected Components

- Metagraph: After partitioning the graph into SCCs, we can represent these components as a metagraph, where:
  - Each vertex in the metagraph represents a strongly connected component
  - There is an edge between two components if there is a directed edge between any vertex in one component and any vertex in the other component
- Properties:
  - The metagraph is always a Directed Acyclic Graph (DAG)
  - There are no cycles in the metagraph because if there were, it would imply all components in the cycle are the same SCC, which contradicts the definition of SCCs

## Metagraph and DAG Proof

- Why the Metagraph is a DAG:
  - If there were a cycle in the metagraph, it would mean there’s a cycle in the original graph among the SCCs. However, all vertices within an SCC are mutually reachable, so the cycle would imply that all the components in the cycle are the same SCC, which contradicts the assumption of different SCCs

## Summary

- Key Insights:
  - A directed graph can be partitioned into strongly connected components (SCCs)
  - The metagraph of SCCs is always a DAG
  - The connectivity within SCCs behaves similarly to undirected connectivity, but it is directed in nature
