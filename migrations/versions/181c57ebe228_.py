"""empty message

Revision ID: 181c57ebe228
Revises: 9a2c3ea4e99f
Create Date: 2020-08-07 15:19:19.100310

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '181c57ebe228'
down_revision = '9a2c3ea4e99f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=True))

    op.execute('UPDATE todos SET completed=false WHERE completed IS null;')
    op.alter_column('todos', 'completed', nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###
