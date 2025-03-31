using System;
using System.IO;

namespace Question12
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("User Input Validation System");

            try
            {
                int age = GetValidInteger("Enter your age: ", 1, 120);
                double salary = GetValidDouble("Enter your salary: ", 0, double.MaxValue);
                char grade = GetValidChar("Enter your grade (A-F): ", new char[] { 'A', 'B', 'C', 'D', 'E', 'F' });
                bool isEmployed = GetValidBoolean("Are you employed? (true/false): ");
                string choice = GetValidChoice("Do you want to continue? (yes/no): ", new string[] { "yes", "no" });

                Console.WriteLine("\nUser Input Summary:");
                Console.WriteLine($"Age: {age}");
                Console.WriteLine($"Salary: {salary}");
                Console.WriteLine($"Grade: {grade}");
                Console.WriteLine($"Employed: {isEmployed}");
                Console.WriteLine($"Choice: {choice}");

                LogInput(age, salary, grade, isEmployed, choice);
            }
            catch (Exception ex)
            {
                Console.WriteLine("An unexpected error occurred: " + ex.Message);
            }
        }

        static void LogInput(int age, double salary, char grade, bool isEmployed, string choice)
        {
            string logFilePath = "user_input_log.txt";
            try
            {
                using (StreamWriter writer = new StreamWriter(logFilePath, true))
                {
                    writer.WriteLine($"Timestamp: {DateTime.Now}");
                    writer.WriteLine($"Age: {age}");
                    writer.WriteLine($"Salary: {salary}");
                    writer.WriteLine($"Grade: {grade}");
                    writer.WriteLine($"Employed: {isEmployed}");
                    writer.WriteLine($"Choice: {choice}");
                    writer.WriteLine("--------------------------------------");
                }
                Console.WriteLine("User input has been logged successfully.");
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error writing to log file: " + ex.Message);
            }
        }

        static int GetValidInteger(string prompt, int min, int max)
        {
            while (true)
            {
                try
                {
                    Console.Write(prompt);
                    int result = int.Parse(Console.ReadLine());
                    if (result >= min && result <= max)
                        return result;
                    Console.WriteLine("Error: Please enter a number between " + min + " and " + max + ".");
                }
                catch (Exception ex)
                {
                    Console.WriteLine("Invalid input. " + ex.Message);
                }
            }
        }

        static double GetValidDouble(string prompt, double min, double max)
        {
            while (true)
            {
                try
                {
                    Console.Write(prompt);
                    double result = double.Parse(Console.ReadLine());
                    if (result >= min && result <= max)
                        return result;
                    Console.WriteLine("Error: Please enter a valid number greater than or equal to " + min + ".");
                }
                catch (Exception ex)
                {
                    Console.WriteLine("Invalid input. " + ex.Message);
                }
            }
        }

        static char GetValidChar(string prompt, char[] validChars)
        {
            while (true)
            {
                try
                {
                    Console.Write(prompt);
                    char input = char.Parse(Console.ReadLine().ToUpper());
                    if (Array.Exists(validChars, c => c == input))
                        return input;
                    Console.WriteLine("Error: Please enter one of the following: " + string.Join(", ", validChars) + ".");
                }
                catch (Exception ex)
                {
                    Console.WriteLine("Invalid input. " + ex.Message);
                }
            }
        }

        static bool GetValidBoolean(string prompt)
        {
            while (true)
            {
                try
                {
                    Console.Write(prompt);
                    return bool.Parse(Console.ReadLine());
                }
                catch (Exception ex)
                {
                    Console.WriteLine("Invalid input. " + ex.Message);
                }
            }
        }

        static string GetValidChoice(string prompt, string[] validChoices)
        {
            while (true)
            {
                try
                {
                    Console.Write(prompt);
                    string input = Console.ReadLine()?.Trim().ToLower();
                    if (Array.Exists(validChoices, choice => choice == input))
                        return input;
                    Console.WriteLine("Error: Please enter one of the following: " + string.Join(", ", validChoices) + ".");
                }
                catch (Exception ex)
                {
                    Console.WriteLine("Invalid input. " + ex.Message);
                }
            }
        }
    }
}