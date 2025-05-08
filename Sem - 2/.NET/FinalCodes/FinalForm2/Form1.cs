using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Security.Policy;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace FinalForm2
{
    public partial class Form1 : Form
    {
        public static List<string> list = new List<string>();

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            list.Add(textBox1.Text);

            listBox1.Items.Clear();
            foreach (var item in list)
            {
                listBox1.Items.Add(item);
            }

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {
            if(textBox2.Text.Length > 0)
            {
                listBox1.Items.Clear();
                foreach (var item in list)
                {
                    if (item == textBox2.Text)
                    {
                        listBox1.Items.Add(item);
                    }
                }

            }
            else
            {
                listBox1.Items.Clear();
                foreach (var item in list)
                {
                    listBox1.Items.Add(item);
                }
            }
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            list.Remove(listBox1.SelectedItem.ToString());
            listBox1.Items.Clear();
            foreach (var item in list)
            {
                listBox1.Items.Add(item);
            }
        }

    }
}
