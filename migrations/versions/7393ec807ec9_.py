"""empty message

Revision ID: 7393ec807ec9
Revises: 5fffee9ee53a
Create Date: 2021-05-25 17:43:45.884568

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7393ec807ec9'
down_revision = '5fffee9ee53a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ksiazka', sa.Column('is_available', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ksiazka', 'is_available')
    # ### end Alembic commands ###