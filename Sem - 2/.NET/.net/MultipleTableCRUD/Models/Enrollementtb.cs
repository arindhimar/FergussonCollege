using System;
using System.Collections.Generic;

namespace MultipleTableCRUD.Models;

public partial class Enrollementtb
{
    public int Eid { get; set; }

    public int? Sid { get; set; }

    public int? Cid { get; set; }

    public DateOnly? Edate { get; set; }

    public virtual Coursestb? CidNavigation { get; set; }

    public virtual Studenttb? SidNavigation { get; set; }
}
