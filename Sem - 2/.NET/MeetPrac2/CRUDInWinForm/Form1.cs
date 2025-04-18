using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CRUDInWinForm
{
    public partial class Form1 : Form
    {

        List <Student> students = new List <Student> ();

        static int tempId = 0;

        public Form1()
        {
            InitializeComponent();
        }

 

        private void btnAdd_Click(object sender, EventArgs e)
        {

            Student tempojb = new Student(++tempId,txtName.Text,int.Parse(txtMarks.Text));

            students.Add(tempojb);


            listBox1.Items.Clear();
            foreach (Student student in students)
            {
                listBox1.Items.Add(student);
            }

        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

            if(listBox1.SelectedIndex > -1)
            {
                if(listBox1.SelectedItem is Student st)
                {
                    //MessageBox.Show(st.Name);
                    students.Remove(st);
                    listBox1.Items.Clear();
                    foreach (Student student in students)
                    {
                        listBox1.Items.Add(student);
                    }
                }
            }
        }

        private void btnEdit_Click(object sender, EventArgs e)
        {
            Student temp = students.Where(st=>st.id== tempId).FirstOrDefault();

            if (temp != null)
            {
                temp.Name = txtName.Text;
                temp.marks = int.Parse(txtMarks.Text);
                listBox1.Items.Clear();
                foreach (Student student in students)
                {
                    listBox1.Items.Add(student);
                }
            }
        }
    }
}
