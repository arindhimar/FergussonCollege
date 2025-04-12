using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;
using System.Xml.Linq;

namespace WinFormListCRUD
{
    public class Student
    {
        public int sid;
        public string sname;
        public int sage;

        public Student(int sid, string sname, int sage)
        {
            this.sid = sid;
            this.sname = sname;
            this.sage = sage;
        }

        public override string ToString()
        {
            return $"ID: {sid}, Name: {sname}, Age: {sage}";
        }

    }
}
