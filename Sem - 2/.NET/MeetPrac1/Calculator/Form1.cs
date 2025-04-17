using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Calculator
{
    public partial class Form1 : Form
    {
        int n1=0, n2=0;
        string operators="";
        public Form1()
        {
            InitializeComponent();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            if (label1.Text.Length < 10)
            {
                label1.Text += "8";
                if (operators == "")
                {
                    n1 = 8;
                }
                else
                {
                    n2 = 8;
                }
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            if (label1.Text.Length < 10)
            {
                label1.Text += "7";
                if (operators == "")
                {
                    n1 = 7;
                }
                else
                {
                    n2 = 7;
                }
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            if (label1.Text.Length < 10)
            {
                label1.Text += "9";
                if (operators == "")
                {
                    n1 = 9;
                }
                else
                {
                    n2 = 9;
                }
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (label1.Text.Length < 10)
            {
                label1.Text += "4";
                if (operators == "")
                {
                    n1 = 4;
                }
                else
                {
                    n2 = 4;
                }
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            if (label1.Text.Length < 10)
            {
                label1.Text += "5";
                if (operators == "")
                {
                    n1 = 5;
                }
                else
                {
                    n2 = 5;
                }
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            if (label1.Text.Length < 10)
            {
                label1.Text += "6";
                if (operators == "")
                {
                    n1 = 6;
                }
                else
                {
                    n2 = 6;
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (label1.Text.Length < 10)
            {
                label1.Text += "1";
                if (operators == "")
                {
                    n1 = 1;
                }
                else
                {
                    n2 = 1;
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (label1.Text.Length < 10)
            {
                label1.Text += "2";
                if (operators == "")
                {
                    n1 = 2;
                }
                else
                {
                    n2 = 2;
                }
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (label1.Text.Length < 10)
            {
                label1.Text += "3";
                if (operators == "")
                {
                    n1 = 3;
                }
                else
                {
                    n2 = 3;
                }
            }
        }

        private void button0_Click(object sender, EventArgs e)
        {
            if (label1.Text.Length < 10)
            {
                label1.Text += "0";
                if (operators == "")
                {
                    n1 = 0;
                }
                else
                {
                    n2 = 0;
                }
            }
        }

        private void buttonclr_Click(object sender, EventArgs e)
        {
            n1 = 0;
            n2 = 0;
            operators = "";
            label1.Text = "";
        }

        private void button13_Click(object sender, EventArgs e)
        {
            operators = "*";
            label1.Text = "";

        }

        private void button14_Click(object sender, EventArgs e)
        {
            if (operators == "+")
            {
                label1.Text = (n1+n2).ToString();
            }
            else if (operators == "-")
            {
                label1.Text = (n1 - n2).ToString();
            }
            else if (operators == "*")
            {
                label1.Text = (n1 * n2).ToString();
            }
            else if (operators == "/")
            {
                label1.Text = (n1 / n2).ToString();
            }

            operators = "";

        }

        private void button12_Click(object sender, EventArgs e)
        {
            operators = "/";
            label1.Text = "";


        }

        private void button11_Click(object sender, EventArgs e)
        {
            label1.Text = "";

            operators = "-";

        }

        private void button10_Click(object sender, EventArgs e)
        {
            operators = "+";
            label1.Text = "";
        }
    }
}
