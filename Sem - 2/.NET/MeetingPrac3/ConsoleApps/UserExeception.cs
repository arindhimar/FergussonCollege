using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApps
{
    public class UserExeception
    {

        public static int div(int a , int b)
        {
            if (b == 0)
            {
                throw new CustomExecption("Cant divide by zero user wla");
            }

            return a/ b;
        }

    }
}
