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
    public class EnrollementtbsController : Controller
    {
        private readonly Assignment4Context _context;

        public EnrollementtbsController(Assignment4Context context)
        {
            _context = context;
        }

        // GET: Enrollementtbs
        public async Task<IActionResult> Index()
        {
            var assignment4Context = _context.Enrollementtbs.Include(e => e.CidNavigation).Include(e => e.SidNavigation);
            return View(await assignment4Context.ToListAsync());
        }

        // GET: Enrollementtbs/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var enrollementtb = await _context.Enrollementtbs
                .Include(e => e.CidNavigation)
                .Include(e => e.SidNavigation)
                .FirstOrDefaultAsync(m => m.Eid == id);
            if (enrollementtb == null)
            {
                return NotFound();
            }

            return View(enrollementtb);
        }

        // GET: Enrollementtbs/Create
        public IActionResult Create()
        {
            ViewData["Cid"] = new SelectList(_context.Coursestbs, "Cid", "Cid");
            ViewData["Sid"] = new SelectList(_context.Studenttbs, "Sid", "Sid");
            return View();
        }

        // POST: Enrollementtbs/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Eid,Sid,Cid,Edate")] Enrollementtb enrollementtb)
        {
            if (ModelState.IsValid)
            {
                _context.Add(enrollementtb);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            ViewData["Cid"] = new SelectList(_context.Coursestbs, "Cid", "Cid", enrollementtb.Cid);
            ViewData["Sid"] = new SelectList(_context.Studenttbs, "Sid", "Sid", enrollementtb.Sid);
            return View(enrollementtb);
        }

        // GET: Enrollementtbs/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var enrollementtb = await _context.Enrollementtbs.FindAsync(id);
            if (enrollementtb == null)
            {
                return NotFound();
            }
            ViewData["Cid"] = new SelectList(_context.Coursestbs, "Cid", "Cid", enrollementtb.Cid);
            ViewData["Sid"] = new SelectList(_context.Studenttbs, "Sid", "Sid", enrollementtb.Sid);
            return View(enrollementtb);
        }

        // POST: Enrollementtbs/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Eid,Sid,Cid,Edate")] Enrollementtb enrollementtb)
        {
            if (id != enrollementtb.Eid)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(enrollementtb);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!EnrollementtbExists(enrollementtb.Eid))
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
            ViewData["Cid"] = new SelectList(_context.Coursestbs, "Cid", "Cid", enrollementtb.Cid);
            ViewData["Sid"] = new SelectList(_context.Studenttbs, "Sid", "Sid", enrollementtb.Sid);
            return View(enrollementtb);
        }

        // GET: Enrollementtbs/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var enrollementtb = await _context.Enrollementtbs
                .Include(e => e.CidNavigation)
                .Include(e => e.SidNavigation)
                .FirstOrDefaultAsync(m => m.Eid == id);
            if (enrollementtb == null)
            {
                return NotFound();
            }

            return View(enrollementtb);
        }

        // POST: Enrollementtbs/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            var enrollementtb = await _context.Enrollementtbs.FindAsync(id);
            if (enrollementtb != null)
            {
                _context.Enrollementtbs.Remove(enrollementtb);
            }

            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool EnrollementtbExists(int id)
        {
            return _context.Enrollementtbs.Any(e => e.Eid == id);
        }
    }
}
