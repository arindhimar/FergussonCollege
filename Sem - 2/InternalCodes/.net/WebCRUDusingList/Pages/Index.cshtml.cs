using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using WebCRUDusingList.Models;

public class IndexModel : PageModel
{
    public static List<Student> Students = new();

    [BindProperty]
    public Student Student { get; set; }

    [BindProperty]
    public int? EditId { get; set; }

    public void OnGet() { }

    public IActionResult OnPostAdd()
    {
        if (!Students.Any(s => s.Id == Student.Id))
            Students.Add(Student);
        return RedirectToPage();
    }

    public IActionResult OnPostDelete(int id)
    {
        Students.RemoveAll(s => s.Id == id);
        return RedirectToPage();
    }

    public IActionResult OnPostEdit()
    {
        var s = Students.FirstOrDefault(x => x.Id == Student.Id);
        if (s != null)
        {
            s.Name = Student.Name;
            s.Age = Student.Age;
        }
        return RedirectToPage();
    }
}
