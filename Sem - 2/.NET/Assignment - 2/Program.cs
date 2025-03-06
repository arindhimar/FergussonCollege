using System;

namespace Assignment___2
{
    internal class Program
    {
        static void menu()
        {
            Console.WriteLine("1 - Add");
            Console.WriteLine("2 - Sub");
            Console.WriteLine("3 - Mul");
            Console.WriteLine("4 - Div");
            Console.WriteLine("5 - Per");
            Console.WriteLine("6 - Exit");
        }

        static void Add(int a, int b)
        {
            Console.WriteLine($"Addition: {a + b}");
        }

        static void Add(double a, double b)
        {
            Console.WriteLine($"Addition: {a + b}");
        }

        static void Sub(int a, int b)
        {
            Console.WriteLine($"Subtraction: {a - b}");
        }

        static void Sub(double a, double b)
        {
            Console.WriteLine($"Subtraction: {a - b}");
        }

        static void Mul(int a, int b)
        {
            Console.WriteLine($"Multiplication: {a * b}");
        }

        static void Mul(double a, double b)
        {
            Console.WriteLine($"Multiplication: {a * b}");
        }

        static void Div(int a, int b)
        {
            if (b != 0)
                Console.WriteLine($"Division: {a / (double)b}");
            else
                Console.WriteLine("Cannot divide by zero");
        }

        static void Div(double a, double b)
        {
            if (b != 0)
                Console.WriteLine($"Division: {a / b}");
            else
                Console.WriteLine("Cannot divide by zero");
        }

        static void Per(int total, int obtained)
        {
            if (total != 0)
                Console.WriteLine($"Percentage: {(obtained / (double)total) * 100}%");
            else
                Console.WriteLine("Total cannot be zero");
        }

        static void Per(double total, double obtained)
        {
            if (total != 0)
                Console.WriteLine($"Percentage: {(obtained / total) * 100}%");
            else
                Console.WriteLine("Total cannot be zero");
        }

        static void Main(string[] args)
        {
            int opt;
            int n1, n2;
            double dn1, dn2;

            do
            {
                menu();
                opt = int.Parse(Console.ReadLine());

                if (opt == 5)
                {
                    Console.Write("Enter Total Number (int or double): ");
                    string input = Console.ReadLine();
                    bool isInt = int.TryParse(input, out n1);
                    if (isInt)
                    {
                        Console.Write("Enter Obtained Number (int or double): ");
                        input = Console.ReadLine();
                        isInt = int.TryParse(input, out n2);
                        if (isInt)
                        {
                            Per(n1, n2);
                        }
                        else
                        {
                            dn2 = double.Parse(input);
                            Per(n1, dn2);
                        }
                    }
                    else
                    {
                        dn1 = double.Parse(input);
                        Console.Write("Enter Obtained Number (int or double): ");
                        input = Console.ReadLine();
                        isInt = int.TryParse(input, out n2);
                        if (isInt)
                        {
                            Per(dn1, n2);
                        }
                        else
                        {
                            dn2 = double.Parse(input);
                            Per(dn1, dn2);
                        }
                    }
                }
                else
                {
                    Console.Write("Enter First Number (int or double): ");
                    string input = Console.ReadLine();
                    bool isInt = int.TryParse(input, out n1);
                    if (isInt)
                    {
                        Console.Write("Enter Second Number (int or double): ");
                        input = Console.ReadLine();
                        isInt = int.TryParse(input, out n2);
                        if (isInt)
                        {
                            switch (opt)
                            {
                                case 1:
                                    Add(n1, n2);
                                    break;
                                case 2:
                                    Sub(n1, n2);
                                    break;
                                case 3:
                                    Mul(n1, n2);
                                    break;
                                case 4:
                                    Div(n1, n2);
                                    break;
                            }
                        }
                        else
                        {
                            dn2 = double.Parse(input);
                            switch (opt)
                            {
                                case 1:
                                    Add(n1, dn2);
                                    break;
                                case 2:
                                    Sub(n1, dn2);
                                    break;
                                case 3:
                                    Mul(n1, dn2);
                                    break;
                                case 4:
                                    Div(n1, dn2);
                                    break;
                            }
                        }
                    }
                    else
                    {
                        dn1 = double.Parse(input);
                        Console.Write("Enter Second Number (int or double): ");
                        input = Console.ReadLine();
                        isInt = int.TryParse(input, out n2);
                        if (isInt)
                        {
                            switch (opt)
                            {
                                case 1:
                                    Add(dn1, n2);
                                    break;
                                case 2:
                                    Sub(dn1, n2);
                                    break;
                                case 3:
                                    Mul(dn1, n2);
                                    break;
                                case 4:
                                    Div(dn1, n2);
                                    break;
                            }
                        }
                        else
                        {
                            dn2 = double.Parse(input);
                            switch (opt)
                            {
                                case 1:
                                    Add(dn1, dn2);
                                    break;
                                case 2:
                                    Sub(dn1, dn2);
                                    break;
                                case 3:
                                    Mul(dn1, dn2);
                                    break;
                                case 4:
                                    Div(dn1, dn2);
                                    break;
                            }
                        }
                    }
                }
            } while (opt != 6);
        }
    }
}
