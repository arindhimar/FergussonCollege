namespace Question1
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
            this.label1 = new System.Windows.Forms.Label();
            this.todoText = new System.Windows.Forms.TextBox();
            this.button1 = new System.Windows.Forms.Button();
            this.todoList = new System.Windows.Forms.ListBox();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(213, 42);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(38, 16);
            this.label1.TabIndex = 0;
            this.label1.Text = "Task";
            this.label1.Click += new System.EventHandler(this.label1_Click);
            // 
            // todoText
            // 
            this.todoText.Location = new System.Drawing.Point(333, 42);
            this.todoText.Name = "todoText";
            this.todoText.Size = new System.Drawing.Size(185, 22);
            this.todoText.TabIndex = 1;
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(389, 95);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 23);
            this.button1.TabIndex = 2;
            this.button1.Text = "Add";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // todoList
            // 
            this.todoList.FormattingEnabled = true;
            this.todoList.ItemHeight = 16;
            this.todoList.Location = new System.Drawing.Point(371, 170);
            this.todoList.Name = "todoList";
            this.todoList.Size = new System.Drawing.Size(120, 84);
            this.todoList.TabIndex = 3;
            this.todoList.SelectedIndexChanged += new System.EventHandler(this.todoList_SelectedIndexChanged);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(963, 453);
            this.Controls.Add(this.todoList);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.todoText);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox todoText;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.ListBox todoList;
    }
}

