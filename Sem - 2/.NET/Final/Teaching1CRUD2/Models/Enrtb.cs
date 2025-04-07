using System;
using System.Collections.Generic;

namespace Teaching1CRUD2.Models;

public partial class Enrtb
{
    public int Eid { get; set; }

    public int? Sid { get; set; }

    public int? Cid { get; set; }

    public virtual Course? CidNavigation { get; set; }

    public virtual Stud? SidNavigation { get; set; }
}
