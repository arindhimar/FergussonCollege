using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace _6A
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int noOfTshirt = 0;
            int comboBoxIndex = -1;
            string promoCode = "";

            if (textBox1.Text.Length > 0)
            {
                noOfTshirt = Convert.ToInt32(textBox1.Text.ToString());
                comboBoxIndex = comboBox1.SelectedIndex;
                promoCode = (textBox2.Text.ToString());

                //Count final price

                double total = 0;

                if (comboBoxIndex != -1)
                {
                    if (comboBoxIndex == 0)
                    {
                        total = noOfTshirt * 125;
                    }
                    else if (comboBoxIndex == 1)
                    {
                        total = noOfTshirt * 175;
                    }
                    else if (comboBoxIndex == 2)
                    {
                        total = noOfTshirt * 250;
                    }

                }

                total = total + (total * 0.09);


                //check for the promocode
                if (promoCode== "TRUEBLUE")
                {
                    total = total - (total * 0.1);
                }

                
                label5.Text = total.ToString();
            }





            /*MessageBox.Show(comboBoxIndex.ToString());*/
        }
    }
}
