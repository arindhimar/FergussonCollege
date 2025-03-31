using Microsoft.AspNetCore.Mvc;
using Question11.Models;
using System.Collections.Generic;
using System.Linq;

namespace Question11.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class StudentController : ControllerBase
    {
        private static List<Student> students = new List<Student>
        {
            new Student { Id = 1, Name = "Arin Dhimar", Age = 20, Course = "Computer Science" },
            new Student { Id = 2, Name = "Ashish Dhimar", Age = 22, Course = "Data Science" }
        };

        // GET: api/student
        [HttpGet]
        public ActionResult<IEnumerable<Student>> GetStudents()
        {
            return Ok(students);
        }

        // GET: api/student/{id}
        [HttpGet("{id}")]
        public ActionResult<Student> GetStudentById(int id)
        {
            var student = students.FirstOrDefault(s => s.Id == id);
            if (student == null)
                return NotFound(new { message = "Student not found" });

            return Ok(student);
        }

        // POST: api/student
        [HttpPost]
        public ActionResult<Student> AddStudent([FromBody] Student newStudent)
        {
            if (newStudent == null || string.IsNullOrWhiteSpace(newStudent.Name) || newStudent.Age <= 0)
                return BadRequest("Invalid student data");

            newStudent.Id = students.Count + 1;
            students.Add(newStudent);

            return CreatedAtAction(nameof(GetStudentById), new { id = newStudent.Id }, newStudent);
        }

        // PUT: api/student/{id}
        [HttpPut("{id}")]
        public ActionResult UpdateStudent(int id, [FromBody] Student updatedStudent)
        {
            var student = students.FirstOrDefault(s => s.Id == id);
            if (student == null)
                return NotFound(new { message = "Student not found" });

            if (string.IsNullOrWhiteSpace(updatedStudent.Name) || updatedStudent.Age <= 0)
                return BadRequest("Invalid student data");

            student.Name = updatedStudent.Name;
            student.Age = updatedStudent.Age;
            student.Course = updatedStudent.Course;

            return NoContent();
        }

        // DELETE: api/student/{id}
        [HttpDelete("{id}")]
        public ActionResult DeleteStudent(int id)
        {
            var student = students.FirstOrDefault(s => s.Id == id);
            if (student == null)
                return NotFound(new { message = "Student not found" });

            students.Remove(student);
            return NoContent();
        }
    }
}
