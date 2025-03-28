using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Question5
{
    interface Shape
    {
        void getArea();
    }

    class Square : Shape
    {
        public void getArea()
        {
            throw new NotImplementedException();
        }
    }

    class Animal
    {
        public Animal() { }

        // Marking speak() as virtual to allow overriding
        public virtual void Speak()
        {
            Console.WriteLine("Animal speaks!");
        }
    }

    class Cat : Animal
    {
        public Cat() { }

        // Overriding the Speak method
        public override void Speak()
        {
            Console.WriteLine("Cat meows!");
        }
    }


    class staticCtor
    {
        static int a = 5;
        static staticCtor()
        {
            a++;
            Console.WriteLine(a);
        }


    }

    internal class Program
    {
        static void Main(string[] args)
        {
            //staticCtor src = new staticCtor();
            //staticCtor src2 = new staticCtor();
            //staticCtor src3 = new staticCtor();

            Animal myAnimal = new Animal();
            myAnimal.Speak(); // Calls Animal's Speak

            Animal myCat = new Cat();
            myCat.Speak(); // Calls Cat's Speak due to runtime polymorphism

            Cat specificCat = new Cat();
            specificCat.Speak(); // Calls Cat's Speak directly




        }
    }
}
