using Microsoft.AspNetCore.Mvc;

namespace MyPortfolio.Controllers
{
    public class HomeController : Controller
    {
        // Home page action
        public IActionResult Index()
        {
            return View();
        }

        // About page action
        public IActionResult About()
        {
            return View();
        }

        // Projects page action
        public IActionResult Projects()
        {
            return View();
        }

        // Contact page action
        public IActionResult Contact()
        {
            return View();
        }
    }
}
