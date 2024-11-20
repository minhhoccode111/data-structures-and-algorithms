using System;
using System.Collections;

class Program
{
    static int N;
    static Hashtable PhoneBook = new Hashtable();

    static void Main(string[] args)
    {
        // Console.WriteLine("Hello, World!");
        Solve();
    }

    static void Solve()
    {
        N = int.Parse(Console.ReadLine() ?? throw new Exception("Need input n"));
        for (int i = 0; i < N; i++)
        {
            string[] data = (Console.ReadLine() ?? throw new Exception("Need input data")).Split(
                ' '
            );
            string action = data[0];
            string number = data[1];
            if (action == "add")
            {
                string name = data[2];
                PhoneBook[number] = name;
            }
            else if (action == "find")
            {
                if (PhoneBook.ContainsKey(number))
                    Console.WriteLine(PhoneBook[number]);
                else
                    Console.WriteLine("not found");
            }
            else if (action == "del")
            {
                PhoneBook.Remove(number);
            }
        }
    }
}
