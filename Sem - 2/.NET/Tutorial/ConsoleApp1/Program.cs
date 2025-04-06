using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    internal class Program
    {

        static void Main(string[] args)
        {
            /*try
            {
                int n = Convert.ToInt32(Console.ReadLine());
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }*/


            /*string s = Console.ReadLine();

            char[] arr = s.ToCharArray();

            char c = arr[0];
            arr[0] = arr[arr.Length-1];
            arr[arr.Length-1] = c;

            foreach (var item in arr)
            {
                Console.WriteLine(item);
            }

            
*/


            string str = Console.ReadLine();

            char[] arr = str.ToCharArray();

            int sum = 0;

            foreach (char c in arr)
            {
                sum += Convert.ToInt16(c.ToString());
            }

            Console.WriteLine(sum);


        }
    }
}
