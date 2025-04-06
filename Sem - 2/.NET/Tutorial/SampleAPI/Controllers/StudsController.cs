using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using SampleAPI.Models;

namespace SampleAPI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class StudsController : ControllerBase
    {
        private readonly LoltrycrudContext _context;

        public StudsController(LoltrycrudContext context)
        {
            _context = context;
        }

        // GET: api/Studs
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Stud>>> GetStuds()
        {
            return await _context.Studs.ToListAsync();
        }

        // GET: api/Studs/5
        [HttpGet("{id}")]
        public async Task<ActionResult<Stud>> GetStud(int id)
        {
            var stud = await _context.Studs.FindAsync(id);

            if (stud == null)
            {
                return NotFound();
            }

            return stud;
        }

        // PUT: api/Studs/5
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPut("{id}")]
        public async Task<IActionResult> PutStud(int id, Stud stud)
        {
            if (id != stud.Sid)
            {
                return BadRequest();
            }

            _context.Entry(stud).State = EntityState.Modified;

            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!StudExists(id))
                {
                    return NotFound();
                }
                else
                {
                    throw;
                }
            }

            return NoContent();
        }

        // POST: api/Studs
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPost]
        public async Task<ActionResult<Stud>> PostStud(Stud stud)
        {
            _context.Studs.Add(stud);
            await _context.SaveChangesAsync();

            return CreatedAtAction("GetStud", new { id = stud.Sid }, stud);
        }

        // DELETE: api/Studs/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteStud(int id)
        {
            var stud = await _context.Studs.FindAsync(id);
            if (stud == null)
            {
                return NotFound();
            }

            _context.Studs.Remove(stud);
            await _context.SaveChangesAsync();

            return NoContent();
        }

        private bool StudExists(int id)
        {
            return _context.Studs.Any(e => e.Sid == id);
        }
    }
}
