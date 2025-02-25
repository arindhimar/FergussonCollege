using System;
using System.IO;

namespace Assignment___1
{
    internal class Program
    {
        void Q1()
        {
            Console.Write("Give an input in order to typecast: ");
            string input = Console.ReadLine();

            try
            {
                int intValue = Convert.ToInt32(input);
                Console.WriteLine($"Integer value: {intValue}");
            }
            catch
            {
                Console.WriteLine("Input is not a valid integer.");
            }

            try
            {
                bool boolValue = Convert.ToBoolean(input);
                Console.WriteLine($"Boolean value: {boolValue}");
            }
            catch
            {
                Console.WriteLine("Input is not a valid boolean.");
            }

            try
            {
                double doubleValue = Convert.ToDouble(input);
                Console.WriteLine($"Double value: {doubleValue}");
            }
            catch
            {
                Console.WriteLine("Input is not a valid double.");
            }

            try
            {
                decimal decimalValue = Convert.ToDecimal(input);
                Console.WriteLine($"Decimal value: {decimalValue}");
            }
            catch
            {
                Console.WriteLine("Input is not a valid decimal.");
            }

            try
            {
                DateTime dateTimeValue = Convert.ToDateTime(input);
                Console.WriteLine($"DateTime value: {dateTimeValue}");
            }
            catch
            {
                Console.WriteLine("Input is not a valid DateTime.");
            }
        }

        void Q2()
        {
            Console.Write("Enter a string: ");
            string input = Console.ReadLine();

            string upperCase = input.ToUpper();
            string lowerCase = input.ToLower();
            string trimmed = input.Trim();
            string replaced = input.Replace('l', '*');

            int count = 0;
            for (int i = 0; i < input.Length; i++)
            {
                if (input[i] == 'l')
                {
                    count++;
                }
            }

            string formattedOutput = string.Join("*", input.ToCharArray());

            Console.WriteLine($"Uppercase: {upperCase}");
            Console.WriteLine($"Lowercase: {lowerCase}");
            Console.WriteLine($"Trimmed: '{trimmed}'");
            Console.WriteLine($"Replaced 'l' with '*': {replaced}");
            Console.WriteLine($"Number of 'l' in the string: {count}");
            Console.WriteLine($"Formatted output: {formattedOutput}");
        }

        void Q3()
        {
            string filePath = "output.txt";

            if (File.Exists(filePath))
            {
                Console.WriteLine("Current contents of the file:");
                string[] lines = File.ReadAllLines(filePath);
                foreach (string line in lines)
                {
                    Console.WriteLine(line);
                }
            }
            else
            {
                Console.WriteLine("File does not exist. A new file will be created.");
            }

            Console.Write("Enter a string to append to the file: ");
            string input = Console.ReadLine();

            using (StreamWriter writer = new StreamWriter(filePath, true))
            {
                writer.WriteLine(input);
            }

            Console.WriteLine("String appended to the file successfully.");

            Console.WriteLine("Updated contents of the file:");
            string[] updatedLines = File.ReadAllLines(filePath);
            foreach (string line in updatedLines)
            {
                Console.WriteLine(line);
            }
        }

        static void Main(string[] args)
        {
            Program program = new Program();
            bool exit = false;

            while (!exit)
            {
                Console.WriteLine("\nMenu:");
                Console.WriteLine("1. Typecast Input");
                Console.WriteLine("2. String Manipulation");
                Console.WriteLine("3. Append to File");
                Console.WriteLine("4. Exit");
                Console.Write("Choose an option (1-4): ");

                string choice = Console.ReadLine();

                switch (choice)
                {
                    case "1":
                        program.Q1();
                        break;
                    case "2":
                        program.Q2();
                        break;
                    case "3":
                        program.Q3();
                        break;
                    case "4":
                        exit = true;
                        Console.WriteLine("Exiting the program.");
                        break;
                    default:
                        Console.WriteLine("Invalid choice. Please select a valid option.");
                        break;
                }
            }
        }
    }
}