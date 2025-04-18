using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace WebCRUDFinal.Pages
{
    public class IndexModel : PageModel
    {
        public class Stundent
        {
            public int Id { get; set; }
            public string Name { get; set; }
        }

        public static List<Stundent> Stundents  = new List<Stundent>();

        [BindProperty]
        public Stundent stundent { get; set; }

        public void OnGet()
        {

        }


        public IActionResult OnPostAdd()
        {
            Stundents.Add(stundent);
            return RedirectToPage();
        }

        public IActionResult OnPostEdit()
        {
            Stundent temp = Stundents.Where(s => s.Id == stundent.Id).FirstOrDefault();


            if (temp != null)
            {
                temp.Id = stundent.Id;
                temp.Name = stundent.Name;
            }

            return RedirectToPage();
        }

        public IActionResult OnPostDelete(int id)
        {
            Stundent temp = Stundents.Where(s=>s.Id==id).FirstOrDefault();
            if (temp != null)
            {
                Stundents.Remove(temp);
            }

            return RedirectToPage();
        }

    }
}
