"""adding email

Revision ID: dc675c4aa42a
Revises: 6da2289072fc
Create Date: 2023-11-07 22:53:20.945390

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dc675c4aa42a'
down_revision: Union[str, None] = '6da2289072fc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
