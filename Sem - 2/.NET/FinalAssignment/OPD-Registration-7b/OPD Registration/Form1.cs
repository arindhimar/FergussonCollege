using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace OPD_Registration
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnRegister_Click(object sender, EventArgs e)
        {
            string patientName = txtPatientName.Text;
            string age = txtAge.Text;
            string gender = cmbGender.SelectedItem?.ToString();
            string contact = txtContactNumber.Text;
            string address = rtbAddress.Text;
            string visitDate = dtpDateOfVisit.Value.ToShortDateString();
            string doctor = cmbDoctorName.SelectedItem?.ToString();
            string symptoms = rtbSymptoms.Text;

            if (string.IsNullOrWhiteSpace(patientName) || string.IsNullOrWhiteSpace(age) || string.IsNullOrWhiteSpace(contact))
            {
                MessageBox.Show("Please fill in all required fields!", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            MessageBox.Show($"Patient {patientName} has been registered successfully!", "Success", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void btnClear_Click(object sender, EventArgs e)
        {
            txtPatientName.Clear();
            txtAge.Clear();
            cmbGender.SelectedIndex = -1;
            txtContactNumber.Clear();
            rtbAddress.Clear();
            dtpDateOfVisit.Value = DateTime.Now;
            cmbDoctorName.SelectedIndex = -1;
            rtbSymptoms.Clear();
        }

        private void btnExit_Click(object sender, EventArgs e)
        {
            this.Close();
        }

    }
}
