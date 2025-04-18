using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CustomException
{
    public class UserExecption
    {
        public static int div(int a,int b)
        {
            if (b == 0)
            {
                throw new CustomException("Cant divide by zero!!");
            }

            return a / b;
        }
    }
}
