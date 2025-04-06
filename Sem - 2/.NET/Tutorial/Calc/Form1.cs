using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Calc
{
    public partial class Form1 : Form
    {
        
        public double n1=0, n2=0;

        public string operation="";

        public Form1()
        {
            InitializeComponent();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            if (txtDisplay.Text.Length < 10)
            {
                txtDisplay.Text +=6;
            }
        }

        private void btn7_Click(object sender, EventArgs e)
        {
            if (txtDisplay.Text.Length < 10)
            {
                txtDisplay.Text += 7;
            }
        }

        private void btn8_Click(object sender, EventArgs e)
        {
            if (txtDisplay.Text.Length < 10)
            {
                txtDisplay.Text += 8;
            }
        }

        private void btn9_Click(object sender, EventArgs e)
        {
            if (txtDisplay.Text.Length < 10)
            {
                txtDisplay.Text += 9;
            }
        }

        private void btn4_Click(object sender, EventArgs e)
        {
            if (txtDisplay.Text.Length < 10)
            {
                txtDisplay.Text += 4;
            }
        }

        private void btn5_Click(object sender, EventArgs e)
        {
            if (txtDisplay.Text.Length < 10)
            {
                txtDisplay.Text += 5;
            }
        }

        private void btn1_Click(object sender, EventArgs e)
        {
            if (txtDisplay.Text.Length < 10)
            {
                txtDisplay.Text += 1;
            }
        }

        private void btn2_Click(object sender, EventArgs e)
        {
            if (txtDisplay.Text.Length < 10)
            {
                txtDisplay.Text += 2;
            }
        }

        private void btn3_Click(object sender, EventArgs e)
        {
            if (txtDisplay.Text.Length < 10)
            {
                txtDisplay.Text += 3;
            }
        }

        private void btn0_Click(object sender, EventArgs e)
        {
            if (txtDisplay.Text.Length < 10)
            {
                txtDisplay.Text += 0;
            }
        }

        private void btnpls_Click(object sender, EventArgs e)
        {
            if (txtDisplay.Text.Length > 0)
            {
                if (n1 == 0)
                {
                    n1 = Convert.ToDouble(txtDisplay.Text);
                }
                    operation = "+";
                txtDisplay.Text = "";
            }
            
        }

        private void btnmin_Click(object sender, EventArgs e)
        {
            if (txtDisplay.Text.Length > 0)
            {
                if (n1 == 0)
                {
                    n1 = Convert.ToDouble(txtDisplay.Text);
                }
                operation = "-";
                txtDisplay.Text = "";

            }

        }

        private void btnmul_Click(object sender, EventArgs e)
        {
            if (txtDisplay.Text.Length > 0)
            {
                if (n1 == 0)
                {
                    n1 = Convert.ToDouble(txtDisplay.Text);
                }
                operation = "*";

                txtDisplay.Text = "";

            }

        }

        private void btneq_Click(object sender, EventArgs e)
        {
            if (txtDisplay.Text.Length > 0 && n1 != 0)
            {
                n2 = Convert.ToDouble(txtDisplay.Text);

                if (operation == "+")
                {
                    txtDisplay.Text = (n1 + n2).ToString();
                }
                else if (operation == "-")
                {
                    txtDisplay.Text = (n1 - n2).ToString();

                }
                else if (operation == "*")
                {
                    txtDisplay.Text = (n1 * n2).ToString();

                }
                else if (operation == "/")
                {
                    txtDisplay.Text = (n1 / n2).ToString();
                }
            }
        }

        private void btndiv_Click(object sender, EventArgs e)
        {
            if (txtDisplay.Text.Length > 0)
            {
                if (n1 == 0)
                {
                    n1 = Convert.ToDouble(txtDisplay.Text);
                }
                operation = "/";
                txtDisplay.Text = "";

            }
        }

        private void btncls_Click(object sender, EventArgs e)
        {
            n1 = 0;
            n2 = 0;
            operation = "";
            txtDisplay.Text = "";
        }
    }
}
