using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Calc2
{
    public partial class Form1 : Form
    {
        public double n1 = 0, n2 = 0;
        public string operation = "";
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (txtDisp.Text.Length < 10)
            {
                txtDisp.Text += 1;
            }
        }

        private void button0_Click(object sender, EventArgs e)
        {
            if (txtDisp.Text.Length < 10)
            {
                txtDisp.Text += 0;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (txtDisp.Text.Length < 10)
            {
                txtDisp.Text += 2;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (txtDisp.Text.Length < 10)
            {
                txtDisp.Text += 3;
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (txtDisp.Text.Length < 10)
            {
                txtDisp.Text += 4;
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            if (txtDisp.Text.Length < 10)
            {
                txtDisp.Text += 5;
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            if (txtDisp.Text.Length < 10)
            {
                txtDisp.Text += 6;
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            if (txtDisp.Text.Length < 10)
            {
                txtDisp.Text += 7;
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            if (txtDisp.Text.Length < 10)
            {
                txtDisp.Text += 8;
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            if (txtDisp.Text.Length < 10)
            {
                txtDisp.Text += 9;
            }
        }

        private void buttonPls_Click(object sender, EventArgs e)
        {
            if (n1 == 0 && txtDisp.Text.Length>0)
            {
                n1 = Convert.ToDouble(txtDisp.Text);
                operation = "+";
                txtDisp.Text = "";
            }
        }

        private void buttonMin_Click(object sender, EventArgs e)
        {
            if (n1 == 0 && txtDisp.Text.Length > 0)
            {
                n1 = Convert.ToDouble(txtDisp.Text);
                operation = "-";
                txtDisp.Text = "";

            }
        }

        private void buttonMul_Click(object sender, EventArgs e)
        {
            if (n1 == 0 && txtDisp.Text.Length > 0)
            {
                n1 = Convert.ToDouble(txtDisp.Text);
                operation = "*";
                txtDisp.Text = "";

            }
        }

        private void buttonDiv_Click(object sender, EventArgs e)
        {
            if (n1 == 0 && txtDisp.Text.Length > 0)
            {
                n1 = Convert.ToDouble(txtDisp.Text);
                operation = "/";
                txtDisp.Text = "";

            }
        }

        private void buttonCls_Click(object sender, EventArgs e)
        {
            n1 = 0;
            n2 = 0;
            operation = "";
            txtDisp.Text = "";
        }

        private void buttonEq_Click(object sender, EventArgs e)
        {
            if (txtDisp.Text.Length > 0 && n1 != 0)
            {
                n2 = Convert.ToDouble(txtDisp.Text);
                txtDisp.Text = "";

                if (operation == "+")
                {
                    txtDisp.Text = (n1 + n2).ToString();
                }
                else if (operation == "-")
                {
                    txtDisp.Text = (n1 - n2).ToString();
                }
                else if (operation == "*")
                {
                    txtDisp.Text = (n1 * n2).ToString();
                }
                else if (operation == "/")
                {
                    txtDisp.Text = (n1 / n2).ToString();
                }


            }
        }
    }
}
