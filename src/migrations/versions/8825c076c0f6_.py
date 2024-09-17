"""empty message

Revision ID: 8825c076c0f6
Revises: 46876bd316ef
Create Date: 2024-09-16 12:21:57.833855

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8825c076c0f6'
down_revision: Union[str, None] = '46876bd316ef'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(" insert into events values"
               "('c22f8a53-2aba-4d42-997f-3070e9499621', 'задача №1'), "
               "('7d45d9fd-9fe2-4261-a01b-ba7af95d124f', 'задача №2'); ")


def downgrade() -> None:
    pass
