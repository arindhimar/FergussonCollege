using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace WebCRUD.Pages
{
    public class Student
    {
        public int Id { get; set; }
        public string Name { get; set; }
    }

    public class IndexModel : PageModel
    {
        public static List<Student> students=   new List<Student>();

        [BindProperty]
        public Student student { get; set; }

        public void OnGet()
        {

        }

        public IActionResult OnPostAdd()
        {
            students.Add(student);

            return RedirectToPage();
        }

        public IActionResult OnPostDelete(int id)
        {
            students.RemoveAll(x => x.Id == id);

            return RedirectToPage();
        }

        public IActionResult OnPostEdit()
        {
            Student temp = students.Where(s=>s.Id==student.Id).FirstOrDefault();

            if (temp != null) {
                temp.Name = student.Name;
            }


            return RedirectToPage();
        }


    }
}
