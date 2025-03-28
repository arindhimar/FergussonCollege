using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using Assignment_4.Models;

namespace Assignment_4.Controllers
{
    public class CoursestbsController : Controller
    {
        private readonly Assignment4Context _context;

        public CoursestbsController(Assignment4Context context)
        {
            _context = context;
        }

        // GET: Coursestbs
        public async Task<IActionResult> Index()
        {
            return View(await _context.Coursestbs.ToListAsync());
        }

        // GET: Coursestbs/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var coursestb = await _context.Coursestbs
                .FirstOrDefaultAsync(m => m.Cid == id);
            if (coursestb == null)
            {
                return NotFound();
            }

            return View(coursestb);
        }

        // GET: Coursestbs/Create
        public IActionResult Create()
        {
            return View();
        }

        // POST: Coursestbs/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Cid,Cname,Cdesc")] Coursestb coursestb)
        {
            if (ModelState.IsValid)
            {
                _context.Add(coursestb);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            return View(coursestb);
        }

        // GET: Coursestbs/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var coursestb = await _context.Coursestbs.FindAsync(id);
            if (coursestb == null)
            {
                return NotFound();
            }
            return View(coursestb);
        }

        // POST: Coursestbs/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Cid,Cname,Cdesc")] Coursestb coursestb)
        {
            if (id != coursestb.Cid)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(coursestb);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!CoursestbExists(coursestb.Cid))
                    {
                        return NotFound();
                    }
                    else
                    {
                        throw;
                    }
                }
                return RedirectToAction(nameof(Index));
            }
            return View(coursestb);
        }

        // GET: Coursestbs/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var coursestb = await _context.Coursestbs
                .FirstOrDefaultAsync(m => m.Cid == id);
            if (coursestb == null)
            {
                return NotFound();
            }

            return View(coursestb);
        }

        // POST: Coursestbs/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            var coursestb = await _context.Coursestbs.FindAsync(id);
            if (coursestb != null)
            {
                _context.Coursestbs.Remove(coursestb);
            }

            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool CoursestbExists(int id)
        {
            return _context.Coursestbs.Any(e => e.Cid == id);
        }
    }
}
