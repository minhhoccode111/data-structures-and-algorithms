using System;
using System.Collections.Generic;
using System.Linq;

public class Reachability
{
    // init a visited array to keep trach of visited nodes
    static bool[] visited;

    // helper function for DFS
    static bool DFS(List<int>[] adj, int current, int target)
    {
        // if the current node is the target, return true
        if (current == target)
            return true;

        // mark the current node as visited
        visited[current] = true;

        // explore all neighbors of the current node
        foreach (int neighbor in adj[current])
        {
            // if the neighbor is not visited, recursively call DFS
            if (!visited[neighbor])
                // if neighbor is the target, return true
                if (DFS(adj, neighbor, target))
                    return true;
        }

        // if no that is found, return false
        return false;
    }

    private static int Reach(List<int>[] adj, int x, int y)
    {
        visited = new bool[adj.Length];

        // return 1 or 0 base on function call DFS's result using x and y
        if (DFS(adj, x, y))
            return 1;
        return 0;
    }

    public static void Main()
    {
        // read first line input
        int[] input = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
        // n: vertices, m: edges
        int n = input[0];
        int m = input[1];
        // an array of adjacency lists<int>, base on vertices n
        List<int>[] adj = new List<int>[n];
        for (int i = 0; i < n; i++)
        {
            adj[i] = new List<int>();
        }
        // loop through m edges
        for (int j = 0; j < m; j++)
        {
            // read input for each edge
            int[] line = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
            // extract x and y, remember to use indexes
            int lineX = line[0] - 1;
            int lineY = line[1] - 1;
            // add to adjacency lists
            adj[lineX].Add(lineY);
            adj[lineY].Add(lineX);
        }

        // last line, to check if x have path to y
        int[] lastLine = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
        int x = lastLine[0] - 1;
        int y = lastLine[1] - 1;

        // print result of reach function with adjacency lists and x and y
        Console.WriteLine(Reach(adj, x, y));
    }
}
