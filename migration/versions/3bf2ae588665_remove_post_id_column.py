"""remove post id column

Revision ID: 3bf2ae588665
Revises: a65deb81fa14
Create Date: 2023-07-16 15:32:09.630260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3bf2ae588665'
down_revision = 'a65deb81fa14'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('userInformationPost', 'owner_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
    op.drop_index('ix_userInformationPost_id', table_name='userInformationPost')
    op.drop_column('userInformationPost', 'id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('userInformationPost', sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"userInformationPost_id_seq"\'::regclass)'), autoincrement=True, nullable=False))
    op.create_index('ix_userInformationPost_id', 'userInformationPost', ['id'], unique=False)
    op.alter_column('userInformationPost', 'owner_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)
    # ### end Alembic commands ###