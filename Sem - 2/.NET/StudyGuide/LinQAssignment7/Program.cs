using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LinQAssignment7
{
    class Product
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Category { get; set; }

        public Product(int id, string name, string category)
        {
            Id = id;
            Name = name;
            Category = category;
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            List<Product> products = new List<Product>
            {
                new Product(1, "Laptop", "Electronics"),
                new Product(2, "Smartphone", "Electronics"),
                new Product(3, "Tablet", "Electronics"),
                new Product(4, "Headphones", "Accessories"),
                new Product(5, "Keyboard", "Accessories"),
                new Product(6, "Mouse", "Accessories"),
                new Product(7, "Monitor", "Electronics"),
                new Product(8, "Smartwatch", "Wearables"),
                new Product(9, "Fitness Band", "Wearables"),
                new Product(10, "Wireless Charger", "Accessories"),
                new Product(11, "Gaming Console", "Gaming"),
                new Product(12, "Graphics Card", "Computers"),
                new Product(13, "SSD 1TB", "Storage"),
                new Product(14, "External HDD 2TB", "Storage"),
                new Product(15, "Bluetooth Speaker", "Audio"),
                new Product(16, "Projector", "Electronics"),
                new Product(17, "Action Camera", "Photography"),
                new Product(18, "Tripod Stand", "Photography"),
                new Product(19, "Microwave Oven", "Home Appliances"),
                new Product(20, "Air Conditioner", "Home Appliances")
            };

            var avgByCategory = products
                .GroupBy(p => p.Category)
                .Select(g => new { Category = g.Key, AverageId = g.Average(p => p.Id) });

            foreach (var item in avgByCategory)
            {
                Console.WriteLine($"Category: {item.Category}, Average Product ID: {item.AverageId:F2}");
            }

            Console.ReadKey();
        }
    }
}
