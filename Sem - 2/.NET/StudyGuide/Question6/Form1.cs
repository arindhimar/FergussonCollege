using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Question6
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void txtTotal_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if(txtPrice.Text !=""&& Convert.ToInt64(txtPrice.Text)>0 && txtDiscount.Text != "" && Convert.ToInt64(txtDiscount.Text) > -1 && Convert.ToInt64(txtDiscount.Text) < 100)
            {
                int total = Convert.ToInt32(txtPrice.Text) - Convert.ToInt32(txtPrice.Text) * Convert.ToInt32(txtDiscount.Text)/100;
                listBox1.Items.Add(total.ToString());
                int temp = Convert.ToInt32(txtTotal.Text);
                int finaltemp = temp + Convert.ToInt32(total);
                MessageBox.Show(finaltemp.ToString());
                txtTotal.Text = finaltemp.ToString() ;
            }
        }
    }
}
