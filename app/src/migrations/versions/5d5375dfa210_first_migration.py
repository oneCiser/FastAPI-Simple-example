"""first migration

Revision ID: 5d5375dfa210
Revises: ddf6ac7e0f01
Create Date: 2022-02-27 20:31:03.381872

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d5375dfa210'
down_revision = 'ddf6ac7e0f01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('abilities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('is_main_series', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_abilities_id'), 'abilities', ['id'], unique=False)
    op.create_index(op.f('ix_abilities_name'), 'abilities', ['name'], unique=True)
    op.create_table('pokemons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('weight', sa.Integer(), nullable=False),
    sa.Column('location_area_encounters', sa.String(length=200), nullable=False),
    sa.Column('last_consulted', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pokemons_id'), 'pokemons', ['id'], unique=False)
    op.create_index(op.f('ix_pokemons_name'), 'pokemons', ['name'], unique=True)
    op.create_table('stats',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('game_index', sa.Integer(), nullable=False),
    sa.Column('is_battle_only', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_stats_id'), 'stats', ['id'], unique=False)
    op.create_index(op.f('ix_stats_name'), 'stats', ['name'], unique=True)
    op.create_table('types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_types_id'), 'types', ['id'], unique=False)
    op.create_index(op.f('ix_types_name'), 'types', ['name'], unique=True)
    op.create_table('abilities_pokemons',
    sa.Column('ability_id', sa.Integer(), nullable=False),
    sa.Column('pokemon_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['ability_id'], ['abilities.id'], ),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemons.id'], ),
    sa.PrimaryKeyConstraint('ability_id', 'pokemon_id')
    )
    op.create_table('stats_pokemons',
    sa.Column('stat_id', sa.Integer(), nullable=False),
    sa.Column('pokemon_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemons.id'], ),
    sa.ForeignKeyConstraint(['stat_id'], ['stats.id'], ),
    sa.PrimaryKeyConstraint('stat_id', 'pokemon_id')
    )
    op.create_table('types_pokemons',
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.Column('pokemon_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemons.id'], ),
    sa.ForeignKeyConstraint(['type_id'], ['types.id'], ),
    sa.PrimaryKeyConstraint('type_id', 'pokemon_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('types_pokemons')
    op.drop_table('stats_pokemons')
    op.drop_table('abilities_pokemons')
    op.drop_index(op.f('ix_types_name'), table_name='types')
    op.drop_index(op.f('ix_types_id'), table_name='types')
    op.drop_table('types')
    op.drop_index(op.f('ix_stats_name'), table_name='stats')
    op.drop_index(op.f('ix_stats_id'), table_name='stats')
    op.drop_table('stats')
    op.drop_index(op.f('ix_pokemons_name'), table_name='pokemons')
    op.drop_index(op.f('ix_pokemons_id'), table_name='pokemons')
    op.drop_table('pokemons')
    op.drop_index(op.f('ix_abilities_name'), table_name='abilities')
    op.drop_index(op.f('ix_abilities_id'), table_name='abilities')
    op.drop_table('abilities')
    # ### end Alembic commands ###
