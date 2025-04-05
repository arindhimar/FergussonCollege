using System;

namespace MyOperations
{
    public class Operations
    {
        public static int Divide(int numerator, int denominator)
        {
            try
            {
                return numerator / denominator; 
            }
            catch (DivideByZeroException ex)
            {
                throw new MyCustomException(1001, "Error: Division by zero is not allowed.");
            }
        }

        public static int GetElementAtIndex(int[] array, int index)
        {
            try
            {
                return array[index]; 
            }
            catch (IndexOutOfRangeException ex)
            {
                throw new MyCustomException(1002, "Error: Index is out of range.");
            }
        }
    }
}
