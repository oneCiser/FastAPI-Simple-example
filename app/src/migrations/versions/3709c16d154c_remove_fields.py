"""remove fields

Revision ID: 3709c16d154c
Revises: 5d5375dfa210
Create Date: 2022-02-27 21:38:44.142790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3709c16d154c'
down_revision = '5d5375dfa210'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('stats', 'is_battle_only')
    op.drop_column('stats', 'game_index')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stats', sa.Column('game_index', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('stats', sa.Column('is_battle_only', sa.BOOLEAN(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
