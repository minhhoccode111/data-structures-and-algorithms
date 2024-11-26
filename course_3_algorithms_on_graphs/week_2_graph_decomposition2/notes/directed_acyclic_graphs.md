## Directed Graphs vs Undirected Graphs

- Motivation:
  - Directed graphs are used when edges have a direction, meaning the relationship between pairs of nodes is not symmetric.
  - Examples of directed graphs:
    - City maps: One-way streets where the direction matters for navigation
    - Web pages: Links between pages (e.g., A → B but not necessarily B → A)
    - Social networks: Followers can be one-directional (e.g., Twitter)
    - Task dependencies: Tasks that must be completed in a specific order (e.g., waking up before showering)

## Depth First Search (DFS) on Directed Graphs

- Modifications:

  - In DFS for directed graphs, you only explore edges in the direction from a vertex \( v \) to a neighbor \( w \)
  - This ensures you're exploring reachable vertices following the directed edges

- Properties:
  - Pre- and post-orderings can still be computed
  - DFS on directed graphs runs in linear time, just like for undirected graphs

## Task Dependency Example

- Task Dependencies:
  - Tasks (e.g., wake up, shower, eat breakfast, go to work) have a specific order based on their dependencies
  - This can be represented by a directed graph, where directed edges indicate dependencies (e.g., wake up → shower)
  - A linear order is desired that respects all dependencies (e.g., wake up before shower, shower before getting dressed)

## Cycle and Linear Ordering

- Is linear ordering always possible?

  - No, if a directed graph has a cycle (i.e., a sequence of vertices where each vertex points to the next in a directed manner, creating a loop), it is impossible to linearly order the graph
  - Example: The chicken-and-egg problem: You need chickens to lay eggs and eggs to hatch chickens, so no order is possible

- Theorem:
  - If a directed graph contains a cycle, it cannot be linearly ordered
  - Proof: If there's a cycle, any linear ordering will contradict the direction of the edges in the cycle

## Directed Acyclic Graphs (DAGs)

- DAG: A directed acyclic graph (DAG) is a directed graph with no cycles

  - DAGs can be linearly ordered
  - Theorem: Any DAG can be linearly ordered

- Example:
  - Graphs (A, B, C) are shown, where only graph A is a DAG (no cycles), while graphs B and C contain cycles

## Conclusion

- Theorem: If a directed graph is a DAG, it can be linearly ordered
