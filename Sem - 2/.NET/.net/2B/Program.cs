using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _2B
{
    internal class Program
    {
        static void Main(string[] args)
        {
            try
            {
                Console.Write("Enter a number: ");
                double number = Convert.ToDouble(Console.ReadLine());

                if (number < 0)
                {
                    throw new ArgumentOutOfRangeException("Number cannot be negative.");
                }

                double result = Math.Sqrt(number);
                Console.WriteLine("Square root of {0} is {1}", number, result);
            }
            catch (ArgumentOutOfRangeException ex)
            {
                Console.WriteLine("Error: " + ex.Message);
            }
            catch (FormatException)
            {
                Console.WriteLine("Error: Please enter a valid numeric value.");
            }
            catch (Exception ex)
            {
                Console.WriteLine("Unexpected error: " + ex.Message);
            }

            Console.WriteLine("Press any key to exit...");
            Console.ReadKey();
        }
    }
}
