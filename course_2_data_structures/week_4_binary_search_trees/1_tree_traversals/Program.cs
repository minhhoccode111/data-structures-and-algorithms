using System;
using System.Collections.Generic;
using System.Linq;

/*
my small test cases:
diff -b <(dotnet run <test/1) <(cat test/1.a)
diff -b <(dotnet run <test/2) <(cat test/2.a)

course's test cases:
diff -b <(dotnet run <tests/21) <(cat tests/21.a)
*/

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

    // left, right is actually index point back to key
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

    // LNR
    public List<int> InOrder()
    {
        result = new List<int>();
        InOrder(0, result);
        return result;
    }

    private void InOrder(int rootIndex, List<int> resultList)
    {
        if (rootIndex == -1)
        {
            return;
        }
        InOrder(left[rootIndex], resultList);
        resultList.Add(key[rootIndex]);
        InOrder(right[rootIndex], resultList);
    }

    // NLR
    public List<int> PreOrder()
    {
        result = new List<int>();
        PreOrder(0, result);
        return result;
    }

    private void PreOrder(int rootIndex, List<int> resultList)
    {
        if (rootIndex == -1)
        {
            return;
        }
        resultList.Add(key[rootIndex]);
        PreOrder(left[rootIndex], resultList);
        PreOrder(right[rootIndex], resultList);
    }

    // LRN
    public List<int> PostOrder()
    {
        result = new List<int>();
        PostOrder(0, result);
        return result;
    }

    private void PostOrder(int rootIndex, List<int> resultList)
    {
        if (rootIndex == -1)
        {
            return;
        }
        PostOrder(left[rootIndex], resultList);
        PostOrder(right[rootIndex], resultList);
        resultList.Add(key[rootIndex]);
    }
}
