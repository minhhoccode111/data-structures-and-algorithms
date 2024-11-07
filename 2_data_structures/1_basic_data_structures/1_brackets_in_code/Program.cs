// See https://aka.ms/new-console-template for more information

using System;
using System.Collections.Generic;

namespace CheckBrackets
{
    public class Bracket
    {
        public char Char { get; }
        public int Position { get; }

        public Bracket(char ch, int position)
        {
            Char = ch;
            Position = position;
        }
    }

    public class Program
    {
        static bool AreMatching(char left, char right)
        {
            return (left == '(' && right == ')')
                || (left == '[' && right == ']')
                || (left == '{' && right == '}');
        }

        static int FindMismatch(string text = "")
        {
            var openingBracketsStack = new Stack<Bracket>();
            for (int i = 0; i < text.Length; i++)
            {
                char next = text[i];

                if (next == '(' || next == '[' || next == '{')
                {
                    // Process opening bracket
                    openingBracketsStack.Push(new Bracket(next, i + 1));
                }

                if (next == ')' || next == ']' || next == '}')
                {
                    // Process closing bracket
                    if (openingBracketsStack.Count == 0)
                    {
                        return i + 1;
                    }

                    var top = openingBracketsStack.Pop();
                    if (!AreMatching(top.Char, next))
                    {
                        return i + 1;
                    }
                }
            }

            if (openingBracketsStack.Count > 0)
            {
                return openingBracketsStack.Peek().Position;
            }

            return -1;
        }

        public static void Main()
        {
            string text = Console.ReadLine() ?? throw new Exception("Need input!");
            int mismatch = FindMismatch(text);

            if (mismatch == -1)
            {
                Console.WriteLine("Success");
            }
            else
            {
                Console.WriteLine(mismatch);
            }
        }
    }
}
