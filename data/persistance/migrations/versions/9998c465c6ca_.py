"""empty message

Revision ID: 9998c465c6ca
Revises: 
Create Date: 2020-07-04 14:44:44.979060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9998c465c6ca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=30), nullable=False),
    sa.Column('lastname', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.Column('img_path', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###