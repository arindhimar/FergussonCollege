using _3A;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SampleLearning
{



    internal class Program
    {

        void TryFun()
        {
            Console.WriteLine("Hey IM A function");
        }



        static void Main(string[] args)
        {
            //take full line as input
            //string s = Console.ReadLine();

            //int input
            //int n = Convert.ToInt32(Console.ReadLine());

            //double input

            //try
            //{
            //    double d = Convert.ToDouble(Console.ReadLine());
            //    Console.WriteLine(d);
            //}
            //catch (Exception e)
            //{
            //    Console.WriteLine(e.Message);
            //}
            //Program p = new Program();
            //p.TryFun();

            //Diplay the output

            //display output
            /*Console.Write(s);
            Console.WriteLine(s);*/


/*            string str = Console.ReadLine();
            
            char[] arr = str.ToCharArray();

            char c = arr[0];

            arr[0] = arr[arr.Length - 1];

            arr[arr.Length - 1] = c;




            foreach (var item in arr)
            {
                Console.Write(item);
            }
*/          
/*
            int n = Convert.ToInt32(Console.ReadLine());

            int sum = 0;

            while (n > 0)
            {
                int temp = n % 10;
                sum += temp;
                n /= 10;
            }

            Console.WriteLine(sum);*/

/*            LolExpections lolExpections = new LolExpections();

            try
            {
                lolExpections.IdxOutOfRange();
            }
            catch (CustomException e)
            {
                Console.WriteLine($"{e.Message}");
            }*/

        }
    }
}
