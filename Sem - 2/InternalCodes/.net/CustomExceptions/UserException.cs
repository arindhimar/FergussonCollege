using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CustomExceptions
{
    public class UserException
    {
        public static int div(int x,int y)
        {
            if (y == 0)
            {
                throw new CustomExceptions(1, "Cant div by zero");
            }

            return x / y;
        }
    }
}
