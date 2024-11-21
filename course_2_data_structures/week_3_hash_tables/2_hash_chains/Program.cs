using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

/*
-b: flag to ignore whitespace
test/ dir: my local test files dir
tests/ dir: the course's test files dir (really large files, so i added to .gitignore)

diff -b <(dotnet run <test/01) <(cat test/01.a)
diff -b <(dotnet run <test/02) <(cat test/02.a)

diff -b <(dotnet run <tests/06) <(cat tests/06.a)
*/

public class HashChains
{
    private static int NumBuckets;
    private static List<List<string>> HashMap;
    private const long P = 1000000007;
    private const long X = 263;

    public static long HashFunction(string s)
    {
        long hash = 0;
        for (int i = s.Length - 1; i >= 0; --i)
        {
            hash = (hash * X + s[i]) % P;
        }
        return hash % NumBuckets;
    }

    public static void Solve()
    {
        NumBuckets = int.Parse(Console.ReadLine() ?? throw new Exception("Bucket count required"));
        int numQueries = int.Parse(
            Console.ReadLine() ?? throw new Exception("Number of queries required")
        );

        HashMap = new List<List<string>>(NumBuckets);
        for (int i = 0; i < NumBuckets; i++)
        {
            HashMap.Add(new List<string>());
        }

        for (int i = 0; i < numQueries; i++)
        {
            string[] query = (Console.ReadLine() ?? throw new Exception("Query required")).Split(
                ' '
            );

            if (query[0] == "check")
            {
                int index = int.Parse(query[1]);
                Console.WriteLine(HashMap[index].Count > 0 ? string.Join(" ", HashMap[index]) : "");
            }
            else
            {
                string value = query[1];
                int hash = (int)HashFunction(value);
                if (query[0] == "find")
                {
                    Console.WriteLine(HashMap[hash].Contains(value) ? "yes" : "no");
                }
                else if (query[0] == "add")
                {
                    if (!HashMap[hash].Contains(value))
                    {
                        HashMap[hash].Insert(0, value); // Add to the front for "check" order
                    }
                }
                else if (query[0] == "del")
                {
                    if (HashMap[hash].Contains(value))
                    {
                        HashMap[hash].Remove(value);
                    }
                }
            }
        }
    }

    public static void Main(string[] args)
    {
        Solve();
    }
}
