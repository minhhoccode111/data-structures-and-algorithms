using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main()
    {
        TreeOrders tree = new TreeOrders();
        tree.Read();
        Console.WriteLine(string.Join(" ", tree.InOrder()));
        Console.WriteLine(string.Join(" ", tree.PreOrder()));
        Console.WriteLine(string.Join(" ", tree.PostOrder()));
    }
}

class TreeOrders
{
    private int n;
    private int[] key;
    private int[] left;
    private int[] right;
    private List<int> result;

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

    public List<int> InOrder()
    {
        result = new List<int>();
        // Implement in-order traversal here
        return result;
    }

    public List<int> PreOrder()
    {
        result = new List<int>();
        // Implement pre-order traversal here
        return result;
    }

    public List<int> PostOrder()
    {
        result = new List<int>();
        // Implement post-order traversal here
        return result;
    }
}
