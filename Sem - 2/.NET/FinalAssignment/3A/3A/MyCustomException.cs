using System;

namespace MyOperations
{
    public class MyCustomException : Exception
    {
        public int ErrorCode { get; set; }
        public string ErrorMessage { get; set; }

        public MyCustomException(int errorCode, string errorMessage)
            : base(errorMessage)
        {
            ErrorCode = errorCode;
            ErrorMessage = errorMessage;
        }
    }
}
