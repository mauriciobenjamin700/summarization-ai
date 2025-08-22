from typing import Any, Optional

from sqlalchemy.orm import DeclarativeBase

from src.utils import to_dict


class BaseModel(DeclarativeBase):

    def to_dict(
        self,
        exclude: Optional[set[str]] = None,
        include: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        return to_dict(self, exclude, include)
