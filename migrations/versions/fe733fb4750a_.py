"""empty message

Revision ID: fe733fb4750a
Revises: caddff20f01d
Create Date: 2020-05-04 19:42:00.478523

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe733fb4750a'
down_revision = 'caddff20f01d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('slot', 'slug')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('slot', sa.Column('slug', sa.VARCHAR(length=128), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
