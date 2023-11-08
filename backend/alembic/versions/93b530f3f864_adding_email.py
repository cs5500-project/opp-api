"""adding email

Revision ID: 93b530f3f864
Revises: abc3474e4763
Create Date: 2023-11-07 23:00:35.616638

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '93b530f3f864'
down_revision: Union[str, None] = 'abc3474e4763'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
