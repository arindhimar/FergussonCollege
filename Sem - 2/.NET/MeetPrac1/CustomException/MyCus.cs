using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CustomException
{
    public class MyCus:Exception
    {
        public int errorCode;
        public string errorMessage;

        public MyCus(int errorCode, string errorMessage):base(errorMessage)
        {
            this.errorCode = errorCode;
            this.errorMessage = errorMessage;
        }
    }
}
