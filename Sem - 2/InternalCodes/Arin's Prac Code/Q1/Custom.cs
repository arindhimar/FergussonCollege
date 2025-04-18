using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Q1
{
    public class Custom:Exception
    {
        public string errorMessage;

        public Custom(string errorMessage):base(errorMessage) 
        {
            this.errorMessage = errorMessage;
        }


    }
}
