using System;
using System.Collections.Generic;
using System.Linq;

/*
my small test cases:
diff -b <(dotnet run <test/1) <(cat test/1.a)
diff -b <(dotnet run <test/2) <(cat test/2.a)
diff -b <(dotnet run <test/3) <(cat test/3.a)
diff -b <(dotnet run <test/4) <(cat test/4.a)
diff -b <(dotnet run <test/5) <(cat test/5.a)
diff -b <(dotnet run <test/6) <(cat test/6.a)
*/

class Program
{
    static void Main()
    {
        TreeOrders tree = new TreeOrders();
        tree.Read();
        Console.WriteLine(tree.IsBinarySearchTrees() ? "CORRECT" : "INCORRECT");
    }
}

class TreeOrders
{
    private int n;
    private int[] key;

    // left, right is actually index point back to key
    private int[] left;
    private int[] right;

    public void Read()
    {
        n = int.Parse(Console.ReadLine());
        key = new int[n];
        left = new int[n];
        right = new int[n];

        for (int i = 0; i < n; i++)
        {
            int[] values = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();

            key[i] = values[0];
            left[i] = values[1];
            right[i] = values[2];
        }
    }

    public bool IsBinarySearchTrees()
    {
        // empty tree is considered correct
        if (n == 0)
        {
            return true;
        }
        return IsBinarySearchTrees(0, int.MinValue, int.MaxValue);
    }

    private bool IsBinarySearchTrees(int rootIndex, int minValue, int maxValue)
    {
        if (rootIndex == -1)
            return true;

        int root = key[rootIndex];
        int leftIndex = left[rootIndex];
        int rightIndex = right[rootIndex];

        // return false if minValue less than root or maxValue greater than root
        if (minValue > root || maxValue < root)
            return false;

        // new root as maxValue for left tree and
        // new root as minValue for right tree
        return IsBinarySearchTrees(leftIndex, minValue, root)
            && IsBinarySearchTrees(rightIndex, root, maxValue);
    }
}
