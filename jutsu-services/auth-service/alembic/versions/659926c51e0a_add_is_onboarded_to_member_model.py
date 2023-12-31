"""Add is_onboarded to Member model

Revision ID: 659926c51e0a
Revises: e298036d788e
Create Date: 2023-09-22 21:53:10.249781

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '659926c51e0a'
down_revision = 'e298036d788e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('members', sa.Column('is_onboarded', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('members', 'is_onboarded')
    # ### end Alembic commands ###
