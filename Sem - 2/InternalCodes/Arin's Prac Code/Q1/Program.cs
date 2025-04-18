using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.IO;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace Q1
{

    public class Stundent {

        public int id ; public string name; public string description;

        public Stundent(int id, string name, string description)
        {
            this.id = id;
            this.name = name;
            this.description = description;
        }

        public override string ToString()
        {
            return "Id : "+ id+ " Name : "+name+" Description : "+description;
        }
    }


    internal class Program
    {

        static List<Stundent> list = new List<Stundent>();

        static void Main(string[] args)
        {
            /*            string str = Console.ReadLine();

                        char[] chars = str.ToCharArray();

                        char temp= chars[0];

                        chars[0] = chars[chars.Length - 1];
                        chars[chars.Length - 1] = temp;

                        foreach (var item in chars)
                        {
                            Console.Write(item);
                        }*/


            /*try
            {
                Console.WriteLine(User.div(4, 0));

            }
            catch(Custom e)
            {
                Console.WriteLine(e.Message);

            }
*/


            /*File.WriteAllText("sample.txt", "arin");
            File.AppendAllText("sample.txt", "Dhimar");

            Console.WriteLine(File.ReadAllText("sample.txt"));
*/

            /*BinaryWriter binaryWriter = new BinaryWriter(File.Open("sample.bin", FileMode.Create));

            binaryWriter.Write("Arin");

            binaryWriter.Close();

            binaryWriter = new BinaryWriter(File.Open("sample.bin", FileMode.Append));

            binaryWriter.Write("Dhimar");

            binaryWriter.Close();

            BinaryReader binaryReader = new BinaryReader(File.Open("sample.bin", FileMode.Open));

            while (true)
            {
                try
                {
                    string temp = binaryReader.ReadString();
                    Console.WriteLine(temp);
                }
                catch (Exception e)
                {
                    break;
                }
            }


            binaryReader.Close();*/


            list.Add(new Stundent(1, "arin", "SW "));
            list.Add(new Stundent(2, "arin", "SW "));

            list.Add(new Stundent(3, "arin", "SW "));



            foreach (Stundent stundent in list)
            {
                Console.WriteLine(stundent);
            }

            Console.WriteLine(list.Where(s=>s.name=="arin"));




            Console.ReadLine();
        }
    }
}
