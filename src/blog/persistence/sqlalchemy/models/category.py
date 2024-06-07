from sqlalchemy.orm import Mapped, mapped_column

from .base import Model


class CategoryModel(Model):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    name: Mapped[str] = mapped_column(
        unique=True,
        nullable=False,
    )
    description: Mapped[str] = mapped_column(
        nullable=False,
    )
