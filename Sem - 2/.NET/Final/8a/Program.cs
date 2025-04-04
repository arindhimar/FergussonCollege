using System;
using System.IO;

namespace _8a
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string filePath = "sample.txt";
            int choice;

            while (true)
            {
                Console.Clear();
                Console.WriteLine("Menu:");
                Console.WriteLine("1. Read File");
                Console.WriteLine("2. Write to File");
                Console.WriteLine("3. Append to File");
                Console.WriteLine("4. Exit");
                Console.Write("Enter your choice: ");
                choice = Convert.ToInt32(Console.ReadLine());

                if (choice == 1)
                {
                    if (File.Exists(filePath))
                    {
                        string content = File.ReadAllText(filePath);
                        Console.WriteLine("\nFile Content:");
                        Console.WriteLine(content);
                    }
                    else
                    {
                        Console.WriteLine("\nFile not found.");
                    }
                    Console.ReadKey();
                }
                else if (choice == 2)
                {
                    Console.Write("\nEnter text to write to the file: ");
                    string newText = Console.ReadLine();
                    File.WriteAllText(filePath, newText);
                    Console.WriteLine("\nText written to file.");
                    Console.ReadKey();
                }
                else if (choice == 3)
                {
                    Console.Write("\nEnter text to append to the file: ");
                    string textToAppend = Console.ReadLine();
                    File.AppendAllText(filePath, textToAppend);
                    Console.WriteLine("\nText appended to file.");
                    Console.ReadKey();
                }
                else if (choice == 4)
                {
                    break;
                }
                else
                {
                    Console.WriteLine("\nInvalid choice. Please try again.");
                    Console.ReadKey();
                }
            }
        }
    }
}
