/*

diff <(dotnet run <test/1) <(cat test/1.a)
diff <(dotnet run <test/2) <(cat test/2.a)

*/

using System;
using System.Collections.Generic;

public class BFS
{
    private static int Distance(List<int>[] adj, int s, int t)
    {
        // bfs starting at node s
        int[] dist = new int[adj.Length];
        // initialize distances to "infinity"
        for (int i = 0; i < dist.Length; i++)
        {
            dist[i] = -1;
        }
        dist[s] = 0;

        // queue of nodes to be processed, heart of bfs algorithm
        Queue<int> q = new Queue<int>();
        q.Enqueue(s);

        while (q.Count > 0)
        {
            int curr = q.Dequeue();
            // add unprocessed nodes to the queue
            foreach (int n in adj[curr])
            {
                if (dist[n] == -1)
                {
                    q.Enqueue(n);
                    // set distance of node
                    dist[n] = dist[curr] + 1;
                }
            }
        }

        return dist[t];
    }

    public static void Main(string[] args)
    {
        string[] firstLineInput = Console.ReadLine().Split(' ');

        int vertices = int.Parse(firstLineInput[0]);
        int edges = int.Parse(firstLineInput[1]);

        List<int>[] adj = new List<int>[vertices];

        for (int i = 0; i < vertices; i++)
        {
            adj[i] = new List<int>();
        }

        for (int i = 0; i < edges; i++)
        {
            string[] currLineInput = Console.ReadLine().Split(' ');
            int currX = int.Parse(currLineInput[0]);
            int currY = int.Parse(currLineInput[1]);

            adj[currX - 1].Add(currY - 1);
            adj[currY - 1].Add(currX - 1);
        }

        string[] lastLineInput = Console.ReadLine().Split(' ');
        int x = int.Parse(lastLineInput[0]);
        int y = int.Parse(lastLineInput[1]);

        Console.WriteLine(Distance(adj, x - 1, y - 1));
    }
}
