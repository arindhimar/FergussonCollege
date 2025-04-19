using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace Collections
{
    internal class Program
    {
        static void Main(string[] args)
        {

            Stack<int> stack = new Stack<int>();

            stack.Push(1);
            stack.Push(2);

            

            foreach (var item in stack)
            {
                Console.WriteLine(item);
            }

            Console.WriteLine(stack.Count());

            Queue<int> queue = new Queue<int>();
            queue.Enqueue(1);
            queue.Enqueue(2);

            foreach (var item in queue)
            {
                Console.WriteLine(item);
            }

            Console.WriteLine(queue.Count());

        }
    }
}
