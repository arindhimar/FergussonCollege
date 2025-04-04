using System;
using System.Collections.Generic;

namespace MultipleTableCRUD.Models;

public partial class Studenttb
{
    public int Sid { get; set; }

    public string? Fname { get; set; }

    public string? Lname { get; set; }

    public string? Email { get; set; }

    public string? Phone { get; set; }

    public virtual ICollection<Enrollementtb> Enrollementtbs { get; set; } = new List<Enrollementtb>();
}
