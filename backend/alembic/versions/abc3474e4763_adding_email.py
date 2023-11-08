"""adding email

Revision ID: abc3474e4763
Revises: dc675c4aa42a
Create Date: 2023-11-07 22:56:25.949227

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'abc3474e4763'
down_revision: Union[str, None] = 'dc675c4aa42a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
