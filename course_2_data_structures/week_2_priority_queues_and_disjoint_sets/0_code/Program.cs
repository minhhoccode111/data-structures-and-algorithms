using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Hello, World!");
    }
}

public class QuickFindUF
{
    private int[] id;

    public QuickFindUF(int N)
    {
        id = new int[N];
        // set id of each object to itself
        // N array accesses
        for (int i = 0; i < N; i++)
            id[i] = i;
    }

    public bool connected(int p, int q)
    {
        // check whether p and q are in the same component
        // 2 array accesses
        return id[p] == id[q];
    }

    public void union(int p, int q)
    {
        int pid = id[p];
        int qid = id[q];
        for (int i = 0; i < id.Length; i++)
            // change all entries with id[p] to id[q]
            // at most 2N + 2 array accesses
            if (id[i] == pid)
                id[i] = qid;
    }
}

// quick-union
public class QuickUnionUF
{
    private int[] id;

    public QuickUnionUF(int N)
    {
        id = new int[N];
        // set id of each object to itself
        // N array accesses
        for (int i = 0; i < N; i++)
            id[i] = i;
    }

    private int root(int i)
    {
        // chase parent pointer until reach root
        // depth of i array accesses
        while (i != id[i])
            i = id[i];
        return i;
    }

    public bool connected(int p, int q)
    {
        // check if p and q have the same root
        // depth of p and q array accesses
        return root(p) == root(q);
    }

    public void union(int p, int q)
    {
        // change root of p to point to root of q
        // depth of p and q array accesses
        int i = root(p);
        int j = root(q);
        id[i] = j;
    }
}

// weighted quick-union
public class WeightedQuickUnionUF
{
    private int[] id;

    // same as quick-union but maintain extra array sz[i] to count number of objects in the tree rooted at i
    private int[] sz;

    public WeightedQuickUnionUF(int N)
    {
        id = new int[N];
        // set id of each object to itself
        // N array accesses
        for (int i = 0; i < N; i++)
            id[i] = i;
    }

    private int root(int i)
    {
        // chase parent pointer until reach root
        // depth of i array accesses
        while (i != id[i])
            i = id[i];
        return i;
    }

    // or Find
    public bool connected(int p, int q)
    {
        // check if p and q have the same root
        // depth of p and q array accesses
        return root(p) == root(q);
    }

    public void union(int p, int q)
    {
        // modify quick-union to
        // link root of smaller tree to root of larger tree
        // update the sz[] array
        int i = root(p);
        int j = root(q);
        if (i == j)
            return;
        if (sz[i] < sz[j])
        {
            id[i] = j;
            sz[j] += sz[i];
        }
        else
        {
            id[j] = i;
            sz[i] += sz[j];
        }
    }
}

public class PathCompression
{
    private int[] id;

    // similar to above
    // ...
    // but the root method

    private int root(int i)
    {
        while (i != id[i])
        {
            id[i] = id[id[i]]; // only one extra line of code
            i = id[i];
        }
        return i;
    }
}
