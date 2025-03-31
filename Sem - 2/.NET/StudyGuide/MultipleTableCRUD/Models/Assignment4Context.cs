using System;
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore;

namespace MultipleTableCRUD.Models;

public partial class Assignment4Context : DbContext
{
    public Assignment4Context()
    {
    }

    public Assignment4Context(DbContextOptions<Assignment4Context> options)
        : base(options)
    {
    }

    public virtual DbSet<Coursestb> Coursestbs { get; set; }

    public virtual DbSet<Enrollementtb> Enrollementtbs { get; set; }

    public virtual DbSet<Studenttb> Studenttbs { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
#warning To protect potentially sensitive information in your connection string, you should move it out of source code. You can avoid scaffolding the connection string by using the Name= syntax to read it from configuration - see https://go.microsoft.com/fwlink/?linkid=2131148. For more guidance on storing connection strings, see https://go.microsoft.com/fwlink/?LinkId=723263.
        => optionsBuilder.UseSqlServer("Data Source=Arin;Initial Catalog=assignment4;Integrated Security=True;Encrypt=True;Trust Server Certificate=True");

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Coursestb>(entity =>
        {
            entity.HasKey(e => e.Cid);

            entity.ToTable("coursestb");

            entity.Property(e => e.Cid)
                .ValueGeneratedNever()
                .HasColumnName("cid");
            entity.Property(e => e.Cdesc)
                .HasMaxLength(50)
                .IsUnicode(false)
                .HasColumnName("cdesc");
            entity.Property(e => e.Cname)
                .HasMaxLength(50)
                .IsUnicode(false)
                .HasColumnName("cname");
        });

        modelBuilder.Entity<Enrollementtb>(entity =>
        {
            entity.HasKey(e => e.Eid);

            entity.ToTable("enrollementtb");

            entity.Property(e => e.Eid)
                .ValueGeneratedNever()
                .HasColumnName("eid");
            entity.Property(e => e.Cid).HasColumnName("cid");
            entity.Property(e => e.Edate).HasColumnName("edate");
            entity.Property(e => e.Sid).HasColumnName("sid");

            entity.HasOne(d => d.CidNavigation).WithMany(p => p.Enrollementtbs)
                .HasForeignKey(d => d.Cid)
                .HasConstraintName("FK_enrollementtb_coursestb");

            entity.HasOne(d => d.SidNavigation).WithMany(p => p.Enrollementtbs)
                .HasForeignKey(d => d.Sid)
                .HasConstraintName("FK_enrollementtb_studenttb");
        });

        modelBuilder.Entity<Studenttb>(entity =>
        {
            entity.HasKey(e => e.Sid);

            entity.ToTable("studenttb");

            entity.Property(e => e.Sid)
                .ValueGeneratedNever()
                .HasColumnName("sid");
            entity.Property(e => e.Email)
                .HasMaxLength(50)
                .IsUnicode(false)
                .HasColumnName("email");
            entity.Property(e => e.Fname)
                .HasMaxLength(50)
                .IsUnicode(false)
                .HasColumnName("fname");
            entity.Property(e => e.Lname)
                .HasMaxLength(50)
                .IsUnicode(false)
                .HasColumnName("lname");
            entity.Property(e => e.Phone)
                .HasMaxLength(50)
                .IsUnicode(false)
                .HasColumnName("phone");
        });

        OnModelCreatingPartial(modelBuilder);
    }

    partial void OnModelCreatingPartial(ModelBuilder modelBuilder);
}
