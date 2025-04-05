using SampleLearning;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _3A
{
    public class LolExpections
    {
        public int Div()
        {
            int numerator,denominator;

            numerator = Convert.ToInt32(Console.ReadLine());
            denominator = Convert.ToInt32(Console.ReadLine());


            try
            {
                return numerator / denominator;
            }
            catch (DivideByZeroException e)
            {
                throw new CustomException(101,"Cannot divide by zero");
            }
        }

        public int IdxOutOfRange()
        {
            int[] arr = {1,2,3};

            try
            {
                int n = Convert.ToInt32(Console.ReadLine());

                Console.WriteLine(arr[n]);
            }
            catch(IndexOutOfRangeException e)
            {
                throw new CustomException(102, "Index out of bound!");
            }

            return 0;

        }
    }
}
