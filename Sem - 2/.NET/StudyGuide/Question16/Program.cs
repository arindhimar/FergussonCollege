using System;
using System.Text.RegularExpressions;

namespace Question16
{
    internal class Program
    {
        static void Main(string[] args)
        {
            while (true)
            {
                Console.Write("Enter a password to check its strength (or type 'exit' to quit): ");
                string password = Console.ReadLine();

                if (password.ToLower() == "exit")
                    break;

                string strength = EvaluatePasswordStrength(password);
                Console.WriteLine($"Password Strength: {strength}\n");
            }
        }

        static string EvaluatePasswordStrength(string password)
        {
            int score = 0;

            if (password.Length >= 8)
                score++;
            if (Regex.IsMatch(password, "[A-Z]"))
                score++;
            if (Regex.IsMatch(password, "[a-z]"))
                score++;
            if (Regex.IsMatch(password, "[0-9]"))
                score++;
            if (Regex.IsMatch(password, "[!@#$%^&*(),.?\":{}|<>]"))
                score++;

            // Replace switch expression with traditional switch statement
            string result;
            switch (score)
            {
                case 5:
                    result = "Very Strong";
                    break;
                case 4:
                    result = "Strong";
                    break;
                case 3:
                    result = "Medium";
                    break;
                case 2:
                    result = "Weak";
                    break;
                default:
                    result = "Very Weak";
                    break;
            }
            return result;
        }
    }
}
