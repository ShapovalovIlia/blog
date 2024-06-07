"""empty message

Revision ID: b7c52c512847
Revises:
Create Date: 2024-05-15 16:35:28.195313

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b7c52c512847"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column(
            "id",
            sa.Identity(start=1, increment=1),
            primary_key=True,
        ),
        sa.Column("login", sa.String(), unique=True, nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column("bio", sa.String(), nullable=False),
    )

    op.create_table(
        "tags",
        sa.Column(
            "id",
            sa.Identity(start=1, increment=1),
            primary_key=True,
        ),
        sa.Column("name", sa.String(), nullable=False, unique=True),
    )

    op.create_table(
        "categories",
        sa.Column(
            "id",
            sa.Identity(start=1, increment=1),
            primary_key=True,
        ),
        sa.Column("name", sa.String(), unique=True, nullable=False),
        sa.Column("description", sa.String(), nullable=False),
    )

    op.create_table(
        "posts",
        sa.Column(
            "id",
            sa.Identity(start=1, increment=1),
            primary_key=True,
        ),
        sa.Column("id_user", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("content", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["id_user"],
            ["user.id"],
            ondelete="CASCADE",
        ),
    )

    op.create_table(
        "category_post",
        sa.Column("id_category", sa.Integer(), nullable=False),
        sa.Column("id_post", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["id_category"],
            ["category.id"],
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["id_post"],
            ["posts.id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id_category", "id_post"),
    )

    op.create_table(
        "tag_post",
        sa.Column("id_tag", sa.Integer(), nullable=False),
        sa.Column("id_post", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["id_tag"],
            ["tags.id"],
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["ip_post"],
            ["posts.id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id_tag", "id_post"),
    )


def downgrade() -> None:
    op.drop_table("users")
    op.drop_table("tags")
    op.drop_table("category")
    op.drop_table("post")
    op.drop_table("category_post")
    op.drop_table("tag_post")
