"""Testing members without oauth

Revision ID: 2657b80a2c69
Revises: 7419494187b7
Create Date: 2023-07-22 21:06:28.238260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2657b80a2c69'
down_revision = '7419494187b7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_oauth_account_account_id', table_name='oauth_account')
    op.drop_index('ix_oauth_account_oauth_name', table_name='oauth_account')
    op.drop_table('oauth_account')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('oauth_account',
    sa.Column('user_id', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('oauth_name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('access_token', sa.VARCHAR(length=1024), autoincrement=False, nullable=False),
    sa.Column('expires_at', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('refresh_token', sa.VARCHAR(length=1024), autoincrement=False, nullable=True),
    sa.Column('account_id', sa.VARCHAR(length=320), autoincrement=False, nullable=False),
    sa.Column('account_email', sa.VARCHAR(length=320), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['members.id'], name='oauth_account_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='oauth_account_pkey')
    )
    op.create_index('ix_oauth_account_oauth_name', 'oauth_account', ['oauth_name'], unique=False)
    op.create_index('ix_oauth_account_account_id', 'oauth_account', ['account_id'], unique=False)
    # ### end Alembic commands ###