using System;
using System.Collections.Generic;

namespace Assignment_4.Models;

public partial class Coursestb
{
    public int Cid { get; set; }

    public string? Cname { get; set; }

    public string? Cdesc { get; set; }

    public virtual ICollection<Enrollementtb> Enrollementtbs { get; set; } = new List<Enrollementtb>();
}
