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
    public class StudenttbsController : Controller
    {
        private readonly Assignment4Context _context;

        public StudenttbsController(Assignment4Context context)
        {
            _context = context;
        }

        // GET: Studenttbs
        public async Task<IActionResult> Index()
        {
            return View(await _context.Studenttbs.ToListAsync());
        }

        // GET: Studenttbs/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var studenttb = await _context.Studenttbs
                .FirstOrDefaultAsync(m => m.Sid == id);
            if (studenttb == null)
            {
                return NotFound();
            }

            return View(studenttb);
        }

        // GET: Studenttbs/Create
        public IActionResult Create()
        {
            return View();
        }

        // POST: Studenttbs/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Sid,Fname,Lname,Email,Phone")] Studenttb studenttb)
        {
            if (ModelState.IsValid)
            {
                _context.Add(studenttb);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            return View(studenttb);
        }

        // GET: Studenttbs/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var studenttb = await _context.Studenttbs.FindAsync(id);
            if (studenttb == null)
            {
                return NotFound();
            }
            return View(studenttb);
        }

        // POST: Studenttbs/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Sid,Fname,Lname,Email,Phone")] Studenttb studenttb)
        {
            if (id != studenttb.Sid)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(studenttb);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!StudenttbExists(studenttb.Sid))
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
            return View(studenttb);
        }

        // GET: Studenttbs/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var studenttb = await _context.Studenttbs
                .FirstOrDefaultAsync(m => m.Sid == id);
            if (studenttb == null)
            {
                return NotFound();
            }

            return View(studenttb);
        }

        // POST: Studenttbs/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            var studenttb = await _context.Studenttbs.FindAsync(id);
            if (studenttb != null)
            {
                _context.Studenttbs.Remove(studenttb);
            }

            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool StudenttbExists(int id)
        {
            return _context.Studenttbs.Any(e => e.Sid == id);
        }
    }
}
