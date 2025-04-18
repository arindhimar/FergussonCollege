using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ExceptionHandling
{
    internal class MyCusExec:Exception
    {
        string errorMessage;

        public MyCusExec(string errorMessage):base(errorMessage) 
        {
            this.errorMessage = errorMessage;
        }

    }
}
