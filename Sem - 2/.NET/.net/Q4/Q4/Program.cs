using System;

namespace Q4
{
    public class CollegeFestEventArgs : EventArgs
    {
        public int NumberOfPeople { get; set; }

        public CollegeFestEventArgs(int numberOfPeople)
        {
            NumberOfPeople = numberOfPeople;
        }
    }

    public class College
    {
        public event EventHandler<CollegeFestEventArgs> CollegeFest;

        public void OnCollegeFest(int numberOfPeople)
        {
            CollegeFest?.Invoke(this, new CollegeFestEventArgs(numberOfPeople));
        }
    }

    public class Catering
    {
        private const int CateringChargePerPlate = 200;

        public void OnCollegeFest(object sender, CollegeFestEventArgs e)
        {
            int totalCateringCost = e.NumberOfPeople * CateringChargePerPlate;
            Console.WriteLine($"Catering Cost for {e.NumberOfPeople} people: Rs {totalCateringCost}");
        }
    }

    public class Decoration
    {
        private const int BasicDecorationCost = 10000;
        private const int PerStudentDecorationCost = 10;

        public void OnCollegeFest(object sender, CollegeFestEventArgs e)
        {
            int totalDecorationCost = BasicDecorationCost + (e.NumberOfPeople * PerStudentDecorationCost);
            Console.WriteLine($"Decoration Cost for {e.NumberOfPeople} people: Rs {totalDecorationCost}");
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            College college = new College();
            Catering catering = new Catering();
            Decoration decoration = new Decoration();

            college.CollegeFest += catering.OnCollegeFest;
            college.CollegeFest += decoration.OnCollegeFest;

            int choice = 0;

            while (true)
            {
                Console.Clear();
                Console.WriteLine("College Fest Event Handling");
                Console.WriteLine("1. Enter the number of people attending the fest");
                Console.WriteLine("2. Exit");
                Console.Write("Enter your choice: ");
                choice = Convert.ToInt32(Console.ReadLine());

                if (choice == 1)
                {
                    Console.Write("Enter the number of people attending the college fest: ");
                    if (int.TryParse(Console.ReadLine(), out int numberOfPeople) && numberOfPeople > 0)
                    {
                        college.OnCollegeFest(numberOfPeople);
                    }
                    else
                    {
                        Console.WriteLine("Invalid number of people entered.");
                    }
                    Console.WriteLine("\nPress any key to continue...");
                    Console.ReadKey();
                }
                else if (choice == 2)
                {
                    break;
                }
                else
                {
                    Console.WriteLine("Invalid choice. Please try again.");
                    Console.ReadKey();
                }
            }
        }
    }
}
