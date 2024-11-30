/*

diff <(dotnet run <test/1) <(cat test/1.a)

*/

using System;
using System.Collections.Generic;
using System.Linq;

public class NegativeCycle
{
    private static int negativeCycle(List<int>[] adj, List<int>[] cost)
    {
        int n = adj.Length;
        long[] dist = new long[n];

        for (int start = 0; start < n; start++)
        {
            Array.Fill(dist, int.MaxValue);
            dist[start] = 0;

            for (int i = 0; i < n - 1; i++)
            {
                bool relaxed = false;
                for (int u = 0; u < n; u++)
                {
                    if (dist[u] == int.MaxValue)
                        continue;

                    for (int j = 0; j < adj[u].Count; j++)
                    {
                        int v = adj[u][j];
                        long newDist = dist[u] + cost[u][j];

                        if (newDist < dist[v])
                        {
                            dist[v] = newDist;
                            relaxed = true;
                        }
                    }
                }

                if (!relaxed)
                    break;
            }

            for (int u = 0; u < n; u++)
            {
                if (dist[u] == int.MaxValue)
                    continue;

                for (int j = 0; j < adj[u].Count; j++)
                {
                    int v = adj[u][j];
                    long newDist = dist[u] + cost[u][j];

                    if (newDist < dist[v])
                    {
                        return 1;
                    }
                }
            }
        }

        return 0;
    }

    public static void Main(string[] args)
    {
        string[] firstLineInput = Console.ReadLine().Split(' ');
        int vertices = int.Parse(firstLineInput[0]);
        int edges = int.Parse(firstLineInput[1]);

        List<int>[] adj = new List<int>[vertices];
        List<int>[] cost = new List<int>[vertices];

        for (int i = 0; i < vertices; i++)
        {
            adj[i] = new List<int>();
            cost[i] = new List<int>();
        }

        for (int i = 0; i < edges; i++)
        {
            string[] currLineInput = Console.ReadLine().Split(' ');
            int currX = int.Parse(currLineInput[0]);
            int currY = int.Parse(currLineInput[1]);
            int currW = int.Parse(currLineInput[2]);

            adj[currX - 1].Add(currY - 1);
            cost[currX - 1].Add(currW);
        }

        Console.WriteLine(negativeCycle(adj, cost));
    }
}
