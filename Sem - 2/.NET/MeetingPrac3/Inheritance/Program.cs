using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Inheritance
{

    public class Shape
    {
        public double CalArea()
        {
            return 0;
        }
    }

    public class Rectangle : Shape
    {
        public new double CalArea()
        {
            int l = int.Parse(Console.ReadLine());
            int b = int.Parse(Console.ReadLine());

            return l * b;
        }
    }

    public class Cirlce : Shape
    {
        public new double CalArea()
        {
            int r = int.Parse(Console.ReadLine());

            return 2*3.14*r;
        }
    }



    internal class Program
    {
        static void Main(string[] args)
        {
            Rectangle r = new Rectangle();
            Cirlce cirlce = new Cirlce();


            Console.WriteLine(r.CalArea());
            Console.WriteLine(cirlce.CalArea());    

        }
    }
}
