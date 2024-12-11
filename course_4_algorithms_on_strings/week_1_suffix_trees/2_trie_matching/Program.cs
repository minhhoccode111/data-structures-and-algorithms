/*

diff <(dotnet run < test/1) <(cat test/1.a)
diff <(dotnet run < test/2) <(cat test/2.a)
diff <(dotnet run < test/3) <(cat test/3.a)

*/

using System;
using System.Collections.Generic;
using System.Linq;

namespace trie_matching
{
    class Program
    {
        static void Main(string[] args)
        {
            string text = Console.ReadLine();
            int n = int.Parse(Console.ReadLine());
            List<string> patterns = new List<string>();
            for (int i = 0; i < n; i++)
            {
                string s = Console.ReadLine();
                patterns.Add(s);
            }

            List<int> answers = Solve(text, patterns);
            string answersLine = string.Join(" ", answers);
            Console.WriteLine(answersLine);
        }

        static List<int> Solve(string text, List<string> patterns)
        {
            List<int> ans = new List<int>();

            // Build the trie from patterns
            var trie = BuildTrie(patterns);

            // Match patterns in the text using the trie
            for (int i = 0; i < text.Length; i++)
            {
                if (TrieMatching(text, i, trie))
                {
                    ans.Add(i);
                }
            }

            return ans;
        }

        static List<Dictionary<char, int>> BuildTrie(List<string> patterns)
        {
            var trie = new List<Dictionary<char, int>> { new Dictionary<char, int>() };
            int nodeCount = 0;

            foreach (var pattern in patterns)
            {
                int currentNode = 0;
                foreach (char symbol in pattern)
                {
                    if (!trie[currentNode].ContainsKey(symbol))
                    {
                        trie.Add(new Dictionary<char, int>());
                        trie[currentNode][symbol] = ++nodeCount;
                    }
                    currentNode = trie[currentNode][symbol];
                }
            }

            return trie;
        }

        static bool TrieMatching(string text, int startPos, List<Dictionary<char, int>> trie)
        {
            int currentNode = 0;
            for (int i = startPos; i < text.Length; i++)
            {
                char currentSymbol = text[i];

                if (trie[currentNode].ContainsKey(currentSymbol))
                {
                    currentNode = trie[currentNode][currentSymbol];

                    // Check if we are at a leaf node (no outgoing edges)
                    if (trie[currentNode].Count == 0)
                    {
                        return true;
                    }
                }
                else
                {
                    return false;
                }
            }

            return false;
        }
    }
}
