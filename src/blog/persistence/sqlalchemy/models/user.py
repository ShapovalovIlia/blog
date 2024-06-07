from sqlalchemy.orm import Mapped, mapped_column

from .base import Model


class UserModel(Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    login: Mapped[str] = mapped_column(
        unique=True,
        nullable=False,
    )
    password: Mapped[str] = mapped_column(
        nullable=False,
    )
    bio: Mapped[str] = mapped_column(
        nullable=False,
    )
