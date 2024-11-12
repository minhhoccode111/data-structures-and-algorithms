using System.Diagnostics;
using TreeHeight;

namespace Tests
{
    public class Tests
    {
        // run all testcases in /tests dir by default
        public static void Run(string testDirectory = "tests")
        {
            int totalTests = 0;
            int passedTests = 0;
            var totalStopwatch = Stopwatch.StartNew(); // Start timing total run

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

                // Read test input and expected output
                string inputN = File.ReadAllText(testFile).Trim().Split('\n')[0];
                string inputParents = File.ReadAllText(testFile).Trim().Split('\n')[1];
                string expectedOutput = File.ReadAllText(answerFile).Trim();

                // NOTE: Process the input with our program here
                int mismatch = Program.TreeHeightCal(inputN, inputParents);
                string actualOutput = mismatch == -1 ? "Success" : mismatch.ToString();

                // Stop timing individual test
                testStopwatch.Stop();
                var testTime = testStopwatch.Elapsed;

                // Compare results
                bool passed = actualOutput == expectedOutput;
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
                    Console.WriteLine($"InputN: {inputN}");
                    Console.WriteLine($"InputParents: {inputParents}");
                    Console.WriteLine($"Expected: {expectedOutput}");
                    Console.WriteLine($"Got: {actualOutput}");
                }
                Console.ResetColor();
            }

            // Stop timing total run
            totalStopwatch.Stop();
            var totalTime = totalStopwatch.Elapsed;

            // Print summary with timing information
            Console.WriteLine($"\nTest Summary: {passedTests}/{totalTests} tests passed");
            Console.WriteLine($"Total Time: {FormatTime(totalTime)}");
            if (totalTests > 0)
            {
                Console.WriteLine(
                    $"Average Time per Test: {FormatTime(TimeSpan.FromTicks(totalTime.Ticks / totalTests))}"
                );
            }
        }

        // Helper method to format TimeSpan in a readable way
        private static string FormatTime(TimeSpan ts)
        {
            if (ts.TotalSeconds >= 1)
            {
                return $"{ts.TotalSeconds:F3}s";
            }
            else if (ts.TotalMilliseconds >= 1)
            {
                return $"{ts.TotalMilliseconds:F2}ms";
            }
            else
            {
                return $"{ts.Ticks / 10:F0}μs"; // Convert ticks to microseconds
            }
        }
    }
}
