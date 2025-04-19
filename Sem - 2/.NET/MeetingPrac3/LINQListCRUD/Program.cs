using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Runtime.Remoting;
using System.Text;
using System.Threading.Tasks;

namespace LINQListCRUD
{

    public class Stundet
    {
        public int ID { get; set; }
        public string Name { get; set; }
        public Stundet(int iD, string name)
        {
            ID = iD;
            Name = name;
        }
    }

    internal class Program
    {

        static int tempId = 0;

        static List<Stundet> list = new List<Stundet>();

        static void Main(string[] args)
        {
            int opt = 0;
            do
            {

                Console.WriteLine("1 - add");
                Console.WriteLine("2 - DEelte");
                Console.WriteLine("3 - update");
                Console.WriteLine("4 - display");

                opt = int.Parse(Console.ReadLine());


                if(opt == 1)
                {
                    try
                    {
                        string temp = Console.ReadLine();

                        Stundet tempSt = new Stundet(++tempId, temp);

                        list.Add(tempSt);
                    }
                    catch(Exception ex) { Console.WriteLine(    ex.ToString()); }
                }
                else if (opt == 2)
                {
                    int tempId = int.Parse(Console.ReadLine());

                    list.RemoveAll(S=>S.ID == tempId);

                }
                else if (opt == 3)
                {
                    int tempId = int.Parse(Console.ReadLine());

                    Stundet tempSt = list.Where(s=>s.ID== tempId).FirstOrDefault();

                    if(tempSt != null)
                    {
                        tempSt.Name = Console.ReadLine();
                    }

                }
                else if (opt == 4)
                {
                    foreach (var item in list)
                    {
                        Console.WriteLine(item.ID);
                        Console.WriteLine(item.Name);
                    }
                }

                


            }while (true);


        }
    }
}
