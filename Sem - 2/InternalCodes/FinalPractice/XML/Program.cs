using System;
using System.Linq;
using System.Xml.Linq;

namespace XML
{
    internal class Program
    {
        static XDocument xmlDoc = new XDocument(new XElement("Employees"));

        static void Main(string[] args)
        {
            bool running = true;

            while (running)
            {
                Console.WriteLine("\n=== Employee XML Manager ===");
                Console.WriteLine("1. Add Employee");
                Console.WriteLine("2. View All Employees");
                Console.WriteLine("3. Search Employee by Name");
                Console.WriteLine("4. Update Employee Name");
                Console.WriteLine("5. Delete Employee");
                Console.WriteLine("6. Exit");
                Console.Write("Choose an option: ");

                switch (Console.ReadLine())
                {
                    case "1":
                        AddEmployee();
                        break;
                    case "2":
                        ViewEmployees();
                        break;
                    case "3":
                        SearchEmployee();
                        break;
                    case "4":
                        UpdateEmployee();
                        break;
                    case "5":
                        DeleteEmployee();
                        break;
                    case "6":
                        running = false;
                        break;
                    default:
                        Console.WriteLine("❌ Invalid choice.");
                        break;
                }
            }
        }

        static void AddEmployee()
        {
            Console.Write("Enter Employee Name: ");
            string name = Console.ReadLine();

            XElement emp = new XElement("Employee",
                new XElement("Name", name)
            );

            xmlDoc.Root.Add(emp);
            Console.WriteLine("✅ Employee added.");
        }

        static void ViewEmployees()
        {
            Console.WriteLine("\n📃 All Employees:");
            var employees = xmlDoc.Descendants("Employee");

            if (!employees.Any())
            {
                Console.WriteLine("No employees found.");
                return;
            }

            foreach (var emp in employees)
            {
                Console.WriteLine("- " + emp.Element("Name")?.Value);
            }
        }

        static void SearchEmployee()
        {
            Console.Write("🔍 Enter name to search: ");
            string searchName = Console.ReadLine();

            var matches = xmlDoc.Descendants("Employee")
                .Where(e => (string)e.Element("Name") == searchName);

            if (matches.Any())
            {
                Console.WriteLine("✅ Employee(s) found:");
                foreach (var emp in matches)
                {
                    Console.WriteLine("- " + emp.Element("Name")?.Value);
                }
            }
            else
            {
                Console.WriteLine("❌ No match found.");
            }
        }

        static void UpdateEmployee()
        {
            Console.Write("✏️ Enter current name to update: ");
            string current = Console.ReadLine();

            var emp = xmlDoc.Descendants("Employee")
                .FirstOrDefault(e => (string)e.Element("Name") == current);

            if (emp != null)
            {
                Console.Write("Enter new name: ");
                string newName = Console.ReadLine();
                emp.SetElementValue("Name", newName);
                Console.WriteLine("✅ Name updated.");
            }
            else
            {
                Console.WriteLine("❌ Employee not found.");
            }
        }

        static void DeleteEmployee()
        {
            Console.Write("🗑️ Enter name to delete: ");
            string name = Console.ReadLine();

            var emp = xmlDoc.Descendants("Employee")
                .FirstOrDefault(e => (string)e.Element("Name") == name);

            if (emp != null)
            {
                emp.Remove();
                Console.WriteLine("✅ Employee deleted.");
            }
            else
            {
                Console.WriteLine("❌ Employee not found.");
            }
        }
    }
}
