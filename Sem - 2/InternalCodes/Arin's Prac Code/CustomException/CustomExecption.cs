using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CustomException
{
    public class CustomException : Exception
    {
        public string errorMessage;
        

        public CustomException(string errorMessage):base(errorMessage) 
        {
            this.errorMessage = errorMessage;
        }
    }
}
