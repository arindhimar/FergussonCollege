using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CustomExceptions
{
    public class CustomExceptions:Exception
    {
        public int errorCode;

        public string errorMessage;

        public CustomExceptions(int errorCode,string errorMessage):base(errorMessage) { 
            this.errorCode = errorCode;
            this.errorMessage = errorMessage;
        }
        
    }
}
