from datetime import datetime

from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, as_declarative, mapped_column


@as_declarative()
class BaseModel:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=func.now()
    )

    def as_dict(self, exclude: list[str] | None = None) -> dict:
        res_dict = {}

        for column in self.__table__.columns:
            if not exclude or column.name not in exclude:
                res_dict[column.name] = (
                    str(getattr(self, column.name)) if getattr(self, column.name) else None
                )

        return res_dict
