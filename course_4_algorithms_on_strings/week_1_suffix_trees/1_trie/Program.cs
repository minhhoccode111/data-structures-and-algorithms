/*

diff <(dotnet run < test/1) <(cat test/1.a)
diff <(dotnet run < test/2) <(cat test/2.a)
diff <(dotnet run < test/3) <(cat test/3.a)

*/


using System;

public class Program
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Hello, World!");
    }
}
