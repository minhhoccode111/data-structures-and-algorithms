/*

diff <(dotnet run <test/1) <(cat test/1.a)
diff <(dotnet run <test/3) <(cat test/3.a)

*/

using System;
using System.Collections.Generic;

public class Program
{
    private static List<int> Toposort(List<int>[] adj)
    {
        int[] used = new int[adj.Length];
        List<int> order = new List<int>();
        Stack<int> ordering = new Stack<int>();

        for (int node = 0; node < adj.Length; node++)
        {
            if (used[node] == 0)
            {
                dfs(adj, used, ordering, node);
            }
        }

        while (ordering.Count > 0)
        {
            order.Add(ordering.Pop() + 1);
        }

        return order;
    }

    private static void dfs(List<int>[] adj, int[] used, Stack<int> ordering, int s)
    {
        used[s] = 1;
        foreach (int neighbor in adj[s])
        {
            if (used[neighbor] == 0)
            {
                dfs(adj, used, ordering, neighbor);
            }
        }
        ordering.Push(s);
    }

    public static void Main(string[] args)
    {
        string[] firstLineInput = Console.ReadLine().Split(' ');
        int vertices = int.Parse(firstLineInput[0]);
        int edges = int.Parse(firstLineInput[1]);
        List<int>[] adjacencyList = new List<int>[vertices];

        for (int i = 0; i < vertices; i++)
        {
            adjacencyList[i] = new List<int>();
        }

        for (int i = 0; i < edges; i++)
        {
            string[] currentLineInput = Console.ReadLine().Split(' ');
            int x = int.Parse(currentLineInput[0]);
            int y = int.Parse(currentLineInput[1]);
            adjacencyList[x - 1].Add(y - 1);
        }

        List<int> order = Toposort(adjacencyList);

        Console.WriteLine(string.Join(' ', order));
    }
}
