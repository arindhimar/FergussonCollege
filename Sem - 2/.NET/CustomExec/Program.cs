using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CustomExec
{
    internal class Program
    {
        static void Main(string[] args)
        {
            try
            {
                Console.WriteLine(UserExecption.div(5,0));
            }
            catch (CustomExeception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
    }
}
