using System;
using System.IO;

namespace BinaryFileExample
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string filePath = "data.bin";
            int choice;

            while (true)
            {
                Console.Clear();
                Console.WriteLine("Menu:");
                Console.WriteLine("1. Write to Binary File");
                Console.WriteLine("2. Read from Binary File");
                Console.WriteLine("3. Exit");
                Console.Write("Enter your choice: ");
                choice = Convert.ToInt32(Console.ReadLine());

                if (choice == 1)
                {
                    Console.Write("Enter an integer to write to the binary file: ");
                    int intData = Convert.ToInt32(Console.ReadLine());

                    Console.Write("Enter a double to write to the binary file: ");
                    double doubleData = Convert.ToDouble(Console.ReadLine());

                    Console.Write("Enter a string to write to the binary file: ");
                    string stringData = Console.ReadLine();

                    using (BinaryWriter writer = new BinaryWriter(File.Open(filePath, FileMode.Create)))
                    {
                        writer.Write(intData);
                        writer.Write(doubleData);
                        writer.Write(stringData);
                    }

                    Console.WriteLine("\nData written to binary file.");
                    Console.ReadKey();
                }
                else if (choice == 2)
                {
                    if (File.Exists(filePath))
                    {
                        using (BinaryReader reader = new BinaryReader(File.Open(filePath, FileMode.Open)))
                        {
                            int intData = reader.ReadInt32();
                            double doubleData = reader.ReadDouble();
                            string stringData = reader.ReadString();

                            Console.WriteLine("\nData read from binary file:");
                            Console.WriteLine("Integer: " + intData);
                            Console.WriteLine("Double: " + doubleData);
                            Console.WriteLine("String: " + stringData);
                        }
                    }
                    else
                    {
                        Console.WriteLine("\nFile not found.");
                    }

                    Console.ReadKey();
                }
                else if (choice == 3)
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
