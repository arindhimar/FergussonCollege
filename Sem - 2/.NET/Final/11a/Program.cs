using System;
using System.Linq;

namespace _11a
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] numbers = { 1, 3, 5, 7, 9, 2, 4, 6, 8, 10 };
            int choice;

            while (true)
            {
                Console.Clear();
                Console.WriteLine("Menu:");
                Console.WriteLine("1. Find Even Numbers");
                Console.WriteLine("2. Numbers Greater than 5");
                Console.WriteLine("3. Sort Numbers");
                Console.WriteLine("4. First Number Greater than 5");
                Console.WriteLine("5. Sum of All Numbers");
                Console.WriteLine("6. Group Numbers by Even/Odd");
                Console.WriteLine("7. Count Even Numbers");
                Console.WriteLine("8. Exit");
                Console.Write("Enter your choice: ");
                choice = Convert.ToInt32(Console.ReadLine());

                if (choice == 1)
                {
                    var evenNumbers = from n in numbers
                                      where n % 2 == 0
                                      select n;

                    Console.WriteLine("\nEven numbers:");
                    foreach (var num in evenNumbers)
                    {
                        Console.WriteLine(num);
                    }
                }
                else if (choice == 2)
                {
                    var greaterThanFive = numbers.Where(n => n > 5);

                    Console.WriteLine("\nNumbers greater than 5:");
                    foreach (var num in greaterThanFive)
                    {
                        Console.WriteLine(num);
                    }
                }
                else if (choice == 3)
                {
                    var sortedNumbers = numbers.OrderBy(n => n);

                    Console.WriteLine("\nSorted numbers:");
                    foreach (var num in sortedNumbers)
                    {
                        Console.WriteLine(num);
                    }
                }
                else if (choice == 4)
                {
                    var firstGreaterThanFive = numbers.FirstOrDefault(n => n > 5);
                    Console.WriteLine($"\nFirst number greater than 5: {firstGreaterThanFive}");
                }
                else if (choice == 5)
                {
                    var sum = numbers.Sum();
                    Console.WriteLine($"\nSum of all numbers: {sum}");
                }
                else if (choice == 6)
                {
                    var groupedNumbers = numbers.GroupBy(n => n % 2 == 0 ? "Even" : "Odd");

                    Console.WriteLine("\nGrouped numbers (Even/Odd):");
                    foreach (var group in groupedNumbers)
                    {
                        Console.WriteLine($"{group.Key}:");
                        foreach (var num in group)
                        {
                            Console.WriteLine(num);
                        }
                    }
                }
                else if (choice == 7)
                {
                    var evenCount = numbers.Count(n => n % 2 == 0);
                    Console.WriteLine($"\nCount of even numbers: {evenCount}");
                }
                else if (choice == 8)
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
