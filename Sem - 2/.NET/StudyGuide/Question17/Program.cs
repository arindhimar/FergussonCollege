using System;
using System.Collections.Generic;
using System.Linq;

namespace Question17
{
    class Program
    {
        static List<Contact> contacts = new List<Contact>();

        static void Main(string[] args)
        {
            while (true)
            {
                Console.WriteLine("\nContact Management System");
                Console.WriteLine("1. Add Contact");
                Console.WriteLine("2. View Contacts");
                Console.WriteLine("3. Search Contact");
                Console.WriteLine("4. Delete Contact");
                Console.WriteLine("5. Exit");
                Console.Write("Enter your choice: ");

                if (!int.TryParse(Console.ReadLine(), out int choice))
                {
                    Console.WriteLine("Invalid input. Please enter a number.");
                    continue;
                }

                switch (choice)
                {
                    case 1:
                        AddContact();
                        break;
                    case 2:
                        ViewContacts();
                        break;
                    case 3:
                        SearchContact();
                        break;
                    case 4:
                        DeleteContact();
                        break;
                    case 5:
                        return;
                    default:
                        Console.WriteLine("Invalid choice. Please try again.");
                        break;
                }
            }
        }

        static void AddContact()
        {
            Console.Write("\nEnter Name: ");
            string name = Console.ReadLine().Trim();

            Console.Write("Enter Phone Number: ");
            string phoneNumber = Console.ReadLine().Trim();

            if (string.IsNullOrEmpty(name) || string.IsNullOrEmpty(phoneNumber))
            {
                Console.WriteLine("Name and Phone Number cannot be empty.");
                return;
            }

            if (contacts.Any(c => c.PhoneNumber == phoneNumber))
            {
                Console.WriteLine("A contact with this phone number already exists.");
                return;
            }

            contacts.Add(new Contact(name, phoneNumber));
            Console.WriteLine("Contact added successfully.");
        }

        static void ViewContacts()
        {
            if (contacts.Count == 0)
            {
                Console.WriteLine("No contacts available.");
                return;
            }

            Console.WriteLine("\nContacts:");
            foreach (var contact in contacts)
            {
                Console.WriteLine(contact);
            }
        }

        static void SearchContact()
        {
            Console.Write("\nEnter Name or Phone Number to search: ");
            string searchTerm = Console.ReadLine().Trim().ToLower();

            var results = contacts.Where(c => c.Name.ToLower().Contains(searchTerm) || c.PhoneNumber.Contains(searchTerm)).ToList();

            if (results.Count == 0)
            {
                Console.WriteLine("No contacts found.");
                return;
            }

            Console.WriteLine("\nSearch Results:");
            foreach (var contact in results)
            {
                Console.WriteLine(contact);
            }
        }

        static void DeleteContact()
        {
            Console.Write("\nEnter Name or Phone Number to delete: ");
            string searchTerm = Console.ReadLine().Trim().ToLower();

            var contact = contacts.FirstOrDefault(c => c.Name.ToLower().Contains(searchTerm) || c.PhoneNumber.Contains(searchTerm));

            if (contact == null)
            {
                Console.WriteLine("Contact not found.");
                return;
            }

            contacts.Remove(contact);
            Console.WriteLine("Contact deleted successfully.");
        }
    }

    class Contact
    {
        public string Name { get; set; }
        public string PhoneNumber { get; set; }

        public Contact(string name, string phoneNumber)
        {
            Name = name;
            PhoneNumber = phoneNumber;
        }

        public override string ToString()
        {
            return $"Name: {Name}, Phone: {PhoneNumber}";
        }
    }
}
