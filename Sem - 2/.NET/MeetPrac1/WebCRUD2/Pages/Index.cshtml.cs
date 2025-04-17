using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace WebCRUD2.Pages
{
    public class Student
    {
        public int Id { get; set; }
        public string FirstName { get; set; }

        public string LastName { get; set; }
    }
    public class IndexModel : PageModel
    {
        
        public static List<Student> List = new List<Student>();

        [BindProperty]
        public Student student { get; set; }

        [BindProperty]
        public int? EditId { get; set; }

        public void OnGet()
        {

        }

        public IActionResult OnPostAdd()
        {
            List.Add(student);
            return RedirectToPage();
        }

        public IActionResult OnPostDelete(int id)
        {
            List.RemoveAll(x => x.Id == id);
            return RedirectToPage();
        }

        public IActionResult OnPostEdit()
        {
            Student temp = List.Where(s=>s.Id==student.Id).FirstOrDefault();

            if (temp != null)
            {
                temp.FirstName = student.FirstName;
                temp.LastName = student.LastName;
            }

            return RedirectToPage();
        }
    }
}
