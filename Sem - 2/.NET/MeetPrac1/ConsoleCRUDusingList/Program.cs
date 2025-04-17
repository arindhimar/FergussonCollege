using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleCRUDusingList
{
    public class Student
    {
        public int Id { get; set; }
        public string Name { get; set; }

    }
    internal class Program
    {


        public static void menu()
        {
            Console.WriteLine("1 - add");
            Console.WriteLine("2 - display");
            Console.WriteLine("3 - update");
            Console.WriteLine("4 - delete");
            Console.WriteLine("5 - exit");
        }

        static void Main(string[] args)
        {
            List<Student> students = new List<Student>();

            int opt;


            int tempId = 0;

            do
            {
                menu();

                opt = int.Parse(Console.ReadLine());

                if (opt == 1)
                {
                    int id = ++tempId;
                    string name = Console.ReadLine();

                    students.Add(new Student { Id = id, Name = name });
                }
                else if (opt == 2)
                {
                    foreach (var item in students)
                    {
                        Console.WriteLine(item.Id);
                        Console.WriteLine(item.Name);
                        Console.WriteLine();
                    }
                }
                else if (opt == 4)
                {
                    int id = int.Parse(Console.ReadLine());

                    Student temp = students.Where(s=>s.Id==id).FirstOrDefault();

                    if (temp != null)
                    {
                        students.Remove(temp);
                    }


                }

                else if (opt == 3)
                {
                    int id = int.Parse(Console.ReadLine());

                    Student temp = students.Where(s => s.Id == id).FirstOrDefault();

                    if (temp != null)
                    {
                        string tempName = Console.ReadLine();

                        temp.Name = tempName;
                    }
                    else
                    {
                        Console.WriteLine("Invalid Id");
                    }
                }

            } while (opt != 5) ;
        }
    }
}
