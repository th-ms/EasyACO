"""empty message

Revision ID: 915d3352d0fc
Revises: 27f5eacbc91a
Create Date: 2020-05-04 22:41:56.464527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '915d3352d0fc'
down_revision = '27f5eacbc91a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('color', sa.String(length=16), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'color')
    # ### end Alembic commands ###
