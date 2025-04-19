using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection.Emit;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApps
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*
                        try
                        {
                            int x = int.Parse(Console.ReadLine());
                        }
                        catch (Exception ex)
                        {
                            Console.WriteLine(ex.Message);
                        }*/


            /*            try {
                            Console.WriteLine(UserExeception.div(5, 1));
                        }
                        catch(CustomExecption e)
                        {
                            Console.WriteLine(e.Message);
                        }
            */

            /*
                        string temp = Console.ReadLine();

                        File.WriteAllText("sample.txt", temp);


                        temp = Console.ReadLine();


                        File.AppendAllText("sample.txt", temp);


                        Console.WriteLine(File.ReadAllText("sample.txt"));*/


            /*            FileInfo fileInfo = new FileInfo("sample.txt");

                        Console.WriteLine(fileInfo.FullName);
                        Console.WriteLine(fileInfo.Name);
                        Console.WriteLine(fileInfo.Extension);
                        Console.WriteLine(fileInfo.CreationTime);
                        Console.WriteLine(fileInfo.LastWriteTime);
                        Console.WriteLine(fileInfo.LastAccessTime);
                        Console.WriteLine(fileInfo.Directory);*/

            /*
                        DirectoryInfo directoryInfo = new DirectoryInfo("C:\\Users\\Arin Dhimar\\Documents\\FergussonCollege\\Sem - 2\\.NET\\MeetingPrac3\\ConsoleApps\\bin\\Debug");

                        Console.WriteLine(directoryInfo.FullName);
                        Console.WriteLine(directoryInfo.Name);
                        Console.WriteLine(directoryInfo.CreationTime);*/
/*

            BinaryWriter binaryWriter = new BinaryWriter(File.Open("sample.bin", FileMode.Create));

            string temp = Console.ReadLine();

            binaryWriter.Write(temp);

            binaryWriter.Close();



            binaryWriter = new BinaryWriter(File.Open("sample.bin", FileMode.Append));

            temp = Console.ReadLine();

            binaryWriter.Write(temp);

            binaryWriter.Close();


            BinaryReader binaryReader = new BinaryReader(File.Open("sample.bin", FileMode.Open));

            while (true)
            {
                try
                {
                    Console.WriteLine(binaryReader.ReadString());
                }
                catch (Exception e)
                {
                    break;
                }
            }


            binaryReader.Close();*/



        }
    }
}
