"""empty message

Revision ID: 27f5eacbc91a
Revises: 1acc35c424a8
Create Date: 2020-05-04 21:40:44.270625

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27f5eacbc91a'
down_revision = '1acc35c424a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('drop', sa.Column('archived', sa.Boolean(), server_default='0', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('drop', 'archived')
    # ### end Alembic commands ###