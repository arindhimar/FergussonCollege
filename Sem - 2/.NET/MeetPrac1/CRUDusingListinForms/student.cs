using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CRUDusingListinForms
{
    public class student
    {
        public int id;
        public string name;
        public int marks;

        public student(int id, string name, int marks)
        {
            this.id = id;
            this.name = name;
            this.marks = marks;
        }


        public override string ToString()
        {
            return "Id:"+id+"name:"+name+"marks:"+marks;
        }

    }
}
