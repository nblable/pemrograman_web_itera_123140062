"""create mahasiswa table

Revision ID: d53b0a04a080
Revises:
Create Date: 2026-11-19 20:42:21.800415

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd53b0a04a080'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    """Membuat tabel mahasiswa."""
    op.create_table(
        'mahasiswa',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nim', sa.Text(), nullable=False),
        sa.Column('nama', sa.Text(), nullable=False),
        sa.Column('jurusan', sa.Text(), nullable=False),
        sa.Column('tanggal_lahir', sa.Date(), nullable=True),
        sa.Column('alamat', sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_mahasiswa')),
        sa.UniqueConstraint('nim', name=op.f('uq_mahasiswa_nim')),
    )


def downgrade():
    """Menghapus tabel mahasiswa."""
    op.drop_table('mahasiswa')
