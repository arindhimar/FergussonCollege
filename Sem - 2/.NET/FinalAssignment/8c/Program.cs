using System;
using System.IO;

namespace DirectoryFileInfoDemo
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter the path of the directory or file: ");
            string path = Console.ReadLine();

            if (Directory.Exists(path))
            {
                DirectoryInfo directoryInfo = new DirectoryInfo(path);

                Console.WriteLine("\nDirectory Information:");
                Console.WriteLine($"Full Name: {directoryInfo.FullName}");
                Console.WriteLine($"Creation Time: {directoryInfo.CreationTime}");
                Console.WriteLine($"Last Access Time: {directoryInfo.LastAccessTime}");
                Console.WriteLine($"Last Write Time: {directoryInfo.LastWriteTime}");
                Console.WriteLine($"Attributes: {directoryInfo.Attributes}");
                Console.WriteLine($"Parent Directory: {directoryInfo.Parent?.FullName}");

                Console.WriteLine("\nFiles in the directory:");
                FileInfo[] files = directoryInfo.GetFiles();
                foreach (var file in files)
                {
                    Console.WriteLine($"- {file.Name}");
                }
            }
            else if (File.Exists(path))
            {
                FileInfo fileInfo = new FileInfo(path);

                Console.WriteLine("\nFile Information:");
                Console.WriteLine($"Full Name: {fileInfo.FullName}");
                Console.WriteLine($"Creation Time: {fileInfo.CreationTime}");
                Console.WriteLine($"Last Access Time: {fileInfo.LastAccessTime}");
                Console.WriteLine($"Last Write Time: {fileInfo.LastWriteTime}");
                Console.WriteLine($"Size: {fileInfo.Length} bytes");
                Console.WriteLine($"Attributes: {fileInfo.Attributes}");
                Console.WriteLine($"Directory: {fileInfo.DirectoryName}");
            }
            else
            {
                Console.WriteLine("\nThe specified path is neither a valid file nor a directory.");
            }
        }
    }
}
