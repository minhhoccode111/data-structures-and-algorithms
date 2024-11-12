using System;
using System.Collections.Generic;

namespace CheckBrackets
{
    class Bracket
    {
        public char Value { get; }
        public int Index { get; }

        public Bracket(char value, int index)
        {
            Value = value;
            Index = index;
        }
    }

    class Helper
    {
        public static bool IsOpen(char currChar) =>
            currChar == '{' || currChar == '(' || currChar == '[';

        public static bool IsClose(char currChar) =>
            currChar == '}' || currChar == ')' || currChar == ']';

        public static bool IsSameType(char openBracket, char closeBracket) =>
            (openBracket == '{' && closeBracket == '}')
            || (openBracket == '(' && closeBracket == ')')
            || (openBracket == '[' && closeBracket == ']');
    }

    public class Program
    {
        public static int FindMismatch(string text)
        {
            Stack<Bracket> openBrackets = new Stack<Bracket>();
            for (int i = 0; i < text.Length; i++)
            {
                char currChar = text[i];

                if (Helper.IsOpen(currChar))
                {
                    Bracket openBracket = new Bracket(currChar, i + 1);
                    openBrackets.Push(openBracket);
                }
                else if (Helper.IsClose(currChar))
                {
                    if (openBrackets.Count == 0)
                    {
                        return i + 1;
                    }

                    char openBracket = openBrackets.Pop().Value;

                    if (!Helper.IsSameType(openBracket, currChar))
                    {
                        return i + 1;
                    }
                }
            }

            if (openBrackets.Count != 0)
            {
                return openBrackets.Pop().Index;
            }

            return -1;
        }

        public static void Main(string[] args)
        {
            if (args is not null)
            {
                Tests.Tests.Run();
                return;
            }

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
