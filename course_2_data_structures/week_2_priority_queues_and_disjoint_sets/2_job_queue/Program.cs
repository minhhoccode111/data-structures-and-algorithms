// starter file convert from Java to C#
using System;
using System.Diagnostics;
using System.Reflection;

class JobQueue
{
    static int numWorkers;
    static int[] jobs;

    static int[] assignedWorker;
    static long[] startTime;

    static void Main(string[] args)
    {
        // if (args != null)
        // {
        //     Test();
        //     return;
        // }

        Solve();
    }

    static void ReadData()
    {
        string[] input = (Console.ReadLine() ?? throw new Exception("need 'input'")).Split(' ');
        numWorkers = int.Parse(input[0]);
        int m = int.Parse(input[1]);
        jobs = new int[m];
        for (int i = 0; i < m; ++i)
        {
            jobs[i] = int.Parse(Console.ReadLine() ?? throw new Exception("need 'jobs'"));
        }
    }

    static void WriteResponse()
    {
        for (int i = 0; i < jobs.Length; ++i)
        {
            Console.WriteLine($"{assignedWorker[i]} {startTime[i]}");
        }
    }

    static void AssignJobs()
    {
        // TODO: replace this code with a faster algorithm.
        assignedWorker = new int[jobs.Length];
        startTime = new long[jobs.Length];
        long[] nextFreeTime = new long[numWorkers];
        for (int i = 0; i < jobs.Length; i++)
        {
            int duration = jobs[i];
            int bestWorker = 0;
            for (int j = 0; j < numWorkers; ++j)
            {
                if (nextFreeTime[j] < nextFreeTime[bestWorker])
                    bestWorker = j;
            }
            assignedWorker[i] = bestWorker;
            startTime[i] = nextFreeTime[bestWorker];
            nextFreeTime[bestWorker] += duration;
        }
    }

    static void Solve()
    {
        ReadData();
        AssignJobs();
        WriteResponse();
    }

    // TODO: add tests
}
