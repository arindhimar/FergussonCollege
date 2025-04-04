using System;
using System.Collections.Generic;

namespace MultipleTableCRUD.Models;

public partial class Coursestb
{
    public int Cid { get; set; }

    public string? Cname { get; set; }

    public string? Cdesc { get; set; }

    public virtual ICollection<Enrollementtb> Enrollementtbs { get; set; } = new List<Enrollementtb>();
}
