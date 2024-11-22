using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Hello, World!");
    }
}

class HashTable
{
    // TODO:
}

class ListNode
{
    // TODO:
}

class SearchSubstringRabinKarp
{
    private long patHash; // pattern hash value
    private int M; // pattern length
    private long Q; // modulus
    private int R; // radix
    private long RM; // R^(M-1)%Q

    public SearchSubstringRabinKarp(string pat)
    {
        M = pat.Length;
        R = 256;
        Q = longRandomPrime(); // a large prime (but avoid overflow)

        RM = 1; // precomputer R^(M-1) (mod Q)
        for (int i = 1; i <= M - 1; i++)
        {
            RM = (R * RM) % Q;
        }
        patHash = hash(pat, M);
    }

    private long longRandomPrime()
    {
        // NOTE: can enhance this
        return 997;
    }

    // compute hash for M-digit key
    private long hash(string key, int M)
    {
        long h = 0;
        for (int j = 0; j < M; j++)
        {
            h = (R * h + key[j]) % Q;
        }
        return h;
    }

    //
    public int search(string txt)
    {
        // check for hash collision using rolling hash function
        int N = txt.Length;
        long txtHash = hash(txt, M);
        if (patHash == txtHash)
            return 0;
        for (int i = M; i < N; i++)
        {
            txtHash = (txtHash + Q - RM * txt[i - M] % Q) % Q;
            txtHash = (txtHash * R + txt[i] % Q);
            if (patHash == txtHash)
                return i - M + 1;
        }
        return N;
    }
}
