using System;
using System.Collections.Generic;

/*

diff <(dotnet run <test/1) <(cat test/1.a)
diff <(dotnet run <test/2) <(cat test/2.a)

*/

public class Acyclicity
{
    private static int Acyclic(List<int>[] adj)
    {
        throw new Exception("Not implemented yet");
    }

    public static void Main(string[] args)
    {
        string[] firstLineInput = Console.ReadLine().Split(' ');
        int vertices = int.Parse(firstLineInput[0]);
        int edges = int.Parse(firstLineInput[1]);
        List<int>[] adjacencyList = new List<int>[vertices];

        for(int i = 0; i < vertices; i++)
        {
            adjacencyList[i] = new List<int>();
        }

        for (int i = 0; i < edges; i++)
        {
            string[] currentLineInput = Console.ReadLine().Split(' ');
            int x = int.Parse(currentLineInput[0]);
            int y = int.Parse(currentLineInput[1]);
            adjacencyList[x - 1].Add(y - 1);
        }

        Console.WriteLine(Acyclic(adjacencyList));

    }

}
