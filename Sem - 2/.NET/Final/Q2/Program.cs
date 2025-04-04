using System;

namespace Q2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter a number: ");
            int number = Convert.ToInt32(Console.ReadLine());

            if (IsPalindromeIterative(number))
            {
                Console.WriteLine($"{number} is a Palindrome number (Iterative).");
            }
            else
            {
                Console.WriteLine($"{number} is not a Palindrome number (Iterative).");
            }

            if (IsPalindromeRecursive(number, number))
            {
                Console.WriteLine($"{number} is a Palindrome number (Recursive).");
            }
            else
            {
                Console.WriteLine($"{number} is not a Palindrome number (Recursive).");
            }
        }

        static bool IsPalindromeIterative(int number)
        {
            int originalNumber = number;
            int reversedNumber = 0;

            while (number > 0)
            {
                int digit = number % 10;
                reversedNumber = (reversedNumber * 10) + digit;
                number /= 10;
            }

            return originalNumber == reversedNumber;
        }

        static bool IsPalindromeRecursive(int originalNumber, int number)
        {
            if (number == 0)
            {
                return originalNumber == 0;
            }
            else
            {
                return (originalNumber % 10 == number % 10) && IsPalindromeRecursive(originalNumber / 10, number / 10);
            }
        }
    }
}
