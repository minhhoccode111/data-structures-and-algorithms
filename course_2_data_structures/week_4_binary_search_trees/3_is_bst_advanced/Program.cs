using System;
using System.Collections.Generic;
using System.Collections.Generic;
using System.Linq;
using System.Linq;

/*
my small test cases:

diff -b <(dotnet run <test/1) <(cat test/1.a)
diff -b <(dotnet run <test/2) <(cat test/2.a)
diff -b <(dotnet run <test/3) <(cat test/3.a)
diff -b <(dotnet run <test/4) <(cat test/4.a)
diff -b <(dotnet run <test/5) <(cat test/5.a)
diff -b <(dotnet run <test/6) <(cat test/6.a)
diff -b <(dotnet run <test/7) <(cat test/7.a)
diff -b <(dotnet run <test/8) <(cat test/8.a)

integer overflow: where?
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
    private int _n;
    private long[] _key;
    private int[] _left;
    private int[] _right;

    public void Read()
    {
        _n = int.Parse(Console.ReadLine());
        _key = new long[_n];
        _left = new int[_n];
        _right = new int[_n];

        for (int i = 0; i < _n; i++)
        {
            string[] values = Console.ReadLine().Split(' ');
            if (values.Length != 3)
            {
                throw new FormatException("Each line must contain exactly three values");
            }

            _key[i] = long.Parse(values[0]);
            _left[i] = int.Parse(values[1]);
            _right[i] = int.Parse(values[2]);

            // Validate that child indices are within bounds
            if ((_left[i] >= _n && _left[i] != -1) || (_right[i] >= _n && _right[i] != -1))
            {
                throw new ArgumentException("Child index out of bounds");
            }
        }
    }

    public bool IsBinarySearchTrees()
    {
        if (_n == 0)
            return true;

        try
        {
            return IsBinarySearchTrees(0, long.MinValue, long.MaxValue);
        }
        catch (Exception)
        {
            return false;
        }
    }

    private bool IsBinarySearchTrees(int rootIndex, long minValue, long maxValue)
    {
        if (rootIndex == -1)
            return true;

        long root = _key[rootIndex];
        int leftIndex = _left[rootIndex];
        int rightIndex = _right[rootIndex];

        // Check if current node's value is within the allowed range
        if (root < minValue || root >= maxValue)
            return false;

        // Recursively check left and right subtrees
        return IsBinarySearchTrees(leftIndex, minValue, root)
            && IsBinarySearchTrees(rightIndex, root, maxValue);
    }
}

