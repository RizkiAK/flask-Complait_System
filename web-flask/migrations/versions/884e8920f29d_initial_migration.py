"""Initial migration.

Revision ID: 884e8920f29d
Revises: 
Create Date: 2021-08-04 23:31:16.981815

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '884e8920f29d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tinformasi',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('judul', sa.String(length=100), nullable=False),
    sa.Column('informasi', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('tmahasiswa', sa.Column('nohp', sa.String(length=200), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tmahasiswa', 'nohp')
    op.drop_table('tinformasi')
    # ### end Alembic commands ###
