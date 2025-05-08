using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace TshirtFORM
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int no = int.Parse(textBox1.Text);


            double price = 0;


            if (comboBox1.SelectedIndex == 0)
            {

                price = (no * 250) ;
            }
            else if (comboBox1.SelectedIndex == 1)
            {
                price = (no * 500);

            }

            if (textBox2.Text == "lol")
            {
                MessageBox.Show(((price) - (0.05 * price)).ToString());
            }
            else
            {
                MessageBox.Show(((price)).ToString());
            }


        }
    }
}
