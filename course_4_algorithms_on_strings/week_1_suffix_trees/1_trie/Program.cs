/*

diff <(dotnet run < test/1) <(cat test/1.a)
diff <(dotnet run < test/2) <(cat test/2.a)
diff <(dotnet run < test/3) <(cat test/3.a)

*/


using System;
using System.Collections.Generic;

class Program
{
    static List<Dictionary<char, int>> BuildTrie(List<string> patterns)
    {
        if (patterns.Count == 0)
            return new List<Dictionary<char, int>>();

        var trie = new List<Dictionary<char, int>> { new Dictionary<char, int>() };
        int root = 0,
            count = 0;

        foreach (var pattern in patterns)
        {
            int current = root;
            foreach (char c in pattern)
            {
                if (trie[current].ContainsKey(c))
                {
                    current = trie[current][c];
                }
                else
                {
                    trie.Add(new Dictionary<char, int>());
                    trie[current][c] = ++count;
                    current = count;
                }
            }
        }

        return trie;
    }

    static void Main(string[] args)
    {
        int n = int.Parse(Console.ReadLine());
        List<string> patterns = new List<string>();
        for (int i = 0; i < n; i++)
        {
            string s = Console.ReadLine();
            patterns.Add(s);
        }

        var trie = BuildTrie(patterns);
        for (int i = 0; i < trie.Count; i++)
        {
            foreach (var kvp in trie[i])
            {
                Console.WriteLine($"{i}->{kvp.Value}:{kvp.Key}");
            }
        }
    }
}
