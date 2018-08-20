// not working

using System;
using System.Linq;

public class Solution 
{
    public static int CountPrimes(int n) 
    {
        if(n <= 2) return 0;

        var primes = Enumerable.Repeat(true, n).ToArray();

        primes[0] = primes[1] = false;

        foreach(var x in Enumerable.Range(2, n - 2))
            if(primes[x])
                FalsifyPrimes(primes, x);

        return primes.Count(x => x);
    }

    private static void FalsifyPrimes(bool[] primes, int x)
    {
        for(int i = x + 1; i < primes.Length; i++)
        {
            if (primes[i] && i % x == 0)
            {
                primes[i] = false;
            }
        }
    }

    public static void Main()
    {
        Console.WriteLine(CountPrimes(0));
        Console.WriteLine(CountPrimes(1));
        Console.WriteLine(CountPrimes(2));
        Console.WriteLine(CountPrimes(3));
        Console.WriteLine(CountPrimes(4));
        Console.WriteLine(CountPrimes(5));
        Console.WriteLine(CountPrimes(10));
        Console.WriteLine(CountPrimes(1000));
        Console.WriteLine(CountPrimes(499979));
    }

}

/*


        for(var i = 0; i < primes.Length; i++)
            if (primes[i])
                Console.WriteLine(i);
*/