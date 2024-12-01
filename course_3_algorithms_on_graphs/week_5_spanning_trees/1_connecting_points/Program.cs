/*

diff <(dotnet run <test/1) <(cat test/1.a)
diff <(dotnet run <test/2) <(cat test/2.a)

*/

using System;
using System.Collections.Generic;

public class Program
{
    private static double Distance(int x1, int y1, int x2, int y2)
    {
        return Math.Sqrt(Math.Pow(x1 - x2, 2) + Math.Pow(y1 - y2, 2));
    }

    private static double MinimumDistance(int[] x, int[] y)
    {
        int n = x.Length;

        // Stores the minimum distance to connect each point to the MST
        double[] minDist = new double[n];
        for (int i = 0; i < n; i++)
        {
            minDist[i] = double.MaxValue;
        }

        // Tracks which points are included in the MST
        bool[] used = new bool[n];

        // Start with the first point
        minDist[0] = 0;

        double result = 0;

        // Iterate n times to connect all points
        for (int i = 0; i < n; i++)
        {
            // Find the minimum distance point not yet used
            int v = -1;
            for (int j = 0; j < n; j++)
            {
                if (!used[j] && (v == -1 || minDist[j] < minDist[v]))
                {
                    v = j;
                }
            }

            // Add this point to the MST
            used[v] = true;
            if (minDist[v] != double.MaxValue)
            {
                result += minDist[v];
            }

            // Update minimum distances to other points
            for (int j = 0; j < n; j++)
            {
                if (!used[j])
                {
                    double dist = Distance(x[v], y[v], x[j], y[j]);
                    minDist[j] = Math.Min(minDist[j], dist);
                }
            }
        }

        return result;
    }

    public static void Main(string[] args)
    {
        int n = int.Parse(Console.ReadLine());
        int[] x = new int[n];
        int[] y = new int[n];
        for (int i = 0; i < n; i++)
        {
            string[] currLineInput = Console.ReadLine().Split(' ');
            x[i] = int.Parse(currLineInput[0]);
            y[i] = int.Parse(currLineInput[1]);
        }
        Console.WriteLine("{0:0.000000000}", MinimumDistance(x, y));
    }
}
