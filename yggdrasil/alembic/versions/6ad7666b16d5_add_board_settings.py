"""add board settings

Revision ID: 6ad7666b16d5
Revises: 5190809011e3
Create Date: 2023-09-29 22:40:23.097370

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6ad7666b16d5"
down_revision: Union[str, None] = "5190809011e3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "user",
        sa.Column(
            "board_background_type",
            sa.Enum("COLOR", "IMAGE", "EARTHPORN", name="boardbackgroundtype", native_enum=False),
            nullable=True,
        ),
    )
    op.add_column("user", sa.Column("board_background_value", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "board_background_value")
    op.drop_column("user", "board_background_type")
    # ### end Alembic commands ###
