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
index  : 0  1 2 3 4
parents: 4 -1 4 1 1

List<int>[] adj:
root: 1
[0]
[1]: 3, 4
[2]
[3]
[4]: 0, 2

example we loop through the parents array with index
- if we found value -1, then the index 1 will be set to root
- we found value 1, then the indices 3, 4 will be push to index 1 linked list in
adj (indicate that these 2 will be child of 1)
- then we found value 4, then the indices 0, 2 will be push to index 4 linked
list in adj (indicate that these 2 will be child of 4)
*/

namespace TreeHeight
{
    class Program
    {
        // an array of Linked List type int
        private static List<int>[] adj { get; set; } = new List<int>[0];

        private static int DFSIterative(int root)
        {
            // stack will store pairs of (node, depth, childIndex), instead of
            // using recursion and depth first search we use a stack to prevent
            // stack over flow with input > 65000
            Stack<(int, int, int)> stack = new Stack<(int node, int depth, int childIndex)>();
            var maxDepth = 1;

            // push root node with depth 1 to the stack, childIndex 0 to count
            // and push all child in the linked list to the stack
            stack.Push((root, 1, 0));

            // while the stack still have node in it
            while (stack.Count > 0)
            {
                // extract value of node at the top of the stack
                var (node, depth, childIndex) = stack.Pop();
                // compare if the depth of that node greater that current maxDepth
                maxDepth = Math.Max(maxDepth, depth);

                // if that node have children, then process those too by pushing
                // them to the stack. All children of current node indicate in
                // the adj array linked lists
                if (childIndex < adj[node].Count)
                {
                    // push current node back with child index increase
                    stack.Push((node, depth, childIndex + 1));
                    // get the child of current node with childIndex in adj array linked lists
                    var child = adj[node][childIndex];
                    // push that child with depth + 1, index 0 to the stack
                    stack.Push((child, depth + 1, 0));
                }
            }

            // finish loop return maxDepth
            return maxDepth;
        }

        public static int TreeHeightCal(string inputN, string inputParents)
        {
            int n = int.Parse(inputN);
            // create an array of n input
            adj = new List<int>[n];
            // loop through each slot in array
            for (int i = 0; i < n; i++)
                // create a linked list of int
                adj[i] = new List<int>();

            // root will always be -1
            int root = -1;
            // split the inputParents string into array of int (length n)
            int[] parents = inputParents.Split(' ').Select(int.Parse).ToArray();

            for (int i = 0; i < n; i++)
            {
                // loop through each int in parents
                int parent = parents[i];
                // if the value is -1
                if (parent == -1)
                    // then the index will be set as root
                    root = i;
                // if value is not -1
                else
                    // then the value will be use as index in adj (List<int>[])
                    // then add the index to the array of children
                    adj[parent].Add(i);
            }

            // then after we built the tree, we call depth first search
            // interactive with root value 1
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
