"""add customer banking fields

Revision ID: b9a696f17de1
Revises: fc88e021507e
Create Date: 2026-08-01 15:50:35.040152

"""

from collections.abc import Sequence
from typing import Union  # noqa: F401

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "b9a696f17de1"
down_revision: str | Sequence[str] | None = "fc88e021507e"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column(
        "customers",
        sa.Column(
            "housing",
            sa.String(length=20),
            server_default="own",
            nullable=False,
        ),
    )

    op.add_column(
        "customers",
        sa.Column(
            "saving_account",
            sa.String(length=30),
            server_default="little",
            nullable=False,
        ),
    )

    op.add_column(
        "customers",
        sa.Column(
            "checking_account",
            sa.String(length=30),
            server_default="little",
            nullable=False,
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_column("customers", "checking_account")
    op.drop_column("customers", "saving_account")
    op.drop_column("customers", "housing")