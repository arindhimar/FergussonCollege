using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CustomException
{
    public class CustomExec
    {
        public static int div(int a, int b)
        {
            try
            {
                return a / b;
            }
            catch(DivideByZeroException e)
            {
                throw new MyCus(101, "ha wahi");
            }
        }
    }
}
