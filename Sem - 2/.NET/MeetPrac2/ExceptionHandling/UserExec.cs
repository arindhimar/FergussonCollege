using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ExceptionHandling
{
    public class UserExec
    {
        public static int div(int a, int b)
        {
            try
            {
                return a / b;
            }
            catch(DivideByZeroException e)
            {
                throw new MyCusExec("Nahi hone wala hai!!");
            }
        }
    }
}
