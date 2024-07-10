"""create student table

Revision ID: <timestamp>
Revises: 
Create Date: 2024-07-10

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '<timestamp>'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'students',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String, index=True),
        sa.Column('age', sa.Integer),
        sa.Column('grade', sa.String),
    )

def downgrade():
    op.drop_table('students')
