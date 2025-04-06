using System;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace Q4final
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // ========== Event Publisher ==========
        public class College
        {
            public delegate void CollegeFestHandler(int visitors);
            public event CollegeFestHandler CollegeFest;

            public void StartFest(int visitors)
            {
                CollegeFest?.Invoke(visitors);
            }
        }

        // ========== Caterer (Subscriber) ==========
        public class Caterer
        {
            public void OnCollegeFest(int visitors)
            {
                int cateringCost = visitors * 200;
                MessageBox.Show($"Catering cost for {visitors} people is Rs.{cateringCost}", "Caterer");
            }
        }

        // ========== Decorator (Subscriber) ==========
        public class Decorator
        {
            public void OnCollegeFest(int visitors)
            {
                int decorationCost = 10000 + (10 * visitors);
                MessageBox.Show($"Decoration cost for {visitors} people is Rs.{decorationCost}", "Decorator");
            }
        }
        private void button1_Click_1(object sender, EventArgs e)
        {
            if (int.TryParse(textBox1.Text, out int visitors) && visitors > 0)
            {
                College college = new College();
                Caterer caterer = new Caterer();
                Decorator decorator = new Decorator();

                // Subscribe to event
                college.CollegeFest += caterer.OnCollegeFest;
                college.CollegeFest += decorator.OnCollegeFest;

                // Raise the event
                college.StartFest(visitors);
            }
            else
            {
                MessageBox.Show("Please enter a valid number of visitors.", "Input Error");
            }
        }
    }
}
