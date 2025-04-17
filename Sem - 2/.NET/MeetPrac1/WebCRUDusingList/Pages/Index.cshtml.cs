using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace WebCRUDusingList.Pages
{

    public class Student
    {
        public int Id { get; set; }
        public string Name { get; set; }

        public int Age { get; set; }
    }



    public class IndexModel : PageModel
    {
        [BindProperty]
        public Student student { get; set; }

        [BindProperty]
        public int? EditId { get; set; }

        static public List<Student> std =  new List<Student>();

        public void OnGet()
        {

        }

        public IActionResult OnPostAdd()
        {

            std.Add(student);

            return RedirectToPage();
        }

        public IActionResult OnPostDelete(int id)
        {

            std.RemoveAll(s => s.Id == id);

            return RedirectToPage();

        }

        public IActionResult OnPostEdit()
        {
            Student temp = std.Where(s=>s.Id==student.Id).FirstOrDefault();

            if (temp != null)
            {
                temp.Name = student.Name;
                temp.Age = student.Age;
            }

            return RedirectToPage();
        }

    }
}
