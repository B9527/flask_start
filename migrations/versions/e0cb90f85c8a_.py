"""empty message

Revision ID: e0cb90f85c8a
Revises: f87aa97231e0
Create Date: 2018-04-03 16:11:53.489940

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0cb90f85c8a'
down_revision = 'f87aa97231e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('Username', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'Username')
    # ### end Alembic commands ###
