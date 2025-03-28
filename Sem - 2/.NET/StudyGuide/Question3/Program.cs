using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Question3
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string str;

            str = Console.ReadLine();

            Console.WriteLine(str.ToLower());

            Console.WriteLine(str.ToUpper());

            //Console.WriteLine(str.Replace("try","do not try"));

            str = str.Replace("try", "do not try");

            Console.WriteLine(str);

            Console.ReadKey();
        }
    }
}
