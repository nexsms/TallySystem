"""add tenant relation to voters

Revision ID: dc78d0ebd954
Revises: 77baeef8bdf7
Create Date: 2025-10-23 12:31:06.563910
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dc78d0ebd954'
down_revision: Union[str, Sequence[str], None] = '77baeef8bdf7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column('agents', 'first_name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('agents', 'last_name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('agents', 'ward_id',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               nullable=False,
               postgresql_using='ward_id::integer')   # ✅ Fix cast here

    op.alter_column('constituencies', 'id',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True,
               postgresql_using='id::integer')         # ✅
    op.alter_column('constituencies', 'county_id',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=False,
               postgresql_using='county_id::integer')  # ✅
    op.alter_column('counties', 'id',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True,
               postgresql_using='id::integer')         # ✅
    op.alter_column('voters', 'ward_code',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               nullable=False,
               postgresql_using='ward_code::integer')  # ✅
    op.alter_column('voters', 'county_code',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=True,
               postgresql_using='county_code::integer')  # ✅
    op.alter_column('voters', 'constituency_code',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=True,
               postgresql_using='constituency_code::integer')  # ✅
    op.alter_column('wards', 'id',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True,
               postgresql_using='id::integer')         # ✅
    op.alter_column('wards', 'constituency_id',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=False,
               postgresql_using='constituency_id::integer')  # ✅


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column('wards', 'constituency_id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=False)
    op.alter_column('wards', 'id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('voters', 'constituency_code',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=True)
    op.alter_column('voters', 'county_code',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=True)
    op.alter_column('voters', 'ward_code',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               nullable=True)
    op.alter_column('counties', 'id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('constituencies', 'county_id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=False)
    op.alter_column('constituencies', 'id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('agents', 'ward_id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               nullable=True)
    op.alter_column('agents', 'last_name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('agents', 'first_name',
               existing_type=sa.VARCHAR(),
               nullable=True)
