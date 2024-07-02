from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class AdModel(BaseModel):
    __tablename__ = "ads"

    ad_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    title: Mapped[str] = mapped_column(nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    views: Mapped[int] = mapped_column(nullable=False, default=0)
    position: Mapped[int] = mapped_column(nullable=False)
