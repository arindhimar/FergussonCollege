using System;
using System.Collections.Generic;
using System.Linq;

namespace ListConsoleCRUD
{
    class Student
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public int Age { get; set; }
    }

    internal class Program
    {
        static List<Student> students = new List<Student>();

        static void Main(string[] args)
        {
            int choice;
            do
            {
                Console.Clear();
                Console.WriteLine("Student CRUD Operations");
                Console.WriteLine("1. Add Student");
                Console.WriteLine("2. View Students");
                Console.WriteLine("3. Update Student");
                Console.WriteLine("4. Delete Student");
                Console.WriteLine("5. Exit");
                Console.Write("Enter your choice: ");

                if (!int.TryParse(Console.ReadLine(), out choice)) continue;

                switch (choice)
                {
                    case 1:
                        AddStudent();
                        break;
                    case 2:
                        ViewStudents();
                        break;
                    case 3:
                        UpdateStudent();
                        break;
                    case 4:
                        DeleteStudent();
                        break;
                    case 5:
                        Console.WriteLine("Exiting...");
                        break;
                    default:
                        Console.WriteLine("Invalid choice. Try again.");
                        break;
                }

                Console.WriteLine("\nPress any key to continue...");
                Console.ReadKey();

            } while (choice != 5);
        }

        static void AddStudent()
        {
            Console.Write("Enter ID: ");
            int id = int.Parse(Console.ReadLine());

            Console.Write("Enter Name: ");
            string name = Console.ReadLine();

            Console.Write("Enter Age: ");
            int age = int.Parse(Console.ReadLine());

            students.Add(new Student { Id = id, Name = name, Age = age });
            Console.WriteLine("Student added successfully.");
        }

        static void ViewStudents()
        {
            Console.WriteLine("\n--- Student List ---");
            foreach (var student in students)
            {
                Console.WriteLine($"ID: {student.Id}, Name: {student.Name}, Age: {student.Age}");
            }

            if (!students.Any())
            {
                Console.WriteLine("No students found.");
            }
        }

        static void UpdateStudent()
        {
            Console.Write("Enter ID of student to update: ");
            int id = int.Parse(Console.ReadLine());

            var student = students.FirstOrDefault(s => s.Id == id);
            if (student != null)
            {
                Console.Write("Enter new name: ");
                student.Name = Console.ReadLine();

                Console.Write("Enter new age: ");
                student.Age = int.Parse(Console.ReadLine());

                Console.WriteLine("Student updated successfully.");
            }
            else
            {
                Console.WriteLine("Student not found.");
            }
        }

        static void DeleteStudent()
        {
            Console.Write("Enter ID of student to delete: ");
            int id = int.Parse(Console.ReadLine());

            var student = students.FirstOrDefault(s => s.Id == id);
            if (student != null)
            {
                students.Remove(student);
                Console.WriteLine("Student deleted successfully.");
            }
            else
            {
                Console.WriteLine("Student not found.");
            }
        }
    }
}
