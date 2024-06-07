from sqlalchemy.orm import Mapped, mapped_column

from .base import Model


class CategoryPostModel(Model):
    __tablename__ = "category_post"

    id_category: Mapped[int] = mapped_column(
        nullable=False,
    )
    id_user: Mapped[str] = mapped_column(
        nullable=False,
    )
