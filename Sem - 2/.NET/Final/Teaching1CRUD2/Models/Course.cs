using System;
using System.Collections.Generic;

namespace Teaching1CRUD2.Models;

public partial class Course
{
    public int Cid { get; set; }

    public string? Cname { get; set; }

    public virtual ICollection<Enrtb> Enrtbs { get; set; } = new List<Enrtb>();
}
