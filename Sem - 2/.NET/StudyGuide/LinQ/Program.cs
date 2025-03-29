using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LinQ
{
    public class Student
    {
        public int Id { get; set; }
        public string Name { get; set; }

        public int Marks { get; set; }

        public Student(int id,string name,int marks) { 
            this.Name = name;
            this.Id = id;
            this.Marks = marks;
        }

    }
    internal class Program
    {
        static void Main(string[] args)
        {
            //List <int> ints = new List <int> { 1,2,3,4,5,6,7,8,9,0};
            //Console.WriteLine(ints);
            //foreach (var item in ints.Where(num => num % 2 == 0))
            //{
            //    Console.WriteLine(item);

            //}


            List<Student> list = new List<Student>
            {
                new Student(1,"Arin",80),new Student(2,"Darshan", 90),new Student(3,"Vasu", 85)
            };

            //foreach (var item in list)
            //{
            //    Console.WriteLine(item.Id);
            //    Console.WriteLine(item.Name);
            //    Console.WriteLine("\n\n");
            //}



            //fetching data from the object
            //foreach (var item in list.Where(temp=>temp.Name=="Arin"))
            //{
            //    Console.WriteLine(item.Id);
            //    Console.WriteLine(item.Name);
            //    Console.WriteLine("\n\n");
            //}


            //fetching just name
            //IEnumerable<string> strings = list.Select(item => item.Name);

            //foreach (var item in strings)
            //{
            //    Console.WriteLine(item);
            //}


            //DEsceding by marks
            IEnumerable<Student> students = list.OrderByDescending(item => item.Marks);
            Student studentsTopper = list.OrderByDescending(item => item.Marks).First();


            Console.WriteLine("Topper");
            Console.WriteLine(studentsTopper.Name);

            //foreach (var student in students)
            //{
            //    Console.WriteLine(student.Id);
            //    Console.WriteLine(student.Name);
            //    Console.WriteLine(student.Marks);
            //    Console.WriteLine("\n\n");
            //}




            Console.ReadKey();
        }
    }
}
