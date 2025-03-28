using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Question4
{
    internal class Program
    {
        static int add(int x,int y) {  return x + y; }
        static int sub(int x, int y) { return x - y; }
        static int mul(int x,int y) {return x * y; }
        static int div(int x,int y) { if (y == 0) return 0; return x / y; }
            
        static void menu()
        {
            Console.WriteLine("1 - Add");
            Console.WriteLine("2 - Sub");
            Console.WriteLine("3 - Mul");
            Console.WriteLine("4 - Div");
        }

        static void Main(string[] args)
        {
            int opt = 0;
            int a, b;
            do
            {
                menu();
                opt = Convert.ToInt32(Console.ReadLine());

                switch (opt)
                {
                    case 1:
                        a = Convert.ToInt32(Console.ReadLine());
                        b = Convert.ToInt32(Console.ReadLine());

                        Console.WriteLine(add(a,b));

                        break;
                    case 2:
                        a = Convert.ToInt32(Console.ReadLine());
                        b = Convert.ToInt32(Console.ReadLine());

                        Console.WriteLine(sub(a, b));
                        break;
                    case 3:
                        a = Convert.ToInt32(Console.ReadLine());
                        b = Convert.ToInt32(Console.ReadLine());

                        Console.WriteLine(mul(a, b));
                        break;
                    case 4:
                        a = Convert.ToInt32(Console.ReadLine());
                        b = Convert.ToInt32(Console.ReadLine());

                        Console.WriteLine(div(a, b));
                        break;
                }

            }while (opt > 0);

        }
    }
}
