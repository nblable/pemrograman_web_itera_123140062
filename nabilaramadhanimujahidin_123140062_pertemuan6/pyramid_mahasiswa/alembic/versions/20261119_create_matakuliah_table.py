"""create matakuliah table

Revision ID: 68876b248e7e
Revises: d53b0a04a080
Create Date: 2026-11-19 20:42:56.170971

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68876b248e7e'
down_revision = 'd53b0a04a080'
branch_labels = None
depends_on = None


def upgrade():
    """Membuat tabel matakuliah."""
    op.create_table(
        'matakuliah',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('kode_mk', sa.Text(), nullable=False),
        sa.Column('nama_mk', sa.Text(), nullable=False),
        sa.Column('sks', sa.Integer(), nullable=False),
        sa.Column('semester', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_matakuliah')),
        sa.UniqueConstraint('kode_mk', name=op.f('uq_matakuliah_kode_mk')),
    )


def downgrade():
    """Menghapus tabel matakuliah."""
    op.drop_table('matakuliah')
