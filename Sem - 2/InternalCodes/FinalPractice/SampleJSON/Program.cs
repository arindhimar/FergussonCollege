using System;
using System.Collections.Generic;
using System.IO;
using System.Xml.Serialization;


class Program
{
    public class Student
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public int Age { get; set; }
    }

    static void Main(string[] args)
    {
 

        // 1️⃣ Serialize to XML
        XmlSerializer serializer = new XmlSerializer(typeof(List<Student>));
        using (TextWriter writer = new StreamWriter("students.xml"))
        {
            serializer.Serialize(writer, students);
        }
        Console.WriteLine("✅ XML written to students.xml");

        // 2️⃣ Deserialize from XML
        List<Student> loadedStudents;
        using (TextReader reader = new StreamReader("students.xml"))
        {
            loadedStudents = (List<Student>)serializer.Deserialize(reader);
        }

        Console.WriteLine("\n📖 Deserialized Students:");
        foreach (var student in loadedStudents)
        {
            Console.WriteLine($"ID: {student.Id}, Name: {student.Name}, Age: {student.Age}");
        }
    }
}
