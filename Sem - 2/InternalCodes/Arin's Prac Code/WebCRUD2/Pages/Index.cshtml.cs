using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace WebCRUD2.Pages
{
    public class IndexModel : PageModel
    {
        public class Stundent
        {
            public int id { get; set; }
            public string Name { get; set; }
        }

        public static List<Stundent> Stundents = new List<Stundent>();


        [BindProperty]
        public Stundent student { get; set; }

        public void OnGet()
        {

        }

        public IActionResult OnPostAdd()
        {
            Stundents.Add(student);
            return RedirectToPage();
        }

        public IActionResult OnPostDelete(int id)
        {
            Stundents.RemoveAll(x => x.id == id);
            return RedirectToPage();

        }

        public IActionResult OnPostEdit()
        {
            Stundent tempStundent = Stundents.Where(s=>s.id==student.id).FirstOrDefault();

            if (tempStundent != null)
            {
                tempStundent.Name = student.Name;
            }
            return RedirectToPage();

        }
    }
}
