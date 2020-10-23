"""empty message

Revision ID: 02279cd845bb
Revises: 9998c465c6ca
Create Date: 2020-07-05 13:41:38.547426

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02279cd845bb'
down_revision = '9998c465c6ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'img_path')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('img_path', sa.VARCHAR(length=1000), autoincrement=False, nullable=True))
    # ### end Alembic commands ###