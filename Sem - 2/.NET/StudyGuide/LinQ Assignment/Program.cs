using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LinQ_Assignment
{
    class Customer
    {
        public string Id { get; set; }
        public string Name { get; set; }

        public Customer(string id, string name)
        {
            this.Id = id;
            this.Name = name;
        }
    }

    class Order
    {
        public string CustomerId { get; set; }
        public string OrderId { get; set; }
        public string OrderDate { get; set; }

        public Order(string customerId, string orderId, string orderDate)
        {
            CustomerId = customerId;
            OrderId = orderId;
            OrderDate = orderDate;
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            List<Customer> customers = new List<Customer>
            {
                new Customer("1", "Arin"),
                new Customer("2", "Vasu"),
                new Customer("3", "Darshan"),
                new Customer("4", "Rahul"),
                new Customer("5", "Meera"),
                new Customer("6", "Kiran")
            };

            List<Order> orders = new List<Order>
            {
                new Order("1", "101", "27 March 2025"),
                new Order("2", "102", "26 March 2025"),
                new Order("3", "103", "25 March 2025"),
                new Order("1", "104", "24 March 2025"),
                new Order("4", "105", "23 March 2025"),
                new Order("5", "106", "22 March 2025"),
                new Order("6", "107", "21 March 2025")
            };

            var innerJoinResult = customers.Join(
                orders,
                customer => customer.Id,
                order => order.CustomerId,
                (customer, order) => new
                {
                    CustomerId = customer.Id,
                    CustomerName = customer.Name,
                    OrderId = order.OrderId,
                    OrderDate = order.OrderDate
                });

            foreach (var item in innerJoinResult)
            {
                Console.WriteLine($"CustomerId: {item.CustomerId}, CustomerName: {item.CustomerName}, OrderId: {item.OrderId}, OrderDate: {item.OrderDate}");
            }

            Console.ReadKey();
        }
    }
}
