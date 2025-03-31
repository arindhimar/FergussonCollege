using System;
using System.Collections.Generic;
using System.Linq;

namespace Question8
{
    internal class Program
    {
        class Student
        {
            public string Name { get; set; }
            public int Age { get; set; }
            public double Grade { get; set; }
        }

        static void Main(string[] args)
        {
            List<Student> students = new List<Student>
            {
                new Student { Name = "Arin Dhimar", Age = 22, Grade = 88.5 },
                new Student { Name = "CodePraxis", Age = 21, Grade = 75.0 },
                new Student { Name = "Animex", Age = 23, Grade = 92.3 },
                new Student { Name = "SayIt", Age = 20, Grade = 85.4 },
                new Student { Name = "CommitBridge", Age = 24, Grade = 78.9 }
            };

            var highScorers = from student in students
                              where student.Grade > 80
                              select student;
            Console.WriteLine("Students with grades above 80:");
            foreach (var student in highScorers)
            {
                Console.WriteLine($"{student.Name} - {student.Grade}");
            }

            var sortedStudents = from student in students
                                 orderby student.Grade descending
                                 select student;
            Console.WriteLine("\nStudents sorted by grades:");
            foreach (var student in sortedStudents)
            {
                Console.WriteLine($"{student.Name} - {student.Grade}");
            }

            var groupedByAge = from student in students
                               group student by student.Age >= 22 ? "Older" : "Younger";
            Console.WriteLine("\nStudents grouped by age:");
            foreach (var group in groupedByAge)
            {
                Console.WriteLine($"{group.Key}:");
                foreach (var student in group)
                {
                    Console.WriteLine($"  {student.Name} - Age: {student.Age}");
                }
            }

            double averageGrade = students.Average(s => s.Grade);
            Console.WriteLine("\nAverage Grade: " + averageGrade);
        }
    }
}
