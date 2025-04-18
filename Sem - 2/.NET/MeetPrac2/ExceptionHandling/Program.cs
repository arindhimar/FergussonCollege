using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.Remoting.Metadata.W3cXsd2001;
using System.Text;
using System.Threading.Tasks;

namespace ExceptionHandling
{
    internal class Program
    {

        static void Main(string[] args)
        {
            
            List <Stundet> studs = new List <Stundet>();

            Stundet temp = new Stundet(1,"Arin");

            studs.Add(temp);

            temp = new Stundet(2, "Ashish");

            studs.Add(temp);

            temp = new Stundet(3, "Ganesh");

            studs.Add(temp);


            temp = new Stundet(4, "Bhushan");

            studs.Add(temp);


            foreach (var item in studs)
            {
                Console.WriteLine(item);
            }


            studs.RemoveAll(s=>s.id == 1);



            Stundet tempstd = studs.Where(s=>s.id == 4).FirstOrDefault();

            Console.WriteLine();

            if (tempstd != null)
            {
                tempstd.name = "ajinkya";
            }


            foreach (var item in studs)
            {
                Console.WriteLine(item);
            }

            

            



        }
    }

    public class Stundet
    {
        public int id;
        public string name;
        public Stundet(int id,string name) { 
        this.id = id;
        this.name = name;
        
        }

        public override string ToString()
        {
            return id + ":" + name;
        }
    }
}
