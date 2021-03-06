"""users table

Revision ID: 9a877de77d49
Revises: 
Create Date: 2021-05-11 22:26:20.868948

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a877de77d49'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('surname', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_book_title'), 'book', ['title'], unique=True)
    op.create_table('borrow',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('available', sa.Boolean(), nullable=True),
    sa.Column('date_borrow', sa.Date(), nullable=True),
    sa.Column('date_return', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('borrow')
    op.drop_index(op.f('ix_book_title'), table_name='book')
    op.drop_table('book')
    op.drop_table('author')
    # ### end Alembic commands ###
