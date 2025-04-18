using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OneShotDesktop
{
    public class Student
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public int Marks { get; set; }

        public Student(int id, string name, int marks)
        {
            Id = id;
            Name = name;
            Marks = marks;
        }

        public override string ToString()
        {
            return "Id : " + Id +" Name : "+Name+" Marks : "+Marks;
        }
    }
}
