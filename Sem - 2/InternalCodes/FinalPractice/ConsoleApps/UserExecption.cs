using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApps
{
    public class UserExecption
    {
        public static int div(int x, int y)
        {
            if (y == 0)
            {
                throw new CustomExecption("Cant div by zero");
            }

            return x / y;
        }
    }
}
