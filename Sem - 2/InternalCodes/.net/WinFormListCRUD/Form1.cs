using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Xml.Linq;

namespace WinFormListCRUD
{
    public partial class Form1 : Form
    {
        static private List<Student> students = new List<Student>();

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (txtsid.Text.Length == 0 || txtsname.Text.Length == 0 || textBox2xtsage.Text.Length == 0)
            {
                MessageBox.Show("Empty Fields!!");
            }
            else
            {
                Student tempStudent = new Student(int.Parse(txtsid.Text),txtsname.Text,int.Parse(textBox2xtsage.Text));
                students.Add(tempStudent);
                txtsid.Text = "";
                txtsname.Text = "";
                textBox2xtsage.Text = "";
                RefreshData();
                MessageBox.Show("Data Added!!");
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (txtsid.Text.Length == 0 || txtsname.Text.Length == 0 || textBox2xtsage.Text.Length == 0)
            {
                MessageBox.Show("Empty Fields!!");
            }
            else
            {
                Student tempNewStudent = new Student(int.Parse(txtsid.Text), txtsname.Text, int.Parse(textBox2xtsage.Text));
                
                Student tempOldStudent = students.Where(s=>s.sid== tempNewStudent.sid).FirstOrDefault();

                if (tempOldStudent != null)
                {
                    students.Remove(tempOldStudent);
                    students.Add(tempNewStudent);
                    RefreshData();
                }
                else
                {
                    MessageBox.Show("No matching id found!!");
                }

            }
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (listBox1.SelectedItem is Student selectedStudent)
            {
                txtsid.Text = selectedStudent.sid.ToString();
                txtsname.Text = selectedStudent.sname.ToString();
                textBox2xtsage.Text = selectedStudent.sage.ToString();
            }

        }

        private void RefreshData()
        {
            listBox1.Items.Clear();
            if (!students.Any())
            {
                return;
            }

            foreach (Student student in students)
            {
                listBox1.Items.Add(student);
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (txtsid.Text.Length == 0 || txtsname.Text.Length == 0 || textBox2xtsage.Text.Length == 0)
            {
                MessageBox.Show("Empty Fields!!");
            }
            else
            {
                Student tempNewStudent = new Student(int.Parse(txtsid.Text), txtsname.Text, int.Parse(textBox2xtsage.Text));
                if (students.Count>0)
                {
                    Student tempOldStudent = students.Where(s => s.sid == int.Parse(txtsid.Text)).FirstOrDefault();
                    if (tempNewStudent!=null)
                    {
                        students.Remove(tempOldStudent);
                        RefreshData();
                    }
                    else
                    {
                        MessageBox.Show("No data found!!");
                    }
                }
                else
                {
                    MessageBox.Show("Student list is empty!!");

                }
            }
        }
    }
}
