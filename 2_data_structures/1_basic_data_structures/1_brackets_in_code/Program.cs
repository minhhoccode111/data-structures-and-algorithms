// See https://aka.ms/new-console-template for more information

using System;
using System.Collections.Generic;

// group everything related, in this situation is the check brackets problem
namespace CheckBrackets
{
    // Bracket helper class
    public class Bracket
    {
        // public properties, can only be get
        public char Char { get; } // get the bracket character
        public int Position { get; } // get the position of bracket character in the string

        // constructor function to initialize values
        public Bracket(char ch, int position)
        {
            Char = ch;
            Position = position;
        }
    }

    // .NET will search to run the `public static void Main` method in Program class to run
    public class Program
    {
        // helper method, can be call in every other method in this Program class
        // or call with Program.AreMatching from other class if public
        private static bool AreMatching(char left, char right)
        {
            // check if the left character is the same type with the right character
            return (left == '(' && right == ')')
                || (left == '[' && right == ']')
                || (left == '{' && right == '}');
        }

        // helper method, to check if char is opening bracket
        private static bool IsOpenBracket(char c) => c == '(' || c == '[' || c == '{';

        private static bool IsCloseBracket(char c) => c == ')' || c == ']' || c == '}';

        // private method to find mismatch in a string of brackets
        private static int FindMismatch(string text)
        {
            // create a stack to store opening bracket
            Stack<Bracket> openingBracketsStack = new Stack<Bracket>();
            // loop through every character in the input string
            for (int i = 0; i < text.Length; i++)
            {
                // current character
                char currChar = text[i];

                // if current character is open bracket
                if (IsOpenBracket(currChar))
                {
                    // push current char to the top of the stack
                    openingBracketsStack.Push(new Bracket(currChar, i + 1));
                }
                // if current character is close bracket
                else if (IsCloseBracket(currChar))
                {
                    // and if no open bracket exist in the stack
                    if (openingBracketsStack.Count == 0)
                    {
                        // then return the index + 1
                        return i + 1;
                    }

                    // we pop the top element of the stack bracket
                    Bracket top = openingBracketsStack.Pop();

                    // check if the top element bracket is not pair with the close bracket
                    if (!AreMatching(top.Char, currChar))
                    {
                        // then also return the index + 1
                        return i + 1;
                    }
                }
            }

            // after looping through every character in the input string,
            // if the opening brackets stack still greater than 0
            // which mean that there is still mismatch
            if (openingBracketsStack.Count > 0)
            {
                // then we return the last bracket position
                return openingBracketsStack.Peek().Position;
            }

            // else return -1, indicate that there is no mismatch found
            return -1;
        }

        // this is our program starting point
        public static void Main()
        {
            // get input from the command line
            string text = Console.ReadLine() ?? throw new Exception("Need input!");
            // find mismatch in the input string
            int mismatch = FindMismatch(text);
            // if no mismatch found
            if (mismatch == -1)
            {
                // then write "Success" to the command line
                Console.WriteLine("Success");
            }
            else
            {
                // else write the mismatch position
                Console.WriteLine(mismatch);
            }
        }
    }
}
