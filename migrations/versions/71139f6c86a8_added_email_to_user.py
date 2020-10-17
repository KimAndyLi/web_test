"""added email to user

Revision ID: 71139f6c86a8
Revises: b814939763ea
Create Date: 2020-10-15 20:38:30.940232

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71139f6c86a8'
down_revision = 'b814939763ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'email')
    # ### end Alembic commands ###
