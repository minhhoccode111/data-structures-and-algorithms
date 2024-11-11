using System;
using System.Collections.Generic;

/*
input:
5
4 -1 4 1 1
output:
3

tree:
root
  |
  v
  1
 / \
3   4
   / \
  0   2

explain:
0  1 2 3 4
4 -1 4 1 1

*/

namespace TreeHeight
{
    class Program
    {
        static List<int>[] adj;

        static int DFS(int r)
        {
            if (adj[r].Count == 0)
                return 1;

            int maxDepth = 0;
            foreach (int child in adj[r])
            {
                maxDepth = Math.Max(maxDepth, DFS(child));
            }

            return 1 + maxDepth;
        }

        static void Main()
        {
            int n = int.Parse(Console.ReadLine());
            adj = new List<int>[n];

            for (int i = 0; i < n; i++)
                adj[i] = new List<int>();

            int root = -1;
            string[] parents = Console.ReadLine().Split();

            for (int i = 0; i < n; i++)
            {
                int parent = int.Parse(parents[i]);
                if (parent == -1)
                    root = i;
                else
                    adj[parent].Add(i);
            }

            Console.WriteLine(DFS(root));
        }
    }
}
