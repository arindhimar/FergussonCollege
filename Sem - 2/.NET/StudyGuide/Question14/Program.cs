using System;
using System.Collections.Generic;
using System.Linq;

namespace Question14
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Dictionary<int, Student> students = new Dictionary<int, Student>
            {
                { 1, new Student(1, "Arin", 23, "A") },
                { 2, new Student(2, "Darshan", 22, "B") },
                { 3, new Student(3, "Vasu", 24, "A") },
                { 4, new Student(4, "Sneha", 21, "C") },
                { 5, new Student(5, "Bansi", 25, "B") },
                { 6, new Student(6, "Pratigna", 23, "A") }
            };

            while (true)
            {
                Console.WriteLine("\nMenu:");
                Console.WriteLine("1. Display All Students");
                Console.WriteLine("2. Display Students by Grade");
                Console.WriteLine("3. Search Student by ID");
                Console.WriteLine("4. Sort Students by Age");
                Console.WriteLine("5. Display Average Age");
                Console.WriteLine("6. Display Grade-wise Student Count");
                Console.WriteLine("7. Display Youngest and Oldest Students");
                Console.WriteLine("8. Group Students by Grade");
                Console.WriteLine("9. Exit");
                Console.Write("Enter your choice: ");

                if (!int.TryParse(Console.ReadLine(), out int choice))
                {
                    Console.WriteLine("Invalid input. Please enter a number.");
                    continue;
                }

                switch (choice)
                {
                    case 1:
                        DisplayAllStudents(students);
                        break;
                    case 2:
                        Console.Write("Enter Grade to filter: ");
                        string grade = Console.ReadLine().ToUpper();
                        DisplayStudentsByGrade(students, grade);
                        break;
                    case 3:
                        SearchStudentById(students);
                        break;
                    case 4:
                        SortStudentsByAge(students);
                        break;
                    case 5:
                        DisplayAverageAge(students);
                        break;
                    case 6:
                        DisplayGradeWiseCount(students);
                        break;
                    case 7:
                        DisplayYoungestAndOldestStudents(students);
                        break;
                    case 8:
                        GroupStudentsByGrade(students);
                        break;
                    case 9:
                        return;
                    default:
                        Console.WriteLine("Invalid choice. Please try again.");
                        break;
                }
            }
        }

        static void DisplayAllStudents(Dictionary<int, Student> students)
        {
            Console.WriteLine("\nAll Students:");
            foreach (var student in students.Values)
            {
                Console.WriteLine(student);
            }
        }

        static void DisplayStudentsByGrade(Dictionary<int, Student> students, string grade)
        {
            Console.WriteLine($"\nStudents with Grade {grade}:");
            var filteredStudents = students.Values.Where(s => s.Grade == grade);
            foreach (var student in filteredStudents)
            {
                Console.WriteLine(student);
            }
        }

        static void SearchStudentById(Dictionary<int, Student> students)
        {
            Console.Write("\nEnter student ID to search: ");
            if (int.TryParse(Console.ReadLine(), out int searchId) && students.TryGetValue(searchId, out Student foundStudent))
            {
                Console.WriteLine("Student Found: " + foundStudent);
            }
            else
            {
                Console.WriteLine("Student not found.");
            }
        }

        static void SortStudentsByAge(Dictionary<int, Student> students)
        {
            Console.WriteLine("\nStudents sorted by Age:");
            var sortedStudents = students.Values.OrderBy(s => s.Age);
            foreach (var student in sortedStudents)
            {
                Console.WriteLine(student);
            }
        }

        static void DisplayAverageAge(Dictionary<int, Student> students)
        {
            double averageAge = students.Values.Average(s => s.Age);
            Console.WriteLine($"\nAverage Age of Students: {averageAge:F2}");
        }

        static void DisplayGradeWiseCount(Dictionary<int, Student> students)
        {
            Console.WriteLine("\nStudent count by Grade:");
            var gradeCount = students.Values.GroupBy(s => s.Grade).Select(g => new { Grade = g.Key, Count = g.Count() });
            foreach (var entry in gradeCount)
            {
                Console.WriteLine($"Grade {entry.Grade}: {entry.Count} students");
            }
        }

        static void DisplayYoungestAndOldestStudents(Dictionary<int, Student> students)
        {
            var youngest = students.Values.OrderBy(s => s.Age).First();
            var oldest = students.Values.OrderByDescending(s => s.Age).First();
            Console.WriteLine($"\nYoungest Student: {youngest}");
            Console.WriteLine($"Oldest Student: {oldest}");
        }

        static void GroupStudentsByGrade(Dictionary<int, Student> students)
        {
            Console.WriteLine("\nGrouping Students by Grade:");
            var grouped = students.Values.GroupBy(s => s.Grade);
            foreach (var group in grouped)
            {
                Console.WriteLine($"Grade {group.Key}:");
                foreach (var student in group)
                {
                    Console.WriteLine($"  {student}");
                }
            }
        }
    }

    class Student
    {
        public int ID { get; set; }
        public string Name { get; set; }
        public int Age { get; set; }
        public string Grade { get; set; }

        public Student(int id, string name, int age, string grade)
        {
            ID = id;
            Name = name;
            Age = age;
            Grade = grade;
        }

        public override string ToString()
        {
            return $"ID: {ID}, Name: {Name}, Age: {Age}, Grade: {Grade}";
        }
    }
}
