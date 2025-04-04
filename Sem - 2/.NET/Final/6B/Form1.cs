using System;
using System.Windows.Forms;

namespace _6B
{
    public partial class Form1 : Form
    {
        static double n1 = 0, n2 = 0, total = 0;
        static string operation = "";

        public Form1()
        {
            InitializeComponent();
        }

        private void b7_Click(object sender, EventArgs e)
        {
            if (label1.Text.Length < 10)
            {
                label1.Text += "7";
            }
        }

        private void b8_Click(object sender, EventArgs e)
        {
            if (label1.Text.Length < 10)
            {
                label1.Text += "8";
            }
        }

        private void b9_Click(object sender, EventArgs e)
        {
            if (label1.Text.Length < 10)
            {
                label1.Text += "9";
            }
        }

        private void b4_Click(object sender, EventArgs e)
        {
            if (label1.Text.Length < 10)
            {
                label1.Text += "4";
            }
        }

        private void b5_Click(object sender, EventArgs e)
        {
            if (label1.Text.Length < 10)
            {
                label1.Text += "5";
            }
        }

        private void b6_Click(object sender, EventArgs e)
        {
            if (label1.Text.Length < 10)
            {
                label1.Text += "6";
            }
        }

        private void b1_Click(object sender, EventArgs e)
        {
            if (label1.Text.Length < 10)
            {
                label1.Text += "1";
            }
        }

        private void b2_Click(object sender, EventArgs e)
        {
            if (label1.Text.Length < 10)
            {
                label1.Text += "2";
            }
        }

        private void button10_Click(object sender, EventArgs e)
        {
            if (label1.Text.Length < 10)
            {
                label1.Text += "3";
            }
        }

        private void b0_Click(object sender, EventArgs e)
        {
            if (label1.Text.Length < 10)
            {
                label1.Text += "0";
            }
        }

        private void add_Click(object sender, EventArgs e)
        {
            if (label1.Text != "")
            {
                n1 = Convert.ToDouble(label1.Text);
                label1.Text = "";
                operation = "+";
            }
        }

        private void sub_Click(object sender, EventArgs e)
        {
            if (label1.Text != "")
            {
                n1 = Convert.ToDouble(label1.Text);
                label1.Text = "";
                operation = "-";
            }
        }

        private void mul_Click(object sender, EventArgs e)
        {
            if (label1.Text != "")
            {
                n1 = Convert.ToDouble(label1.Text);
                label1.Text = "";
                operation = "*";
            }
        }

        private void div_Click(object sender, EventArgs e)
        {
            if (label1.Text != "")
            {
                n1 = Convert.ToDouble(label1.Text);
                label1.Text = "";
                operation = "/";
            }
        }

        private void eq_Click_1(object sender, EventArgs e)
        {
            if (label1.Text != "")
            {
                n2 = Convert.ToDouble(label1.Text);
                switch (operation)
                {
                    case "+":
                        total = n1 + n2;
                        break;
                    case "-":
                        total = n1 - n2;
                        break;
                    case "*":
                        total = n1 * n2;
                        break;
                    case "/":
                        if (n2 != 0)
                            total = n1 / n2;
                        else
                            label1.Text = "Error";
                        break;
                }
                label1.Text = total.ToString();
                n1 = total;  // To chain calculations
                n2 = 0;      // Reset n2
                operation = "";
            }
        }

        private void eq_Click(object sender, EventArgs e)
        {
            
        }

        private void cls_Click(object sender, EventArgs e)
        {
            n1 = 0;
            n2 = 0;
            label1.Text = "";
            operation = "";
        }
    }
}
