"""empty message

Revision ID: a6b107eeffab
Revises: 5d7693a4eafc
Create Date: 2021-03-05 02:14:36.656827

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6b107eeffab'
down_revision = '5d7693a4eafc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'password')
    # ### end Alembic commands ###
