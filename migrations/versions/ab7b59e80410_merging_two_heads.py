"""merging two heads

Revision ID: ab7b59e80410
Revises: 1bb3abcb4c2f, 396dc5dc8e01
Create Date: 2023-05-08 14:31:57.125884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab7b59e80410'
down_revision = ('1bb3abcb4c2f', '396dc5dc8e01')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
