"""esquema_modificado

Revision ID: 43ffe3deab5a
Revises: 87d09239bb04
Create Date: 2025-05-18 13:43:23.852223
PREGUNTAR SI VA A EJECUTAR ESTE COMO UN ESQUEMA DIFERENTE AL DE ANTES O COMO UNA ACTUALIZACION DEL ANTERIOR
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '43ffe3deab5a'
down_revision: Union[str, None] = '87d09239bb04'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
