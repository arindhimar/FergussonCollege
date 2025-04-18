using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CustomExec
{
    public class CustomExeception:Exception
    {
        public string errorMessage;

        public CustomExeception(string errorMessage):base(errorMessage)
        {
            this.errorMessage = errorMessage;
        }
    }
}
