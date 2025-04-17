using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Linq.Expressions;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApps
{
    internal class Program
    {

        public static void menu()
        {
            Console.WriteLine("1 - Write");
            Console.WriteLine("2 - Read");
            Console.WriteLine("3 - Apppend");
            Console.WriteLine("4 - Exit");
        }

        static void Main(string[] args)
        {
            int opt = 0;
            do
            {
                menu();
                try
                {
                    opt = int.Parse(Console.ReadLine());
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.Message);
                }

                if (opt == 1)
                {
                    string temp = Console.ReadLine();
                    File.WriteAllText("sample.txt", temp);

                }
                else if (opt == 2)
                {
                    string temp = File.ReadAllText("sample.txt");
                    Console.WriteLine(temp);
                }
                else if(opt == 3)
                {
                    string temp = Console.ReadLine();
                    File.AppendAllText("sample.txt", temp);
                }


            }while (opt!=4);
        }
    }
}
