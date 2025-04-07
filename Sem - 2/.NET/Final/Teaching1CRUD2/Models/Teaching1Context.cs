using System;
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore;

namespace Teaching1CRUD2.Models;

public partial class Teaching1Context : DbContext
{
    public Teaching1Context()
    {
    }

    public Teaching1Context(DbContextOptions<Teaching1Context> options)
        : base(options)
    {
    }

    public virtual DbSet<Course> Courses { get; set; }

    public virtual DbSet<Enrtb> Enrtbs { get; set; }

    public virtual DbSet<Stud> Studs { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
#warning To protect potentially sensitive information in your connection string, you should move it out of source code. You can avoid scaffolding the connection string by using the Name= syntax to read it from configuration - see https://go.microsoft.com/fwlink/?linkid=2131148. For more guidance on storing connection strings, see https://go.microsoft.com/fwlink/?LinkId=723263.
        => optionsBuilder.UseSqlServer("Data Source=Arin;Initial Catalog=Teaching1;Integrated Security=True;Trust Server Certificate=True");

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Course>(entity =>
        {
            entity.HasKey(e => e.Cid);

            entity.ToTable("course");

            entity.Property(e => e.Cid).HasColumnName("cid");
            entity.Property(e => e.Cname)
                .HasMaxLength(50)
                .IsUnicode(false)
                .HasColumnName("cname");
        });

        modelBuilder.Entity<Enrtb>(entity =>
        {
            entity.HasKey(e => e.Eid);

            entity.ToTable("enrtb");

            entity.Property(e => e.Eid).HasColumnName("eid");
            entity.Property(e => e.Cid).HasColumnName("cid");
            entity.Property(e => e.Sid).HasColumnName("sid");

            entity.HasOne(d => d.CidNavigation).WithMany(p => p.Enrtbs)
                .HasForeignKey(d => d.Cid)
                .HasConstraintName("FK_enrtb_course");

            entity.HasOne(d => d.SidNavigation).WithMany(p => p.Enrtbs)
                .HasForeignKey(d => d.Sid)
                .HasConstraintName("FK_enrtb_stud");
        });

        modelBuilder.Entity<Stud>(entity =>
        {
            entity.HasKey(e => e.Sid);

            entity.ToTable("stud");

            entity.Property(e => e.Sid).HasColumnName("sid");
            entity.Property(e => e.Sname)
                .HasMaxLength(50)
                .IsUnicode(false)
                .HasColumnName("sname");
        });

        OnModelCreatingPartial(modelBuilder);
    }

    partial void OnModelCreatingPartial(ModelBuilder modelBuilder);
}
