/*

diff <(dotnet run <test/1) <(cat test/1.a)
diff <(dotnet run <test/2) <(cat test/2.a)

*/

using System;
using System.Collections.Generic;
using System.Collections.Generic;

public class Acyclicity
{

    private static bool Explore(int node, List<int>[] adj, bool[] visited, bool[] path)
    {
        visited[node] = true;
        path[node] = true;

        foreach (int neighbor in adj[node])
        {
            if (path[neighbor])
            {
                return true;
            }

            if (!visited[neighbor])
            {
                // recursive call to explore neighbors
                if (Explore(neighbor, adj, visited, path))
                {
                    return true;
                }
            }
        }

        path[node] = false;
        return false;
    }

    private static bool IsCycle(List<int>[] adj)
    {
        bool[] visited = new bool[adj.Length];
        bool[] path = new bool[adj.Length];

        for (int i = 0; i < adj.Length; i++)
        {
            if (!visited[i])
            {
                if (Explore(i, adj, visited, path))
                {
                    return true;
                }
            }
        }

        return false;
    }

    public static void Main(string[] args)
    {
        // first line input indicate vertices and edges
        string[] firstLineInput = Console.ReadLine().Split(' ');
        int vertices = int.Parse(firstLineInput[0]);
        int edges = int.Parse(firstLineInput[1]);
        List<int>[] adjacencyList = new List<int>[vertices];

        // init list of each vertex to store neighbors
        for (int i = 0; i < vertices; i++)
        {
            adjacencyList[i] = new List<int>();
        }

        // loop through each edge to identify neighbors
        for (int i = 0; i < edges; i++)
        {
            string[] currentLineInput = Console.ReadLine().Split(' ');
            int x = int.Parse(currentLineInput[0]);
            int y = int.Parse(currentLineInput[1]);
            adjacencyList[x - 1].Add(y - 1);
        }

        // print 1 if there is a cycle
        if (IsCycle(adjacencyList))
        {
            Console.WriteLine(1);
        }
        // else print 0
        else
        {
            Console.WriteLine(0);
        }
    }
}
