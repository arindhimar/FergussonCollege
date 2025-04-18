using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CustomExec
{
    public class UserExecption
    {
        public static int div(int a, int b)
        {
            if(b==0)
            {
                throw new CustomExeception("can div by 0");
            }

            return a / b;
        }
    }
}
