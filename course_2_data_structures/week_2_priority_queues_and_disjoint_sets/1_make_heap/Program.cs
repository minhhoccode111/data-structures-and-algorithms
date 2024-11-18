using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Resources;

class Program
{
    static int N { get; set; }
    static int[] Data { get; set; }
    static List<Swap> Swaps;

    static void Main(string[] args)
    {
        if (args != null)
        {
            Test();
            return;
        }

        Solve();
    }

    static void Solve()
    {
        string nInput = Console.ReadLine() ?? throw new Exception("Need input 'n'");
        string dataInput = Console.ReadLine() ?? throw new Exception("Need input 'data'");
        BuildMaxHeap(nInput, dataInput);
        PrintSwaps();
    }

    static void PrintSwaps()
    {
        int len = Swaps.Count;
        Console.WriteLine(len);
        for (int i = 0; i < len; i++)
        {
            Swap swap = Swaps[i];
            Console.WriteLine(swap.index1 + " " + swap.index2);
        }
    }

    static void BuildMaxHeap(string nInput, string dataInput)
    {
        N = int.Parse(nInput);
        Data = dataInput.Split(' ').Select(int.Parse).ToArray();

        if (N != Data.Length)
        {
            throw new Exception("Wrong input length");
        }

        Swaps = new List<Swap>();
        for (int i = N / 2 - 1; i >= 0; i--)
        {
            SiftDown(i);
        }
    }

    static void SiftDown(int i)
    {
        int l = 2 * i + 1;
        int r = 2 * i + 2;

        int min = i;

        if (l < N && Data[l] < Data[min])
            min = l;

        if (r < N && Data[r] < Data[min])
            min = r;

        if (i != min)
        {
            // push the swap to Swaps
            Swap swap = new Swap(i, min);
            Swaps.Add(swap);
            // actually swap
            // (Data[i], Data[min]) = (Data[min], Data[i]); // syntax not support in C# 7.0
            int tmp = Data[i];
            Data[i] = Data[min];
            Data[min] = tmp;
            // recursive call, can optimize using a while loop
            SiftDown(min);
        }
    }

    static void Test(string testDirectory = "tests")
    {
        int totalTests = 0;
        int passedTests = 0;

        // Get all test input files (files without .a extension)
        var testFiles = Directory
            .GetFiles(testDirectory)
            .Where(f => !f.EndsWith(".a"))
            .OrderBy(f => f);

        foreach (string testFile in testFiles)
        {
            string answerFile = testFile + ".a";

            if (!File.Exists(answerFile))
            {
                Console.WriteLine($"Warning: Answer file not found for {testFile}");
                continue;
            }

            totalTests++;
            var testStopwatch = Stopwatch.StartNew(); // Start timing individual test

            // NOTE: custom this base on input files
            // Read test input and expected output
            string[] input = File.ReadAllText(testFile).Trim().Split('\n');
            string inputN = input[0];
            string inputData = input[1];
            string[] outputExpectedArrStr = File.ReadAllText(answerFile).Trim().Split('\n');

            /*
            input file format
            100000
            999996831 999995868 999979435 999944647 999939222 ...
            ---
            output file format
            99990
            49999 99999
            49998 99998
            49997 99996
            49996 99994
            ...
            */

            List<Swap> outputExpected = new List<Swap>();

            // start from 1 because the first item indicate the total number of swaps
            for (int i = 1; i < outputExpectedArrStr.Length; i++)
            {
                int[] swapArr = outputExpectedArrStr[i].Split(' ').Select(int.Parse).ToArray();
                int index1 = swapArr[0];
                int index2 = swapArr[1];
                Swap currentSwap = new Swap(index1, index2);
                outputExpected.Add(currentSwap);
            }

            int numberOfSwaps = int.Parse(outputExpectedArrStr[0]);

            BuildMaxHeap(inputN, inputData);
            List<Swap> outputReceived = Swaps;

            // Stop timing individual test
            testStopwatch.Stop();
            var testTime = testStopwatch.Elapsed;

            // Compare results
            bool passed = true;

            if (outputReceived.Count != numberOfSwaps)
            {
                Console.WriteLine(
                    $"Wrong number of swaps: {outputReceived.Count} != {numberOfSwaps}"
                );
                passed = false;
            }

            for (int i = 0; i < outputReceived.Count; i++)
            {
                if (
                    outputReceived[i].index1 != outputExpected[i].index1
                    || outputReceived[i].index2 != outputExpected[i].index2
                )
                {
                    Console.WriteLine(
                        $"Received: {outputReceived[i].index1}, {outputReceived[i].index2}"
                    );
                    Console.WriteLine(
                        $"Expected: {outputExpected[i].index1}, {outputExpected[i].index2}"
                    );
                    passed = false;
                    break;
                }
            }

            if (passed)
            {
                passedTests++;
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine(
                    $"Test {Path.GetFileName(testFile)} PASSED (Time: {FormatTime(testTime)})"
                );
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine(
                    $"Test {Path.GetFileName(testFile)} FAILED (Time: {FormatTime(testTime)})"
                );
            }
            Console.ResetColor();

            // Print summary with timing information
            Console.WriteLine($"\nTest Summary: {passedTests}/{totalTests} tests passed");
        }
    }

    static string FormatTime(TimeSpan ts) =>
        ts.TotalSeconds >= 1 ? $"{ts.TotalSeconds:F3}s"
        : ts.TotalMilliseconds >= 1 ? $"{ts.TotalMilliseconds:F2}ms"
        : $"{ts.Ticks / 10:F0}μs";
}

class Swap
{
    public int index1;
    public int index2;

    public Swap(int index1, int index2)
    {
        this.index1 = index1;
        this.index2 = index2;
    }
}
