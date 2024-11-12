using System;
using System.Collections.Generic;
using System.Linq;

namespace StackWithMax
{
    class Program
    {
        private static void StackWithMax(int n, string[] methods)
        {
            Stack<double> stack = new Stack<double>();
            Stack<double> max = new Stack<double>();
            for (int i = 0; i < n; i++)
            {
                string[] line = methods[i].Split(' ');
                if (line[0] == "max")
                {
                    Console.WriteLine(max.Peek());
                }
                else if (line[0] == "pop")
                {
                    if (stack.Peek() == max.Peek())
                    {
                        max.Pop();
                    }
                    stack.Pop();
                }
                else if (line[0] == "push")
                {
                    double value = double.Parse(line[1]);
                    if (max.Count == 0 && stack.Count == 0)
                    {
                        max.Push(value);
                        stack.Push(value);
                    }
                    else
                    {
                        if (value >= max.Peek())
                        {
                            max.Push(value);
                        }
                        stack.Push(value);
                    }
                }
            }
        }

        static void Main()
        {
            int n = int.Parse(
                Console.ReadLine() ?? throw new ArgumentNullException("Need input 'n'")
            );

            string[] methods = new string[n];

            for (int i = 0; i < n; i++)
            {
                methods[i] =
                    Console.ReadLine() ?? throw new ArgumentNullException("Need input 'method'");
            }

            StackWithMax(n, methods);
        }
    }
}
