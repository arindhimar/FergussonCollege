using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Serialization;

namespace BinaryFileOperations
{
    internal class Program
    {
        static void menu()
        {
            Console.Clear();
            Console.WriteLine("Menu:");
            Console.WriteLine("1. Write to Binary File");
            Console.WriteLine("2. Read from Binary File");
            Console.WriteLine("3. Exit");
            Console.Write("Enter your choice: ");
        }
        static void Main(string[] args)
        {
            int opt;


            do
            {

                menu();
                opt = int.Parse(Console.ReadLine());

                if (opt == 1)
                {
                    BinaryWriter writer = new BinaryWriter(File.Open("sample.bin", FileMode.Create));

                    string temp = Console.ReadLine();

                    writer.Write(temp);

                    writer.Close();

                }
                else if (opt == 2)
                {
                    BinaryReader reader = new BinaryReader(File.Open("sample.bin", FileMode.Open));

                    Console.WriteLine(reader.ReadString());

                    reader.Close();

                    Console.ReadKey();
                }
                

            } while (opt!=3);
        }
    }
}
