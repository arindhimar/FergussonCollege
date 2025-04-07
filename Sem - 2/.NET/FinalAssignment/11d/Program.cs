using System;
using System.Linq;
using System.Collections.Generic;

namespace _11d
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int> { 1, 3, 5, 7, 9, 2, 4, 6, 8, 10 };
            List<string> fruits = new List<string> { "Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape" };

            int choice;

            while (true)
            {
                Console.Clear();
                Console.WriteLine("LINQ to Collections Demo Menu:");
                Console.WriteLine("1. Get Even Numbers from List");
                Console.WriteLine("2. Get Odd Numbers from List");
                Console.WriteLine("3. Get Fruits Containing 'e'");
                Console.WriteLine("4. Sort Numbers in Descending Order");
                Console.WriteLine("5. Count Fruits Starting with 'B'");
                Console.WriteLine("6. Exit");
                Console.Write("Enter your choice: ");
                choice = Convert.ToInt32(Console.ReadLine());

                if (choice == 1)
                {
                    var evenNumbers = from num in numbers
                                      where num % 2 == 0
                                      select num;

                    Console.WriteLine("\nEven numbers:");
                    foreach (var num in evenNumbers)
                    {
                        Console.WriteLine(num);
                    }
                }
                else if (choice == 2)
                {
                    var oddNumbers = numbers.Where(n => n % 2 != 0);

                    Console.WriteLine("\nOdd numbers:");
                    foreach (var num in oddNumbers)
                    {
                        Console.WriteLine(num);
                    }
                }
                else if (choice == 3)
                {
                    var fruitsWithE = from fruit in fruits
                                      where fruit.Contains("e")
                                      select fruit;

                    Console.WriteLine("\nFruits containing 'e':");
                    foreach (var fruit in fruitsWithE)
                    {
                        Console.WriteLine(fruit);
                    }
                }
                else if (choice == 4)
                {
                    var sortedNumbers = numbers.OrderByDescending(n => n);

                    Console.WriteLine("\nNumbers sorted in descending order:");
                    foreach (var num in sortedNumbers)
                    {
                        Console.WriteLine(num);
                    }
                }
                else if (choice == 5)
                {
                    var countB = fruits.Count(fruit => fruit.StartsWith("B"));

                    Console.WriteLine($"\nNumber of fruits starting with 'B': {countB}");
                }
                else if (choice == 6)
                {
                    break;
                }
                else
                {
                    Console.WriteLine("\nInvalid choice. Please try again.");
                }

                Console.ReadKey();
            }
        }
    }
}
