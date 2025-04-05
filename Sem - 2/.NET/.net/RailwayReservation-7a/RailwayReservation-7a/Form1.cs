using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace RailwayReservation_7a
{
    public partial class Form1 : Form
    {

        private double baseFare;
        private double totalFare;
        public Form1()
        {
            InitializeComponent();
        }

        private void label5_Click(object sender, EventArgs e)
        {

        }

        private void btnCalculateFare_Click(object sender, EventArgs e)
        {
            if (cmbTrain.SelectedItem == null || cmbClass.SelectedItem == null)
            {
                MessageBox.Show("Please select Train and Class.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            switch (cmbTrain.SelectedItem.ToString())
            {
                case "Rajdhani Express":
                    baseFare = 1500;
                    break;
                case "Shatabdi Express":
                    baseFare = 1200;
                    break;
                case "Duronto Express":
                    baseFare = 1800;
                    break;
                case "Garib Rath":
                    baseFare = 800;
                    break;
                case "Tejas Express":
                    baseFare = 2000;
                    break;
            }

            switch (cmbClass.SelectedItem.ToString())
            {
                case "First AC":
                    totalFare = baseFare * 2.5;
                    break;
                case "Second AC":
                    totalFare = baseFare * 2.0;
                    break;
                case "Third AC":
                    totalFare = baseFare * 1.5;
                    break;
                case "Sleeper":
                    totalFare = baseFare * 1.0;
                    break;
            }

            txtFare.Text = totalFare.ToString("C"); // Format as currency
        }

        private void btnBookTicket_Click(object sender, EventArgs e)
        {
            if (string.IsNullOrEmpty(txtPassengerName.Text) || string.IsNullOrEmpty(txtAge.Text) ||
                cmbGender.SelectedItem == null || cmbFrom.SelectedItem == null || cmbTo.SelectedItem == null ||
                cmbTrain.SelectedItem == null || cmbClass.SelectedItem == null || string.IsNullOrEmpty(txtFare.Text))
            {
                MessageBox.Show("Please fill all fields before booking.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            MessageBox.Show("Ticket Booked Successfully!\n\n" +
                            $"Passenger: {txtPassengerName.Text}\n" +
                            $"Age: {txtAge.Text}\n" +
                            $"Gender: {cmbGender.SelectedItem}\n" +
                            $"From: {cmbFrom.SelectedItem}\n" +
                            $"To: {cmbTo.SelectedItem}\n" +
                            $"Train: {cmbTrain.SelectedItem}\n" +
                            $"Class: {cmbClass.SelectedItem}\n" +
                            $"Fare: {txtFare.Text}\n" +
                            $"Date of Journey: {dtpDate.Value.ToShortDateString()}",
                            "Booking Confirmation", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void btnClear_Click(object sender, EventArgs e)
        {
            txtPassengerName.Clear();
            txtAge.Clear();
            cmbGender.SelectedIndex = -1;
            cmbFrom.SelectedIndex = -1;
            cmbTo.SelectedIndex = -1;
            cmbTrain.SelectedIndex = -1;
            cmbClass.SelectedIndex = -1;
            txtFare.Clear();
        }

    }
}
