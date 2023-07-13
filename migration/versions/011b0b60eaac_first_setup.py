"""First setup

Revision ID: 011b0b60eaac
Revises: 
Create Date: 2023-07-10 15:17:42.342621

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '011b0b60eaac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('post_text', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_posts_id'), 'posts', ['id'], unique=False)
    op.create_index(op.f('ix_posts_owner_id'), 'posts', ['owner_id'], unique=False)
    op.create_index(op.f('ix_posts_post_text'), 'posts', ['post_text'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_posts_post_text'), table_name='posts')
    op.drop_index(op.f('ix_posts_owner_id'), table_name='posts')
    op.drop_index(op.f('ix_posts_id'), table_name='posts')
    op.drop_table('posts')
    # ### end Alembic commands ###
