using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace WebCRUD.Pages
{
    public class IndexModel : PageModel
    {

        public static List <Stundent> studs = new List<Stundent> ();

        [BindProperty]
        public Stundent student { get; set; }

        public void OnGet()
        {

        }

        public IActionResult OnPostAdd()
        {
            studs.Add (student);

            return RedirectToPage();
        }

        public IActionResult OnPostDelete(int id)
        {

            studs.RemoveAll(st=>st.Id==id);

            return RedirectToPage();

        }

        public IActionResult OnPostEdit()
        {

            Stundent st = studs.Where(st => st.Id == student.Id).FirstOrDefault();

            if (st != null)
            {
                st.Name = student.Name;
                st.Description = student.Description;
            }

            return RedirectToPage();

        }

    }

    public class Stundent
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Description { get; set; }
    }
}
