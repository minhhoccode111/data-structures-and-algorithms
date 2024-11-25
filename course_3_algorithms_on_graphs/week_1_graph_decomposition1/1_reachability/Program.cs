using System;
using System.Collections.Generic;
using System.Linq;

public class Program
{
    public static int Reach(List<List<int>> adj, int x, int y)
    {
        // write your code here
        return 0;
    }

    public static void Main(string[] args)
    {
        // get first line
        string input = Console.ReadLine();
        int[] data = input.Split(' ').Select(int.Parse).ToArray();

        // first line, first <int> will be 'n', number of vertices
        int n = data[0];
        // first line, second <int> will be 'm', number of edges
        int m = data[1];

        // init a 2-D array with n cells to store list type <int>
        List<List<int>> adj = new List<List<int>>(n);
        // loop through each cell in the array
        for (int i = 0; i < n; i++)
        {
            // init a new list of <int>
            adj.Add(new List<int>());
        }

        // loop from 0 to m
        for (int i = 0; i < m; i++)
        {
            //
            int a = data[2 * i + 2] - 1;
            int b = data[2 * i + 3] - 1;
            adj[a].Add(b);
            adj[b].Add(a);
        }

        int x = data[2 * m + 2] - 1;
        int y = data[2 * m + 3] - 1;

        Console.WriteLine(Reach(adj, x, y));
    }
}
