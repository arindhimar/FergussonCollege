using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SampleLearning
{
    public class CustomException : Exception { 
        public int ErrorCode { get; set; }
        public string ErrorMessage { get; set; }

        public CustomException(int errorCode, string errorMessage):base(errorMessage)
        {
            ErrorCode = errorCode;
            ErrorMessage = errorMessage;
        }
    }
}
