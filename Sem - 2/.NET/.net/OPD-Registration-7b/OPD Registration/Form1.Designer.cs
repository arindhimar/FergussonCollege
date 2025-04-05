namespace OPD_Registration
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.lblPatientName = new System.Windows.Forms.Label();
            this.lblAge = new System.Windows.Forms.Label();
            this.lblGender = new System.Windows.Forms.Label();
            this.lblContactNumber = new System.Windows.Forms.Label();
            this.lblAddress = new System.Windows.Forms.Label();
            this.lblDateOfVisit = new System.Windows.Forms.Label();
            this.lblDoctorName = new System.Windows.Forms.Label();
            this.lblSymptoms = new System.Windows.Forms.Label();
            this.txtPatientName = new System.Windows.Forms.TextBox();
            this.txtAge = new System.Windows.Forms.TextBox();
            this.txtContactNumber = new System.Windows.Forms.TextBox();
            this.cmbGender = new System.Windows.Forms.ComboBox();
            this.cmbDoctorName = new System.Windows.Forms.ComboBox();
            this.rtbAddress = new System.Windows.Forms.RichTextBox();
            this.dtpDateOfVisit = new System.Windows.Forms.DateTimePicker();
            this.rtbSymptoms = new System.Windows.Forms.RichTextBox();
            this.btnRegister = new System.Windows.Forms.Button();
            this.btnClear = new System.Windows.Forms.Button();
            this.btnExit = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // lblPatientName
            // 
            this.lblPatientName.AutoSize = true;
            this.lblPatientName.Location = new System.Drawing.Point(24, 46);
            this.lblPatientName.Name = "lblPatientName";
            this.lblPatientName.Size = new System.Drawing.Size(91, 16);
            this.lblPatientName.TabIndex = 0;
            this.lblPatientName.Text = "Patient Name:";
            // 
            // lblAge
            // 
            this.lblAge.AutoSize = true;
            this.lblAge.Location = new System.Drawing.Point(24, 79);
            this.lblAge.Name = "lblAge";
            this.lblAge.Size = new System.Drawing.Size(35, 16);
            this.lblAge.TabIndex = 1;
            this.lblAge.Text = "Age:";
            // 
            // lblGender
            // 
            this.lblGender.AutoSize = true;
            this.lblGender.Location = new System.Drawing.Point(24, 113);
            this.lblGender.Name = "lblGender";
            this.lblGender.Size = new System.Drawing.Size(55, 16);
            this.lblGender.TabIndex = 2;
            this.lblGender.Text = "Gender:";
            // 
            // lblContactNumber
            // 
            this.lblContactNumber.AutoSize = true;
            this.lblContactNumber.Location = new System.Drawing.Point(27, 146);
            this.lblContactNumber.Name = "lblContactNumber";
            this.lblContactNumber.Size = new System.Drawing.Size(106, 16);
            this.lblContactNumber.TabIndex = 3;
            this.lblContactNumber.Text = "Contact Number:";
            // 
            // lblAddress
            // 
            this.lblAddress.AutoSize = true;
            this.lblAddress.Location = new System.Drawing.Point(27, 177);
            this.lblAddress.Name = "lblAddress";
            this.lblAddress.Size = new System.Drawing.Size(61, 16);
            this.lblAddress.TabIndex = 4;
            this.lblAddress.Text = "Address:";
            // 
            // lblDateOfVisit
            // 
            this.lblDateOfVisit.AutoSize = true;
            this.lblDateOfVisit.Location = new System.Drawing.Point(14, 264);
            this.lblDateOfVisit.Name = "lblDateOfVisit";
            this.lblDateOfVisit.Size = new System.Drawing.Size(81, 16);
            this.lblDateOfVisit.TabIndex = 5;
            this.lblDateOfVisit.Text = "Date of Visit:";
            // 
            // lblDoctorName
            // 
            this.lblDoctorName.AutoSize = true;
            this.lblDoctorName.Location = new System.Drawing.Point(12, 312);
            this.lblDoctorName.Name = "lblDoctorName";
            this.lblDoctorName.Size = new System.Drawing.Size(100, 16);
            this.lblDoctorName.TabIndex = 6;
            this.lblDoctorName.Text = "Doctor’s Name:";
            // 
            // lblSymptoms
            // 
            this.lblSymptoms.AutoSize = true;
            this.lblSymptoms.Location = new System.Drawing.Point(21, 350);
            this.lblSymptoms.Name = "lblSymptoms";
            this.lblSymptoms.Size = new System.Drawing.Size(74, 16);
            this.lblSymptoms.TabIndex = 7;
            this.lblSymptoms.Text = "Symptoms:";
            // 
            // txtPatientName
            // 
            this.txtPatientName.Location = new System.Drawing.Point(153, 46);
            this.txtPatientName.Name = "txtPatientName";
            this.txtPatientName.Size = new System.Drawing.Size(100, 22);
            this.txtPatientName.TabIndex = 8;
            // 
            // txtAge
            // 
            this.txtAge.Location = new System.Drawing.Point(153, 79);
            this.txtAge.Name = "txtAge";
            this.txtAge.Size = new System.Drawing.Size(100, 22);
            this.txtAge.TabIndex = 9;
            // 
            // txtContactNumber
            // 
            this.txtContactNumber.Location = new System.Drawing.Point(153, 139);
            this.txtContactNumber.Name = "txtContactNumber";
            this.txtContactNumber.Size = new System.Drawing.Size(100, 22);
            this.txtContactNumber.TabIndex = 10;
            // 
            // cmbGender
            // 
            this.cmbGender.FormattingEnabled = true;
            this.cmbGender.Items.AddRange(new object[] {
            "Male",
            "Female",
            "Other"});
            this.cmbGender.Location = new System.Drawing.Point(153, 113);
            this.cmbGender.Name = "cmbGender";
            this.cmbGender.Size = new System.Drawing.Size(121, 24);
            this.cmbGender.TabIndex = 11;
            // 
            // cmbDoctorName
            // 
            this.cmbDoctorName.FormattingEnabled = true;
            this.cmbDoctorName.Items.AddRange(new object[] {
            "Dr. A Sharma",
            "Dr. B Gupta",
            "Dr. C Patil"});
            this.cmbDoctorName.Location = new System.Drawing.Point(153, 309);
            this.cmbDoctorName.Name = "cmbDoctorName";
            this.cmbDoctorName.Size = new System.Drawing.Size(121, 24);
            this.cmbDoctorName.TabIndex = 12;
            // 
            // rtbAddress
            // 
            this.rtbAddress.Location = new System.Drawing.Point(153, 177);
            this.rtbAddress.Name = "rtbAddress";
            this.rtbAddress.Size = new System.Drawing.Size(175, 52);
            this.rtbAddress.TabIndex = 13;
            this.rtbAddress.Text = "";
            // 
            // dtpDateOfVisit
            // 
            this.dtpDateOfVisit.Location = new System.Drawing.Point(153, 264);
            this.dtpDateOfVisit.Name = "dtpDateOfVisit";
            this.dtpDateOfVisit.Size = new System.Drawing.Size(200, 22);
            this.dtpDateOfVisit.TabIndex = 14;
            // 
            // rtbSymptoms
            // 
            this.rtbSymptoms.Location = new System.Drawing.Point(153, 350);
            this.rtbSymptoms.Name = "rtbSymptoms";
            this.rtbSymptoms.Size = new System.Drawing.Size(175, 31);
            this.rtbSymptoms.TabIndex = 15;
            this.rtbSymptoms.Text = "";
            // 
            // btnRegister
            // 
            this.btnRegister.BackColor = System.Drawing.Color.Chartreuse;
            this.btnRegister.Location = new System.Drawing.Point(17, 397);
            this.btnRegister.Name = "btnRegister";
            this.btnRegister.Size = new System.Drawing.Size(75, 32);
            this.btnRegister.TabIndex = 16;
            this.btnRegister.Text = "Register";
            this.btnRegister.UseVisualStyleBackColor = false;
            this.btnRegister.Click += new System.EventHandler(this.btnRegister_Click);
            // 
            // btnClear
            // 
            this.btnClear.Location = new System.Drawing.Point(115, 397);
            this.btnClear.Name = "btnClear";
            this.btnClear.Size = new System.Drawing.Size(75, 32);
            this.btnClear.TabIndex = 17;
            this.btnClear.Text = "Clear";
            this.btnClear.UseVisualStyleBackColor = true;
            this.btnClear.Click += new System.EventHandler(this.btnClear_Click);
            // 
            // btnExit
            // 
            this.btnExit.BackColor = System.Drawing.Color.Red;
            this.btnExit.Location = new System.Drawing.Point(221, 397);
            this.btnExit.Name = "btnExit";
            this.btnExit.Size = new System.Drawing.Size(75, 31);
            this.btnExit.TabIndex = 18;
            this.btnExit.Text = "Exit";
            this.btnExit.UseVisualStyleBackColor = false;
            this.btnExit.Click += new System.EventHandler(this.btnExit_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.btnExit);
            this.Controls.Add(this.btnClear);
            this.Controls.Add(this.btnRegister);
            this.Controls.Add(this.rtbSymptoms);
            this.Controls.Add(this.dtpDateOfVisit);
            this.Controls.Add(this.rtbAddress);
            this.Controls.Add(this.cmbDoctorName);
            this.Controls.Add(this.cmbGender);
            this.Controls.Add(this.txtContactNumber);
            this.Controls.Add(this.txtAge);
            this.Controls.Add(this.txtPatientName);
            this.Controls.Add(this.lblSymptoms);
            this.Controls.Add(this.lblDoctorName);
            this.Controls.Add(this.lblDateOfVisit);
            this.Controls.Add(this.lblAddress);
            this.Controls.Add(this.lblContactNumber);
            this.Controls.Add(this.lblGender);
            this.Controls.Add(this.lblAge);
            this.Controls.Add(this.lblPatientName);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lblPatientName;
        private System.Windows.Forms.Label lblAge;
        private System.Windows.Forms.Label lblGender;
        private System.Windows.Forms.Label lblContactNumber;
        private System.Windows.Forms.Label lblAddress;
        private System.Windows.Forms.Label lblDateOfVisit;
        private System.Windows.Forms.Label lblDoctorName;
        private System.Windows.Forms.Label lblSymptoms;
        private System.Windows.Forms.TextBox txtPatientName;
        private System.Windows.Forms.TextBox txtAge;
        private System.Windows.Forms.TextBox txtContactNumber;
        private System.Windows.Forms.ComboBox cmbGender;
        private System.Windows.Forms.ComboBox cmbDoctorName;
        private System.Windows.Forms.RichTextBox rtbAddress;
        private System.Windows.Forms.DateTimePicker dtpDateOfVisit;
        private System.Windows.Forms.RichTextBox rtbSymptoms;
        private System.Windows.Forms.Button btnRegister;
        private System.Windows.Forms.Button btnClear;
        private System.Windows.Forms.Button btnExit;
    }
}

