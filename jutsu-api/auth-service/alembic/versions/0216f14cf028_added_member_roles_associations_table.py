"""Added member_roles associations table

Revision ID: 0216f14cf028
Revises: 31c27945e784
Create Date: 2023-07-22 20:50:30.957284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0216f14cf028'
down_revision = '31c27945e784'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('member_roles',
    sa.Column('member_id', sa.UUID(), nullable=True),
    sa.Column('role_id', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['member_id'], ['members.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], )
    )
    op.add_column('members', sa.Column('first_name', sa.String(), nullable=False))
    op.drop_column('members', 'oirst_name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('members', sa.Column('oirst_name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('members', 'first_name')
    op.drop_table('member_roles')
    # ### end Alembic commands ###