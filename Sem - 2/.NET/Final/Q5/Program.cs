using System;

namespace Q5
{
    public interface IPerson
    {
        void DisplayInfo();
    }

    public class Person : IPerson
    {
        public string Name { get; set; }
        private int age;

        public Person(string name, int age)
        {
            Name = name;
            this.age = age;
        }

        static Person()
        {
            Console.WriteLine("Static constructor of Person called.");
        }

        private Person()
        {
            Name = "Unknown";
            age = 0;
        }

        public virtual void DisplayInfo()
        {
            Console.WriteLine($"Name: {Name}, Age: {age}");
        }

        public new void ShowDetails()
        {
            Console.WriteLine("This is a method in the Person class.");
        }
    }

    public class Employee : Person
    {
        public string JobTitle { get; set; }

        public Employee(string name, int age, string jobTitle)
            : base(name, age)
        {
            JobTitle = jobTitle;
        }

        public override void DisplayInfo()
        {
            base.DisplayInfo();
            Console.WriteLine($"Job Title: {JobTitle}");
        }

        public new void ShowDetails()
        {
            Console.WriteLine("This is a method in the Employee class.");
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            Person person = new Person("Arin DHimar", 30);
            person.DisplayInfo();
            person.ShowDetails();

            Employee employee = new Employee("Ashish", 25, "Software Developer");
            employee.DisplayInfo();
            employee.ShowDetails();

            Person personEmployee = new Employee("ALVF", 28, "Manager");
            personEmployee.ShowDetails();

            Console.ReadLine();
        }
    }
}
