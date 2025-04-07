using System;
using System.Collections.Generic;
using System.Linq;

namespace _11bc
{
    public class Student
    {
        public int Sid { get; set; }
        public string Sname { get; set; }
        public int Marks { get; set; }
    }

    internal class Program
    {
        static List<Student> students = new List<Student>
        {
            new Student { Sid = 1, Sname = "Arin", Marks = 85 },
            new Student { Sid = 2, Sname = "Mira", Marks = 92 },
            new Student { Sid = 3, Sname = "Jay", Marks = 76 },
            new Student { Sid = 4, Sname = "Neha", Marks = 89 },
            new Student { Sid = 5, Sname = "Karan", Marks = 68 }
        };

        static void Main(string[] args)
        {
            int choice;

            do
            {
                Console.Clear();
                Console.WriteLine("======= College Student Management =======");
                Console.WriteLine("1. View All Students (JSON-like)");
                Console.WriteLine("2. View Toppers (Marks >= 80)");
                Console.WriteLine("3. Add New Student");
                Console.WriteLine("4. Search Student by Name");
                Console.WriteLine("5. Update Marks by ID");
                Console.WriteLine("6. Delete Student by ID");
                Console.WriteLine("7. Sort by Marks (Descending)");
                Console.WriteLine("8. Exit");
                Console.Write("Enter your choice: ");

                if (!int.TryParse(Console.ReadLine(), out choice))
                {
                    Console.WriteLine("Invalid input. Press Enter to continue...");
                    Console.ReadLine();
                    continue;
                }

                switch (choice)
                {
                    case 1:
                        ViewAllStudents();
                        break;
                    case 2:
                        ViewToppers();
                        break;
                    case 3:
                        AddStudent();
                        break;
                    case 4:
                        SearchByName();
                        break;
                    case 5:
                        UpdateMarks();
                        break;
                    case 6:
                        DeleteStudent();
                        break;
                    case 7:
                        SortByMarks();
                        break;
                    case 8:
                        Console.WriteLine("Exiting...");
                        break;
                    default:
                        Console.WriteLine("Invalid choice. Try again.");
                        break;
                }

                if (choice != 8)
                {
                    Console.WriteLine("\nPress Enter to return to menu...");
                    Console.ReadLine();
                }

            } while (choice != 8);
        }

        static void ViewAllStudents()
        {
            Console.WriteLine("\n--- All Students (JSON-like format) ---");
            Console.WriteLine("[");
            for (int i = 0; i < students.Count; i++)
            {
                var s = students[i];
                Console.WriteLine($"  {{ \"Sid\": {s.Sid}, \"Sname\": \"{s.Sname}\", \"Marks\": {s.Marks} }}{(i < students.Count - 1 ? "," : "")}");
            }
            Console.WriteLine("]");
        }

        static void ViewToppers()
        {
            Console.WriteLine("\n--- Toppers (Marks >= 80, JSON-like format) ---");
            var toppers = students.Where(s => s.Marks >= 80).OrderByDescending(s => s.Marks).ToList();

            Console.WriteLine("[");
            for (int i = 0; i < toppers.Count; i++)
            {
                var s = toppers[i];
                Console.WriteLine($"  {{ \"Sid\": {s.Sid}, \"Sname\": \"{s.Sname}\", \"Marks\": {s.Marks} }}{(i < toppers.Count - 1 ? "," : "")}");
            }
            Console.WriteLine("]");
        }

        static void AddStudent()
        {
            Console.Write("Enter Student Name: ");
            string name = Console.ReadLine();

            Console.Write("Enter Marks: ");
            if (int.TryParse(Console.ReadLine(), out int marks))
            {
                int newId = students.Count > 0 ? students.Max(s => s.Sid) + 1 : 1;
                students.Add(new Student { Sid = newId, Sname = name, Marks = marks });
                Console.WriteLine("Student added successfully.");
            }
            else
            {
                Console.WriteLine("Invalid marks input.");
            }
        }

        static void SearchByName()
        {
            Console.Write("Enter name to search: ");
            string name = Console.ReadLine();

            var results = students.Where(s => s.Sname.ToLower().Contains(name.ToLower())).ToList();

            if (results.Count == 0)
            {
                Console.WriteLine("No students found.");
                return;
            }

            Console.WriteLine("\n--- Search Results ---");
            foreach (var s in results)
            {
                Console.WriteLine($"  {{ \"Sid\": {s.Sid}, \"Sname\": \"{s.Sname}\", \"Marks\": {s.Marks} }}");
            }
        }

        static void UpdateMarks()
        {
            Console.Write("Enter Student ID to update: ");
            if (int.TryParse(Console.ReadLine(), out int id))
            {
                var student = students.FirstOrDefault(s => s.Sid == id);
                if (student == null)
                {
                    Console.WriteLine("Student not found.");
                    return;
                }

                Console.Write("Enter new marks: ");
                if (int.TryParse(Console.ReadLine(), out int newMarks))
                {
                    student.Marks = newMarks;
                    Console.WriteLine("Marks updated.");
                }
                else
                {
                    Console.WriteLine("Invalid marks.");
                }
            }
        }

        static void DeleteStudent()
        {
            Console.Write("Enter Student ID to delete: ");
            if (int.TryParse(Console.ReadLine(), out int id))
            {
                var student = students.FirstOrDefault(s => s.Sid == id);
                if (student == null)
                {
                    Console.WriteLine("Student not found.");
                    return;
                }

                students.Remove(student);
                Console.WriteLine("Student deleted.");
            }
        }

        static void SortByMarks()
        {
            Console.WriteLine("\n--- Students Sorted by Marks (Descending) ---");
            var sorted = students.OrderByDescending(s => s.Marks).ToList();

            Console.WriteLine("[");
            for (int i = 0; i < sorted.Count; i++)
            {
                var s = sorted[i];
                Console.WriteLine($"  {{ \"Sid\": {s.Sid}, \"Sname\": \"{s.Sname}\", \"Marks\": {s.Marks} }}{(i < sorted.Count - 1 ? "," : "")}");
            }
            Console.WriteLine("]");
        }
    }
}
