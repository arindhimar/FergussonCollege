using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace OneShotDesktop
{
    public partial class Form1 : Form
    {

        public static int tempId = 0;

        public static List<Student> students = new List<Student>();

        public Form1()
        {
            InitializeComponent();
        }

        private void btnAdd_Click(object sender, EventArgs e)
        {
            students.Add(new Student(++tempId,txtName.Text,int.Parse(txtmarks.Text)));

            listBox1.Items.Clear();

            foreach (Student student in students)
            {
                listBox1.Items.Add(student);
            }
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (listBox1.SelectedIndex >= 0)
            {
                if (listBox1.SelectedItem is Student temp)
                {
                    txtId.Text = temp.Id.ToString();
                    txtName.Text = temp.Name.ToString();
                    txtmarks.Text = temp.Marks.ToString();
                }
            }
        }

        private void btnDelete_Click(object sender, EventArgs e)
        {
            Student temp = students.Where(s => s.Id == int.Parse(txtId.Text) && s.Name == txtName.Text && s.Marks == int.Parse(txtmarks.Text)).FirstOrDefault();

            if (temp != null)
            {
                students.Remove(temp);
                listBox1.Items.Clear();

                foreach (Student student in students)
                {
                    listBox1.Items.Add(student);
                }
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            
        }

        private void btnUpdate_Click(object sender, EventArgs e)
        {
            Student temp = students.Where(s => s.Id == int.Parse(txtId.Text)).FirstOrDefault();

            if (temp != null)
            {
                temp.Name = txtName.Text;
                temp.Marks = int.Parse(txtmarks.Text);
                listBox1.Items.Clear();

                foreach (Student student in students)
                {
                    listBox1.Items.Add(student);
                }
            }
        }
    }
}
