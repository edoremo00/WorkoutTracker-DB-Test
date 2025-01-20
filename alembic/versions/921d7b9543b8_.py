"""empty message

Revision ID: 921d7b9543b8
Revises: 
Create Date: 2025-01-20 20:50:40.253130

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '921d7b9543b8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('workout_exercises', 'workout_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('workout_exercises', 'exercise_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('workout_exercises', 'exercise_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('workout_exercises', 'workout_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
