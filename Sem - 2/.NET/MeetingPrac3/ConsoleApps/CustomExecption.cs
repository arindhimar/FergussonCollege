using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApps
{
    public class CustomExecption:Exception
    {
        public string errorMessage;

        public CustomExecption(string errorMessage):base(errorMessage) 
        {
            this.errorMessage = errorMessage;
        }

    }
}
