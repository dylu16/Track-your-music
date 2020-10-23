"""empty message

Revision ID: 49f472077583
Revises: 0cf274e8404a
Create Date: 2020-07-29 21:17:52.949687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49f472077583'
down_revision = '0cf274e8404a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fingerprints',
    sa.Column('hash', sa.Binary(), nullable=False),
    sa.Column('song_id', sa.Integer(), nullable=False),
    sa.Column('offset', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('date_modified', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['song_id'], ['songs.song_id'], ),
    sa.PrimaryKeyConstraint('hash', 'song_id', 'offset')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fingerprints')
    # ### end Alembic commands ###