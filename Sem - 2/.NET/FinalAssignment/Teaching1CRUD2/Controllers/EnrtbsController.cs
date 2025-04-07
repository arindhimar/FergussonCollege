using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using Teaching1CRUD2.Models;

namespace Teaching1CRUD2.Controllers
{
    public class EnrtbsController : Controller
    {
        private readonly Teaching1Context _context;

        public EnrtbsController(Teaching1Context context)
        {
            _context = context;
        }

        // GET: Enrtbs
        public async Task<IActionResult> Index()
        {
            var teaching1Context = _context.Enrtbs.Include(e => e.CidNavigation).Include(e => e.SidNavigation);
            return View(await teaching1Context.ToListAsync());
        }

        // GET: Enrtbs/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var enrtb = await _context.Enrtbs
                .Include(e => e.CidNavigation)
                .Include(e => e.SidNavigation)
                .FirstOrDefaultAsync(m => m.Eid == id);
            if (enrtb == null)
            {
                return NotFound();
            }

            return View(enrtb);
        }

        // GET: Enrtbs/Create
        public IActionResult Create()
        {
            ViewData["Cid"] = new SelectList(_context.Courses, "Cid", "Cname");
            ViewData["Sid"] = new SelectList(_context.Studs, "Sid", "Sname");
            return View();
        }

        // POST: Enrtbs/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Eid,Sid,Cid")] Enrtb enrtb)
        {
            if (ModelState.IsValid)
            {
                _context.Add(enrtb);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            ViewData["Cid"] = new SelectList(_context.Courses, "Cid", "Cid", enrtb.Cid);
            ViewData["Sid"] = new SelectList(_context.Studs, "Sid", "Sid", enrtb.Sid);
            return View(enrtb);
        }

        // GET: Enrtbs/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var enrtb = await _context.Enrtbs.FindAsync(id);
            if (enrtb == null)
            {
                return NotFound();
            }
            ViewData["Cid"] = new SelectList(_context.Courses, "Cid", "Cid", enrtb.Cid);
            ViewData["Sid"] = new SelectList(_context.Studs, "Sid", "Sid", enrtb.Sid);
            return View(enrtb);
        }

        // POST: Enrtbs/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Eid,Sid,Cid")] Enrtb enrtb)
        {
            if (id != enrtb.Eid)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(enrtb);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!EnrtbExists(enrtb.Eid))
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
            ViewData["Cid"] = new SelectList(_context.Courses, "Cid", "Cid", enrtb.Cid);
            ViewData["Sid"] = new SelectList(_context.Studs, "Sid", "Sid", enrtb.Sid);
            return View(enrtb);
        }

        // GET: Enrtbs/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var enrtb = await _context.Enrtbs
                .Include(e => e.CidNavigation)
                .Include(e => e.SidNavigation)
                .FirstOrDefaultAsync(m => m.Eid == id);
            if (enrtb == null)
            {
                return NotFound();
            }

            return View(enrtb);
        }

        // POST: Enrtbs/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            var enrtb = await _context.Enrtbs.FindAsync(id);
            if (enrtb != null)
            {
                _context.Enrtbs.Remove(enrtb);
            }

            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool EnrtbExists(int id)
        {
            return _context.Enrtbs.Any(e => e.Eid == id);
        }
    }
}
