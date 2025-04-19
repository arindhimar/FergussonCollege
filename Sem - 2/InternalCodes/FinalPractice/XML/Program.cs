using System;
using System.Xml.Linq;

namespace XML
{
    internal class Program
    {
        static void Main(string[] args)
        {
            XElement temp = new XElement("Employee",
                new XElement("name", "Vaibhavi"));

            Console.WriteLine("Original XML:\n" + temp);

            // 🔍 Search
            var nameElement = temp.Element("name");
            if (nameElement != null)
            {
                Console.WriteLine("\nFound name: " + nameElement.Value);

                // ✏️ Update
                nameElement.Value = "Arin";
                Console.WriteLine("\nAfter Update:\n" + temp);
            }
            else
            {
                Console.WriteLine("\n<name> element not found.");
            }
        }
    }
}
