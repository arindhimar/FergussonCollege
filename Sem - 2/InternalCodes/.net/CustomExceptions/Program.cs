using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CustomExceptions
{
    internal class Program
    {
        static void Main(string[] args)
        {
           
            try
            {
                int x= UserException.div(5, 0);
            }
            catch (CustomExceptions e)
            {
                Console.WriteLine(e);
            }
        }
    }
}
