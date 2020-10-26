"""empty message

Revision ID: ff1dc9e841da
Revises: d26eeda531b7
Create Date: 2020-05-04 19:32:45.266418

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff1dc9e841da'
down_revision = 'd26eeda531b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('drop', sa.Column('drop_slug', sa.String(length=128), nullable=True))
    op.drop_column('drop', 'slug')
    op.add_column('slot', sa.Column('slot_slug', sa.String(length=128), nullable=True))
    op.drop_column('slot', 'slug')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('slot', sa.Column('slug', sa.VARCHAR(length=128), autoincrement=False, nullable=True))
    op.drop_column('slot', 'slot_slug')
    op.add_column('drop', sa.Column('slug', sa.VARCHAR(length=128), autoincrement=False, nullable=True))
    op.drop_column('drop', 'drop_slug')
    # ### end Alembic commands ###
