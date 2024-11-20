// starter file convert from Java to C#
using System;
using System.Diagnostics;
using System.Linq;
using System.Reflection;

/*
2 5
1 2 3 4 5
---
0 1
---
0 0 | 1
1 0 | 2
0 1 | 3
1 2 | 4
0 4 | 5

run tests in /tests dir
diff <(dotnet run <tests/02) <(cat tests/02.a)
diff <(dotnet run <tests/08) <(cat tests/08.a)
*/

class JobQueue
{
    static int NumThreads;
    static int NumJobs;
    static int[] Jobs;

    // min-heap priority queue to decide which process will run current job
    static Thread[] Threads;

    static void Main(string[] args)
    {
        ReadData();
        AssignJobs();
        // Console.WriteLine("Hello, World!");
    }

    static void ReadData()
    {
        // first line input
        int[] inputFirstLine = (Console.ReadLine() ?? throw new Exception("Need input n"))
            .Split(' ')
            .Select(int.Parse)
            .ToArray();

        NumThreads = inputFirstLine[0];

        NumJobs = inputFirstLine[1];

        Threads = new Thread[NumThreads];

        // create min-heap priority queue default wait time 0
        for (int i = 0; i < NumThreads; i++)
        {
            Threads[i] = new Thread(i, 0);
        }

        // second line input
        Jobs = (Console.ReadLine() ?? throw new Exception("Need input data"))
            .Split(' ')
            .Select(int.Parse)
            .ToArray();

        if (Jobs.Length != NumJobs)
            throw new Exception("Number of jobs not match");
    }

    static void AssignJobs()
    {
        for (int i = 0; i < NumJobs; i++)
        {
            long job = Jobs[i];
            Console.WriteLine($"{Threads[0].Index} {Threads[0].WaitTime}");
            Threads[0].WaitTime += job;
            SiftDown(0);
        }
    }

    static int Parent(int i) => (i - 1) / 2;

    static int Left(int i) => i * 2 + 1;

    static int Right(int i) => i * 2 + 2;

    static void SiftDown(int i)
    {
        int l = Left(i);
        int r = Right(i);

        int min = i;

        int len = Threads.Length;

        if (
            l < len
            && (
                (Threads[l].WaitTime < Threads[min].WaitTime)
                || (
                    // if wait time is equal
                    Threads[l].WaitTime == Threads[min].WaitTime
                    // then we also have to check for thread's index
                    && Threads[l].Index < Threads[min].Index
                )
            )
        )
        {
            min = l;
        }
        if (
            r < len
            && (
                (Threads[r].WaitTime < Threads[min].WaitTime)
                || (
                    // if wait time is equal
                    Threads[r].WaitTime == Threads[min].WaitTime
                    // then we also have to check for thread's index
                    && Threads[r].Index < Threads[min].Index
                )
            )
        )
        {
            min = r;
        }
        if (i != min)
        {
            var tmp = Threads[min];
            Threads[min] = Threads[i];
            Threads[i] = tmp;
            SiftDown(min);
        }
    }

    class Thread
    {
        public int Index { get; set; }
        public long WaitTime { get; set; }

        public Thread(int index, long waitTime = 0)
        {
            Index = index;
            WaitTime = waitTime;
        }
    }
}
