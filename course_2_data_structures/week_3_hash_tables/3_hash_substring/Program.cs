using System;
using System.Collections.Generic;

/*
TODO: recall this

diff -b <(dotnet run <tests/06) <(cat tests/06.a)

*/

public class HashSubstring
{
    private const long P = 1299709; // Prime number for hashing
    private const long X = 23; // Multiplier for hashing

    public static long Hash(string s, long p, long x)
    {
        long hash = 0;
        for (int i = s.Length - 1; i >= 0; --i)
        {
            hash = (hash * x + s[i]) % p;
        }
        return hash;
    }

    public static List<long> ComputeHashes(string text, int patternSize, long p, long x)
    {
        int size = text.Length - patternSize + 1;
        var hashes = new List<long>(new long[size]);
        string lastSubstring = text.Substring(size - 1, patternSize);
        hashes[size - 1] = Hash(lastSubstring, p, x);

        long xToPatternSize = 1;
        for (int i = 1; i <= patternSize; ++i)
        {
            xToPatternSize = (xToPatternSize * x) % p;
        }

        for (int k = size - 2; k >= 0; --k)
        {
            hashes[k] = (x * hashes[k + 1] + text[k] - text[k + patternSize] * xToPatternSize) % p;
            if (hashes[k] < 0)
            {
                hashes[k] = (hashes[k] + p) % p;
            }
        }

        return hashes;
    }

    public static List<int> RabinKarp(string pattern, string text)
    {
        int patternSize = pattern.Length;
        long patternHash = Hash(pattern, P, X);
        var hashes = ComputeHashes(text, patternSize, P, X);

        var indexes = new List<int>();
        for (int idx = 0; idx < hashes.Count; ++idx)
        {
            if (hashes[idx] == patternHash)
            {
                string substring = text.Substring(idx, patternSize);
                if (substring == pattern)
                {
                    indexes.Add(idx);
                }
            }
        }

        return indexes;
    }

    public static List<int> NaiveMatching(string pattern, string text)
    {
        var ans = new List<int>();
        for (int i = 0; i + pattern.Length <= text.Length; ++i)
        {
            if (text.Substring(i, pattern.Length) == pattern)
            {
                ans.Add(i);
            }
        }
        return ans;
    }

    public static void Display<T>(IEnumerable<T> vector)
    {
        foreach (var v in vector)
        {
            Console.Write(v + " ");
        }
        Console.WriteLine();
    }

    public static bool TestSolution(string pattern, string text)
    {
        var positions = RabinKarp(pattern, text);
        var positionsNaive = NaiveMatching(pattern, text);

        Console.Write("Rabin-Karp: ");
        Display(positions);
        Console.Write("Naive: ");
        Display(positionsNaive);

        bool correct =
            positions.Count == positionsNaive.Count
            && positions.TrueForAll(positionsNaive.Contains);
        if (correct)
        {
            Console.WriteLine("OK!");
        }
        else
        {
            Console.WriteLine("FAIL!");
            Console.WriteLine($"Pattern: {pattern}");
            Console.WriteLine($"Text: {text}");
        }
        return correct;
    }

    public static void Main(string[] args)
    {
        string pattern = Console.ReadLine() ?? string.Empty;
        string text = Console.ReadLine() ?? string.Empty;

        var positions = RabinKarp(pattern, text);
        Display(positions);

        // Uncomment the line below to run a test case
        // TestSolution(pattern, text);
    }
}
