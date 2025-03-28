using System;
using System.Collections.Generic;

namespace Assignment_4.Models;

public partial class Studenttb
{
    public int Sid { get; set; }

    public string? Fname { get; set; }

    public string? Lname { get; set; }

    public byte[]? Email { get; set; }

    public byte[]? Phone { get; set; }

    public virtual ICollection<Enrollementtb> Enrollementtbs { get; set; } = new List<Enrollementtb>();
}
