"""empty message

Revision ID: b0d0515035e2
Revises: d5b9c01b097c
Create Date: 2020-07-29 20:53:52.345795

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b0d0515035e2'
down_revision = 'd5b9c01b097c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('song')
    op.drop_index('ix_fingerprints_hash', table_name='fingerprints')
    op.drop_table('fingerprints')
    op.add_column('songs', sa.Column('id', sa.Integer(), nullable=False))
    op.create_unique_constraint(None, 'songs', ['file_sha1'])
    op.drop_column('songs', 'song_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('songs', sa.Column('song_id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.drop_constraint(None, 'songs', type_='unique')
    op.drop_column('songs', 'id')
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
    op.create_table('song',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('song_name', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.Column('fingerprinted', sa.SMALLINT(), autoincrement=False, nullable=False),
    sa.Column('file_sha1', postgresql.BYTEA(), autoincrement=False, nullable=False),
    sa.Column('total_hashes', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('date_created', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('date_modified', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='song_pkey'),
    sa.UniqueConstraint('file_sha1', name='song_file_sha1_key')
    )
    # ### end Alembic commands ###
