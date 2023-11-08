"""adding email

Revision ID: 6da2289072fc
Revises: 62b10c0c9bcb
Create Date: 2023-11-07 22:47:39.775353

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6da2289072fc'
down_revision: Union[str, None] = '62b10c0c9bcb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
