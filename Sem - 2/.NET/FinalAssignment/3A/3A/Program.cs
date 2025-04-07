using System;
using MyOperations;

namespace ConsoleApp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            try
            {
                int result = Operations.Divide(10, 0); 
                Console.WriteLine($"Result of division: {result}");
            }
            catch (MyCustomException ex)
            {
                Console.WriteLine($"Custom Exception Caught: Error Code: {ex.ErrorCode}, Error Message: {ex.ErrorMessage}");
            }

            try
            {
                int[] numbers = { 1, 2, 3 };
                int element = Operations.GetElementAtIndex(numbers, 5); 
                Console.WriteLine($"Element at index 5: {element}");
            }
            catch (MyCustomException ex)
            {
                Console.WriteLine($"Custom Exception Caught: Error Code: {ex.ErrorCode}, Error Message: {ex.ErrorMessage}");
            }

            Console.ReadLine();
        }
    }
}
