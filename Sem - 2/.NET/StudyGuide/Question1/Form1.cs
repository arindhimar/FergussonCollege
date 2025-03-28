using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Question1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            string temp = todoText.Text;
            //MessageBox.Show(temp);

            todoList.Items.Add(temp);

            todoText.Text = "";

        }

        private void todoList_SelectedIndexChanged(object sender, EventArgs e)
        {
            //MessageBox.Show(todoList.SelectedIndex.ToString());
            if (todoList.SelectedIndex != -1)
            {
                todoList.Items.RemoveAt(todoList.SelectedIndex);
            }
        }
    }
}
