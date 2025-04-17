using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using System.ComponentModel.DataAnnotations;


namespace WebCRUD.Pages
{
    public class IndexModel : PageModel
    {
        //public static List <Student> Students  = new List<Student> ();
        public static List<Student> Students = new();

        [BindProperty]
        public Student Student { get; set; }

        [BindProperty]
        public int? editID { get; set; }


        public void OnGet()
        {

        }

        public IActionResult OnPostAdd()
        {
            if (!Students.Any(s => s.id == Student.id))
                Students.Add(Student);
            return RedirectToPage();
        }

        public IActionResult OnPostDelete(int id)
        {
            Students.RemoveAll(s=>s.id == id);
            return RedirectToPage();
        }

        public IActionResult OnPostEdit()
        {
            Student temp = Students.Where(s => s.id == Student.id).FirstOrDefault();

            if (temp != null)
            {
                temp.name = Student.name;
                temp.age = Student.age; 
            }

            return RedirectToPage();
        }
    }

    public class Student
    {
        [Required]
        public int id { get; set; }

        [Required]
        public string name { get; set; }

        [Range(1, 120, ErrorMessage = "Age must be between 1 and 120")]
        public int age { get; set; }
    }
}
