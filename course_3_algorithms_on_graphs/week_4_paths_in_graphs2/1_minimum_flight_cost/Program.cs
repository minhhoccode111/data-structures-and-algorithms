/*

diff <(dotnet run <test/1) <(cat test/1.a)
diff <(dotnet run <test/2) <(cat test/2.a)
diff <(dotnet run <test/3) <(cat test/3.a)

*/

using System;
using System.Collections.Generic;

class Node : IComparable
{
    public int Idx { get; set; }
    public int Dist { get; set; }

    public Node(int idx, int dist)
    {
        Idx = idx;
        Dist = dist;
    }

    public int CompareTo(object obj)
    {
        Node other = (Node)obj;
        return this.Dist.CompareTo(other.Dist);
    }
}

class WeightedDiGraph
{
    private List<List<int>> adj;
    private List<List<int>> weights;

    public WeightedDiGraph(int n)
    {
        adj = new List<List<int>>();
        weights = new List<List<int>>();

        for (int i = 0; i < n; i++)
        {
            adj.Add(new List<int>());
            weights.Add(new List<int>());
        }
    }

    public void AddEdges(int m)
    {
        for (int j = 0; j < m; j++)
        {
            string[] input = Console.ReadLine().Split(' ');
            int s = int.Parse(input[0]) - 1;
            int t = int.Parse(input[1]) - 1;
            int w = int.Parse(input[2]);

            adj[s].Add(t);
            weights[s].Add(w);
        }
    }

    public int Dijkstra(int s, int t)
    {
        int n = adj.Count;
        int[] dist = new int[n];
        for (int i = 0; i < n; i++)
        {
            dist[i] = int.MaxValue;
        }
        dist[s] = 0;

        // Custom priority queue simulation
        List<Node> pq = new List<Node>();
        pq.Add(new Node(s, 0));

        HashSet<int> processed = new HashSet<int>();

        while (pq.Count > 0)
        {
            // Find and remove the minimum element
            int minIndex = 0;
            for (int i = 1; i < pq.Count; i++)
            {
                if (pq[i].Dist < pq[minIndex].Dist)
                {
                    minIndex = i;
                }
            }
            Node curr = pq[minIndex];
            pq.RemoveAt(minIndex);

            // If we've reached the target, return the distance
            if (curr.Idx == t)
            {
                return curr.Dist;
            }

            // Skip if already processed
            if (processed.Contains(curr.Idx))
            {
                continue;
            }

            // Process outgoing edges
            for (int i = 0; i < adj[curr.Idx].Count; i++)
            {
                int neighbor = adj[curr.Idx][i];
                int weight = weights[curr.Idx][i];

                // Relax the edge
                if (dist[neighbor] > dist[curr.Idx] + weight)
                {
                    dist[neighbor] = dist[curr.Idx] + weight;
                    pq.Add(new Node(neighbor, dist[neighbor]));
                }
            }

            processed.Add(curr.Idx);
        }

        // If no path found
        return -1;
    }
}

class Program
{
    static void Main()
    {
        string[] firstLine = Console.ReadLine().Split(' ');
        int n = int.Parse(firstLine[0]);
        int m = int.Parse(firstLine[1]);

        WeightedDiGraph graph = new WeightedDiGraph(n);
        graph.AddEdges(m);

        string[] lastLine = Console.ReadLine().Split(' ');
        int s = int.Parse(lastLine[0]) - 1;
        int t = int.Parse(lastLine[1]) - 1;

        Console.WriteLine(graph.Dijkstra(s, t));
    }
}
