using System;
using System.Collections.Generic;

/*
TODO: recall this problem
input:
5 5
1 1 1 1 1
3 5
2 4
1 4
5 4
5 3
output:
2
2
3
5
5
---
command to run tests in /tests dir
diff <(dotnet run <tests/116) <(cat tests/116.a)
*/


public class DisjointSetsElement
{
    public int Size { get; set; }
    public int Parent { get; set; }
    public int Rank { get; set; }

    public DisjointSetsElement(int size = 0, int parent = -1, int rank = 0)
    {
        Size = size;
        Parent = parent;
        Rank = rank;
    }
}

public class DisjointSets
{
    public int Size { get; set; }
    public int MaxTableSize { get; set; }
    public List<DisjointSetsElement> Sets { get; set; }

    public DisjointSets(int size)
    {
        Size = size;
        MaxTableSize = 0;
        Sets = new List<DisjointSetsElement>(size);
        for (int i = 0; i < size; i++)
        {
            Sets.Add(new DisjointSetsElement { Parent = i });
        }
    }

    public int GetParent(int table)
    {
        // find parent and compress path
        int i = table;
        if (i != Sets[i].Parent)
        {
            Sets[i].Parent = GetParent(Sets[i].Parent);
        }

        return Sets[i].Parent;
    }

    public void Merge(int destination, int source)
    {
        int realDestination = GetParent(destination);
        int realSource = GetParent(source);
        if (realDestination != realSource)
        {
            // merge two components
            // use union by rank heuristic
            // update max_table_size
            if (Sets[realSource].Rank > Sets[realDestination].Rank)
            {
                Sets[realDestination].Parent = realSource;
                Sets[realSource].Size += Sets[realDestination].Size;
                Sets[realDestination].Size = 0;
                MaxTableSize = Math.Max(MaxTableSize, Sets[realSource].Size);
            }
            else
            {
                Sets[realSource].Parent = realDestination;
                Sets[realDestination].Size += Sets[realSource].Size;
                Sets[realSource].Size = 0;
                MaxTableSize = Math.Max(MaxTableSize, Sets[realDestination].Size);

                if (Sets[realSource].Rank == Sets[realDestination].Rank)
                {
                    Sets[realDestination].Rank += 1;
                }
            }
        }
    }

    public void Input()
    {
        string[] input = (Console.ReadLine() ?? throw new Exception("Need input")).Split(' ');
        for (int i = 0; i < Size; ++i)
        {
            Sets[i].Size = int.Parse(input[i]);
            MaxTableSize = Math.Max(MaxTableSize, Sets[i].Size);
        }
    }
}

class MergingTables
{
    static void Main(string[] args)
    {
        int n,
            m;
        string[] input = (Console.ReadLine() ?? throw new Exception("Need input")).Split(' ');
        n = int.Parse(input[0]);
        m = int.Parse(input[1]);

        DisjointSets tables = new DisjointSets(n);

        tables.Input();

        for (int i = 0; i < m; i++)
        {
            input = (Console.ReadLine() ?? throw new Exception("WTF")).Split(' ');
            int destination = int.Parse(input[0]) - 1;
            int source = int.Parse(input[1]) - 1;

            tables.Merge(destination, source);
            Console.WriteLine(tables.MaxTableSize);
        }
    }
}
