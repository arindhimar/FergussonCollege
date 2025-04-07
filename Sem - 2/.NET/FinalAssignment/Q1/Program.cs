using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;

namespace Q1
{
    internal class Program
    {
        static void qa()
        {
            string s = Console.ReadLine();

            string[] strings = s.Split(' ');

            for (int i = 0; i < strings.Length; i++)
            {
                if (strings[i].Length > 2)
                {
                    char[] chars = strings[i].ToCharArray();
                    char temp = chars[0];
                    chars[0] = chars[chars.Length - 1];
                    chars[chars.Length - 1] = temp;
                    strings[i] = new string(chars);
                }
            }

            for(int i=0;i<strings.Length;i++) {
                Console.WriteLine(strings[i]);
            }

        }

        static void qb()
        {
            int n = int.Parse(Console.ReadLine());

            int sum = 0;
            while (n > 0)
            {
                sum += n % 10;
                n /= 10;
            }
            Console.WriteLine(sum);
        }



        static void Main(string[] args)
        {
            qa();
            qb();
            Console.ReadLine();
        }
    }
}
