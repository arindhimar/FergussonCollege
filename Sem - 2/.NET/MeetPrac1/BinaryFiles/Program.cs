using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BinaryFiles
{
    internal class Program
    {


        public static void menu()
        {
            Console.WriteLine("1 - Create");
            Console.WriteLine("2 - Read");
            Console.WriteLine("3 - Append");
            Console.WriteLine("4 - Exit");
        }

        static void Main(string[] args)
        {
            int opt = 0;

            do
            {
                menu();
                opt = int.Parse(Console.ReadLine());

                if(opt == 1)
                {
                    string temp  = Console.ReadLine();

                    BinaryWriter binaryWriter = new BinaryWriter(File.Open("sample.bin",FileMode.Create));

                    binaryWriter.Write(temp);

                    binaryWriter.Close();

                }
                else if (opt == 2)
                {
                    BinaryReader binaryReader = new BinaryReader(File.Open("sample.bin",FileMode.Open));

                    string temp  = binaryReader.ReadString();

                    string temp2 = binaryReader.ReadString();


                    Console.WriteLine(temp+ temp2);

                    binaryReader.Close();

                }
                else if (opt == 3)
                {
                    BinaryWriter binaryWriter = new BinaryWriter(File.Open("sample.bin", FileMode.Append));
                    string temp = Console.ReadLine();

                    binaryWriter.Write(temp);

                    binaryWriter.Close();
                }
                else if (opt == 5)
                {
                    FileInfo fileInfo = new FileInfo(Console.ReadLine());
                    Console.WriteLine(fileInfo.Name);

                    DirectoryInfo directoryInfo = new DirectoryInfo(Console.ReadLine());
                    Console.WriteLine(directoryInfo.FullName);
                }


            } while (opt!=4);
        }
    }
}
