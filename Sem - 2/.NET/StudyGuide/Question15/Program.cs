using System;
using System.Collections.Generic;
using System.Linq;

namespace Question15
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<Expense> expenses = new List<Expense>();

            while (true)
            {
                Console.WriteLine("\nPersonal Finance Manager");
                Console.WriteLine("1. Add Expense");
                Console.WriteLine("2. View All Expenses");
                Console.WriteLine("3. View Total Expenses");
                Console.WriteLine("4. Filter Expenses by Category");
                Console.WriteLine("5. Get Monthly Report");
                Console.WriteLine("6. Exit");
                Console.Write("Enter your choice: ");

                if (!int.TryParse(Console.ReadLine(), out int choice))
                {
                    Console.WriteLine("Invalid input. Please enter a number.");
                    continue;
                }

                switch (choice)
                {
                    case 1:
                        AddExpense(expenses);
                        break;
                    case 2:
                        ViewAllExpenses(expenses);
                        break;
                    case 3:
                        ViewTotalExpenses(expenses);
                        break;
                    case 4:
                        FilterExpensesByCategory(expenses);
                        break;
                    case 5:
                        GetMonthlyReport(expenses);
                        break;
                    case 6:
                        return;
                    default:
                        Console.WriteLine("Invalid choice. Please try again.");
                        break;
                }
            }
        }

        static void AddExpense(List<Expense> expenses)
        {
            Console.Write("Enter expense description: ");
            string description = Console.ReadLine();

            Console.Write("Enter amount: ");
            if (!decimal.TryParse(Console.ReadLine(), out decimal amount))
            {
                Console.WriteLine("Invalid amount. Please enter a valid number.");
                return;
            }

            Console.Write("Enter category (e.g., Food, Rent, Transport): ");
            string category = Console.ReadLine();

            expenses.Add(new Expense(description, amount, category, DateTime.Now));
            Console.WriteLine("Expense added successfully!");
        }

        static void ViewAllExpenses(List<Expense> expenses)
        {
            Console.WriteLine("\nAll Expenses:");
            foreach (var expense in expenses)
            {
                Console.WriteLine(expense);
            }
        }

        static void ViewTotalExpenses(List<Expense> expenses)
        {
            decimal total = expenses.Sum(e => e.Amount);
            Console.WriteLine($"\nTotal Expenses: ${total:F2}");
        }

        static void FilterExpensesByCategory(List<Expense> expenses)
        {
            Console.Write("Enter category to filter: ");
            string category = Console.ReadLine();
            var filtered = expenses.Where(e => e.Category.Equals(category, StringComparison.OrdinalIgnoreCase));

            Console.WriteLine($"\nExpenses in {category} category:");
            foreach (var expense in filtered)
            {
                Console.WriteLine(expense);
            }
        }

        static void GetMonthlyReport(List<Expense> expenses)
        {
            var grouped = expenses.GroupBy(e => new { e.Date.Year, e.Date.Month })
                                  .Select(g => new { Month = g.Key, Total = g.Sum(e => e.Amount) });

            Console.WriteLine("\nMonthly Expense Report:");
            foreach (var entry in grouped)
            {
                Console.WriteLine($"{entry.Month.Year}-{entry.Month.Month}: ${entry.Total:F2}");
            }
        }
    }

    class Expense
    {
        public string Description { get; set; }
        public decimal Amount { get; set; }
        public string Category { get; set; }
        public DateTime Date { get; set; }

        public Expense(string description, decimal amount, string category, DateTime date)
        {
            Description = description;
            Amount = amount;
            Category = category;
            Date = date;
        }

        public override string ToString()
        {
            return $"{Date:yyyy-MM-dd} | {Category} | {Description} | ${Amount:F2}";
        }
    }
}
