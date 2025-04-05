using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace TshirtPriceCalc
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (txtSize.SelectedIndex > -1 && Convert.ToInt64(txtNo.Text.ToString())>0)
            {
                int noOfTshirt = Convert.ToInt16(txtNo.Text.ToString());

                double total = 0;

                if (txtSize.SelectedIndex == 0)
                {
                    total = 150 * noOfTshirt;
                }
                else if (txtSize.SelectedIndex == 1)
                {
                    total = 175 * noOfTshirt;
                }
                else if(txtSize.SelectedIndex == 2)
                {
                    total = 250 * noOfTshirt;
                }

                total += total * 0.09;

                if(txtPromoCode.Text== "TRUEBLUE")
                {
                    total -= total * 0.10;
                }

                txtPrice.Text = total.ToString();



            }
        }
    }
}
