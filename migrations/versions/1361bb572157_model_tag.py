"""model Tag

Revision ID: 1361bb572157
Revises: bc72e858ee07
Create Date: 2023-03-23 15:30:18.014681

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1361bb572157'
down_revision = 'bc72e858ee07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), server_default='', nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tag')
    # ### end Alembic commands ###
