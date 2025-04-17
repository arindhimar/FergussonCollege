using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CustomException
{
    internal class Program
    {
        static void Main(string[] args)
        {
            try
            {
                Console.WriteLine(CustomExec.div(5, 0));
            }
            catch (MyCus e)
            {
                Console.WriteLine(e);
            }
        }
    }
}
