using System;
using System.Collections.Generic;
using System.Linq;

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

        static int DFSIterative(int root)
        {
            // Stack will store pairs of (node, depth)
            var stack = new Stack<(int node, int depth, int childIndex)>();
            var maxDepth = 1;

            // Push root node with depth 1
            stack.Push((root, 1, 0));

            while (stack.Count > 0)
            {
                var (node, depth, childIndex) = stack.Pop();
                maxDepth = Math.Max(maxDepth, depth);

                // If we have more children to process
                if (childIndex < adj[node].Count)
                {
                    // Push current node back with next child index
                    stack.Push((node, depth, childIndex + 1));
                    // Push the child
                    var child = adj[node][childIndex];
                    stack.Push((child, depth + 1, 0));
                }
            }

            return maxDepth;
        }

        public static int TreeHeightCal(string inputN, string inputParents)
        {
            int n = int.Parse(inputN);
            adj = new List<int>[n];
            for (int i = 0; i < n; i++)
                adj[i] = new List<int>();

            int root = -1;
            int[] parents = inputParents.Split(' ').Select(int.Parse).ToArray();

            for (int i = 0; i < n; i++)
            {
                int parent = parents[i];
                if (parent == -1)
                    root = i;
                else
                    adj[parent].Add(i);
            }

            return DFSIterative(root);
        }

        static void Main(string[] args)
        {
            if (args is not null)
            {
                Tests.Tests.Run();
                return;
            }

            string n = Console.ReadLine() ?? throw new ArgumentNullException("Need input 'n'");
            string parents =
                Console.ReadLine() ?? throw new ArgumentNullException("Need input 'parents'");

            Console.WriteLine(TreeHeightCal(n, parents));
        }
    }
}
