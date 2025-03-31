using System;
using System.IO;

namespace Question7
{
    internal class Program
    {
        static void Main(string[] args)
        {
            while (true)
            {
                Console.WriteLine("\nFile Management System");
                Console.WriteLine("1. Create and Write to a File");
                Console.WriteLine("2. Read a File");
                Console.WriteLine("3. Delete a File");
                Console.WriteLine("4. Check if File Exists");
                Console.WriteLine("5. Exit");
                Console.Write("Enter your choice: ");

                string choice = Console.ReadLine();
                switch (choice)
                {
                    case "1":
                        CreateAndWriteFile();
                        break;
                    case "2":
                        ReadFile();
                        break;
                    case "3":
                        DeleteFile();
                        break;
                    case "4":
                        CheckFileExists();
                        break;
                    case "5":
                        return;
                    default:
                        Console.WriteLine("Invalid choice. Please try again.");
                        break;
                }
            }
        }

        static void CreateAndWriteFile()
        {
            try
            {
                Console.Write("Enter file name: ");
                string fileName = Console.ReadLine();
                Console.Write("Enter text to write into the file: ");
                string content = Console.ReadLine();

                File.WriteAllText(fileName, content);
                Console.WriteLine("File created and written successfully.");
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error: " + ex.Message);
            }
        }

        static void ReadFile()
        {
            try
            {
                Console.Write("Enter file name to read: ");
                string fileName = Console.ReadLine();
                if (File.Exists(fileName))
                {
                    string content = File.ReadAllText(fileName);
                    Console.WriteLine("File Content:\n" + content);
                }
                else
                {
                    Console.WriteLine("File not found.");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error: " + ex.Message);
            }
        }

        static void DeleteFile()
        {
            try
            {
                Console.Write("Enter file name to delete: ");
                string fileName = Console.ReadLine();
                if (File.Exists(fileName))
                {
                    File.Delete(fileName);
                    Console.WriteLine("File deleted successfully.");
                }
                else
                {
                    Console.WriteLine("File not found.");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error: " + ex.Message);
            }
        }

        static void CheckFileExists()
        {
            Console.Write("Enter file name to check: ");
            string fileName = Console.ReadLine();
            if (File.Exists(fileName))
            {
                Console.WriteLine("File exists.");
            }
            else
            {
                Console.WriteLine("File does not exist.");
            }
        }
    }
}