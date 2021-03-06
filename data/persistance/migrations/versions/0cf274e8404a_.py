"""empty message

Revision ID: 0cf274e8404a
Revises: 4d205ebdc619
Create Date: 2020-07-29 21:11:22.321366

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0cf274e8404a'
down_revision = '4d205ebdc619'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_fingerprints_hash', table_name='fingerprints')
    op.drop_table('fingerprints')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fingerprints',
    sa.Column('hash', postgresql.BYTEA(), autoincrement=False, nullable=False),
    sa.Column('song_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('offset', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('date_created', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.Column('date_modified', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['song_id'], ['songs.song_id'], name='fk_fingerprints_song_id', ondelete='CASCADE'),
    sa.UniqueConstraint('song_id', 'offset', 'hash', name='uq_fingerprints')
    )
    op.create_index('ix_fingerprints_hash', 'fingerprints', ['hash'], unique=False)
    # ### end Alembic commands ###
