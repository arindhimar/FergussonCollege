using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CRUDInWinForm
{
    public class Student
    {
        public int id;
        public string Name;
        public int marks;

        public Student(int id, string name, int marks)
        {
            this.id = id;
            Name = name;
            this.marks = marks;
        }

        public override string ToString()
        {
            return "Id : " + id + " Name : " + Name + " Marks : " + marks;
        }
    }
}
