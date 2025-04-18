using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Q1
{
    public class User
    {

        public static int div(int x,int y)
        {
            if (y==0)
            {
                throw new Custom("Cant div by 0");
            }

            return x / y;
            
        }
    }
}
