using System;
using System.Collections.Generic;

namespace Teaching1CRUD2.Models;

public partial class Stud
{
    public int Sid { get; set; }

    public string? Sname { get; set; }

    public virtual ICollection<Enrtb> Enrtbs { get; set; } = new List<Enrtb>();
}
