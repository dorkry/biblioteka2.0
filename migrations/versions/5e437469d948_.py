"""empty message

Revision ID: 5e437469d948
Revises: 9a877de77d49
Create Date: 2021-05-18 23:37:59.068554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e437469d948'
down_revision = '9a877de77d49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_book_title', table_name='book')
    op.drop_table('book')
    op.drop_table('borrow')
    op.drop_table('author')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=True),
    sa.Column('surname', sa.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('borrow',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('available', sa.BOOLEAN(), nullable=True),
    sa.Column('date_borrow', sa.DATE(), nullable=True),
    sa.Column('date_return', sa.DATE(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('book',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_book_title', 'book', ['title'], unique=False)
    # ### end Alembic commands ###
