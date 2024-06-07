from sqlalchemy.orm import Mapped, mapped_column

from .base import Model


class PostModel(Model):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    id_user: Mapped[str] = mapped_column(
        nullable=True,
    )
    title: Mapped[str] = mapped_column(
        nullable=False,
    )
    content: Mapped[str] = mapped_column(
        nullable=False,
    )
