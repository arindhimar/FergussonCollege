using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Runtime.Remoting.Messaging;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CRUDusingListinForms
{



    public partial class Form1 : Form
    {
        static List<student> students = new List<student>();

        static int tempId = 0;


        public Form1()
        {
            InitializeComponent();
        }

        private void btnAdd_Click(object sender, EventArgs e)
        {
            students.Add(new student(++tempId,txtName.Text,int.Parse(txtMarks.Text)));


            listBox1.Items.Clear();



            foreach (student item in students)
            {
                listBox1.Items.Add(item);
            }

        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            //-1 
            /*if (listBox1.Items.Count > 0)
            {

            }
*/
            if (listBox1.SelectedIndex > -1)
            {

                if (listBox1.SelectedItem is student s)
                {
                    student temp = students.Where(st=>st.id == s.id).FirstOrDefault();

                    if (temp != null)
                    {
                        students.Remove(temp);

                        listBox1.Items.Clear();
                        foreach (student item in students)
                        {
                            listBox1.Items.Add(item);
                        }
                    }
                }
            }
        }

        private void btnupdate_Click(object sender, EventArgs e)
        {
            student temp = students.Where(st => st.id == int.Parse(txtId.Text)).FirstOrDefault();

            if (temp != null)
            {
                temp.name = txtName.Text;
                temp.marks = int.Parse(txtMarks.Text);

                listBox1.Items.Clear();
                foreach (student item in students)
                {
                    listBox1.Items.Add(item);
                }
            }

        }
    }
}
