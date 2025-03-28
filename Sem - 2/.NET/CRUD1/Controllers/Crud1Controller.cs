using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using CRUD1.Models;

namespace CRUD1.Controllers
{
    public class Crud1Controller : Controller
    {
        private readonly Crud1Context _context;

        public Crud1Controller(Crud1Context context)
        {
            _context = context;
        }

        // GET: Crud1
        public async Task<IActionResult> Index()
        {
            return View(await _context.Crud1s.ToListAsync());
        }

        // GET: Crud1/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var crud1 = await _context.Crud1s
                .FirstOrDefaultAsync(m => m.Id == id);
            if (crud1 == null)
            {
                return NotFound();
            }

            return View(crud1);
        }

        // GET: Crud1/Create
        public IActionResult Create()
        {
            return View();
        }

        // POST: Crud1/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,Name,Age")] Crud1 crud1)
        {
            if (ModelState.IsValid)
            {
                _context.Add(crud1);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            return View(crud1);
        }

        // GET: Crud1/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var crud1 = await _context.Crud1s.FindAsync(id);
            if (crud1 == null)
            {
                return NotFound();
            }
            return View(crud1);
        }

        // POST: Crud1/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Id,Name,Age")] Crud1 crud1)
        {
            if (id != crud1.Id)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(crud1);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!Crud1Exists(crud1.Id))
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
            return View(crud1);
        }

        // GET: Crud1/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var crud1 = await _context.Crud1s
                .FirstOrDefaultAsync(m => m.Id == id);
            if (crud1 == null)
            {
                return NotFound();
            }

            return View(crud1);
        }

        // POST: Crud1/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            var crud1 = await _context.Crud1s.FindAsync(id);
            if (crud1 != null)
            {
                _context.Crud1s.Remove(crud1);
            }

            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool Crud1Exists(int id)
        {
            return _context.Crud1s.Any(e => e.Id == id);
        }
    }
}
